import sys
import sklearn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer, make_moons
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report
from sklearn.inspection import DecisionBoundaryDisplay

# PUNTO 1 - DEFINIZIONE DEL PROBLEMA

print("\nPUNTO 1 - Classificazione supervisionata binaria")
print("Target: 0 = maligno, 1 = benigno")


# PUNTO 2 - ESPLORAZIONE DEI DATI

# as_frame=True permette di ottenere DataFrame e Series Pandas.
dataset = load_breast_cancer(as_frame=True)

# Separiamo X e y: il target non deve rimanere dentro X.
X = dataset.data
y = dataset.target

print("\nPUNTO 2 - ESPLORAZIONE")
print("Dimensioni X:", X.shape)
print("Dimensioni y:", y.shape)
print("Nomi delle feature:\n", list(dataset.feature_names))
print("Nomi delle classi:", list(dataset.target_names))
print("\nPrime 5 righe:\n", X.head())

print("\nDESCRIZIONE DEL DATASET:\n", dataset.DESCR)

print("\nConteggio delle classi:\n", y.value_counts().sort_index())
print("Percentuali delle classi:\n", (y.value_counts(normalize=True).sort_index() * 100).round(2))
print("Le classi non sono perfettamente bilanciate: prevalgono i benigni.")

# describe() restituisce anche minimo e massimo di ogni feature.
riepilogo = X.describe()
print("\nMinimo e massimo per feature:\n", riepilogo.loc[["min", "max"]].T)

# L'ampiezza (massimo - minimo) misura la scala numerica della colonna.
ampiezze = X.max() - X.min()
feature_grande = ampiezze.idxmax()
feature_piccola = ampiezze.idxmin()
print("\nScala maggiore:", feature_grande, "- ampiezza:", round(ampiezze.max(), 6))
print("Scala minore:", feature_piccola, "- ampiezza:", round(ampiezze.min(), 6))

# PUNTO 3 - DIVISIONE 60% TRAINING / 20% VALIDATION / 20% TEST

X_temp, X_test, y_temp, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

X_train, X_val, y_train, y_val = train_test_split(
    X_temp, y_temp, test_size=0.25, random_state=42, stratify=y_temp
)

print("\nPUNTO 3 - SUDDIVISIONE DEI DATI")
print("Training:", X_train.shape, y_train.shape)
print("Validation:", X_val.shape, y_val.shape)
print("Test:", X_test.shape, y_test.shape)


for nome, etichette in [("Training", y_train), ("Validation", y_val), ("Test", y_test)]:
    percentuale_maligni = (etichette == 0).mean() * 100
    print("Percentuale maligni", nome + ":", round(percentuale_maligni, 2), "%")



# PUNTO 4 - BASELINE CON DUMMYCLASSIFIER

dummy = DummyClassifier(strategy="most_frequent")
dummy.fit(X_train, y_train)
pred_dummy_val = dummy.predict(X_val)

print("\nPUNTO 4 - BASELINE")
print("Accuracy Dummy:", round(accuracy_score(y_val, pred_dummy_val), 4))
print("Recall maligni Dummy:", round(recall_score(y_val, pred_dummy_val, pos_label=0, zero_division=0), 4))


# PUNTO 5 - KNN SENZA SCALING

knn_grezzo = KNeighborsClassifier(n_neighbors=5)
knn_grezzo.fit(X_train, y_train)
pred_knn_grezzo = knn_grezzo.predict(X_val)

print("\nPUNTO 5 - KNN SENZA SCALING")
print("Accuracy training:", round(knn_grezzo.score(X_train, y_train), 4))
print("Accuracy validation:", round(knn_grezzo.score(X_val, y_val), 4))


campione = X_val.iloc[[0]] #prende solo riga 1 
distanze, indici = knn_grezzo.kneighbors(campione)

for i in range(5):
    indice = indici[0][i]
    distanza = distanze[0][i]
    classe = y_train.iloc[indice]
    print("Vicino:", i + 1, "Indice training:", indice,
          "Distanza:", round(distanza, 4), "Classe:", classe)

probabilita = knn_grezzo.predict_proba(campione)[0]
print("Classi nell'ordine:", knn_grezzo.classes_)
print("Frazione dei voti:", probabilita.round(3))
print("Previsione:", knn_grezzo.predict(campione)[0])
print("Classe reale:", y_val.iloc[0])
print("Feature con ampiezza maggiore:", feature_grande)

# PUNTO 6 - SCALING CORRETTO

# Lo scaler impara media e deviazione standard solo sul training.
standard = StandardScaler()
X_train_std = standard.fit_transform(X_train)
X_val_std = standard.transform(X_val)


print("\nPUNTO 6 - STANDARD SCALER")
print("Medie training standardizzato:", X_train_std.mean(axis=0).round(2))
print("Deviazioni std training:", X_train_std.std(axis=0).round(2))
print("Medie validation standardizzata:", X_val_std.mean(axis=0).round(2))

# La validation non ha obbligatoriamente media 0:
# le medie e le deviazioni standard sono state imparate sul training.
knn_std = KNeighborsClassifier(n_neighbors=5)
knn_std.fit(X_train_std, y_train)
print("Accuracy KNN grezzo validation:", round(knn_grezzo.score(X_val, y_val), 4))
print("Accuracy KNN standard validation:", round(knn_std.score(X_val_std, y_val), 4))

# MinMaxScaler porta ciascuna colonna del training tra 0 e 1.
minmax = MinMaxScaler()
X_train_minmax = minmax.fit_transform(X_train)
X_val_minmax = minmax.transform(X_val)
knn_minmax = KNeighborsClassifier(n_neighbors=5)
knn_minmax.fit(X_train_minmax, y_train)
print("Accuracy KNN MinMax validation:", round(knn_minmax.score(X_val_minmax, y_val), 4))

# PUNTO 7 - SCELTA DI K E CURVA DI COMPLESSITA'

valori_k = range(1, 42, 2)
acc_train = []
acc_val = []
migliore_k = None
migliore_accuracy_knn = -1

for k in valori_k:
    modello = KNeighborsClassifier(n_neighbors=k)
    modello.fit(X_train_std, y_train)
    accuracy_train = modello.score(X_train_std, y_train)
    accuracy_val = modello.score(X_val_std, y_val)
    acc_train.append(accuracy_train)
    acc_val.append(accuracy_val)

    if accuracy_val > migliore_accuracy_knn:
        migliore_accuracy_knn = accuracy_val
        migliore_k = k

print("\nPUNTO 7 - SCELTA DI K")
print("K migliore:", migliore_k)
print("Accuracy validation:", round(migliore_accuracy_knn, 4))

plt.figure()
plt.plot(valori_k, acc_train, label="Training")
plt.plot(valori_k, acc_val, label="Validation")
plt.axvline(migliore_k, linestyle="--", label="K scelto")
plt.title("Curva di complessita' KNN")
plt.xlabel("Numero di vicini K")
plt.ylabel("Accuracy")
plt.legend()
plt.grid()
plt.show()

# PUNTO 8 - ALBERO DI DECISIONE

profondita = [1, 2, 3, 5, 8, None]
risultati_albero = []
migliore_depth = None
migliore_accuracy_albero = -1

for depth in profondita:
    modello = DecisionTreeClassifier(max_depth=depth, random_state=42)
    modello.fit(X_train, y_train)
    accuracy_train = modello.score(X_train, y_train)
    accuracy_val = modello.score(X_val, y_val)

    risultati_albero.append({
        "Profondita": str(depth),
        "Foglie": modello.get_n_leaves(),
        "Accuracy Train": accuracy_train,
        "Accuracy Validation": accuracy_val
    })

    # In caso di pareggio scegliamo la prima profondita' 
    if accuracy_val > migliore_accuracy_albero:
        migliore_accuracy_albero = accuracy_val
        migliore_depth = depth

df_albero = pd.DataFrame(risultati_albero)
print("\nPUNTO 8 - DECISION TREE")
print(df_albero.round(4).to_string(index=False))
print("Profondita' scelta:", migliore_depth)
print("Accuracy validation:", round(migliore_accuracy_albero, 4))

albero_scelto = DecisionTreeClassifier(max_depth=migliore_depth, random_state=42)
albero_scelto.fit(X_train, y_train)
print("\nREGOLE DELL'ALBERO")
print(export_text(albero_scelto, feature_names=list(X.columns)))

indice_feature = albero_scelto.tree_.feature[0]
soglia_radice = albero_scelto.tree_.threshold[0]
print("Prima regola: se", X.columns[indice_feature], "<=", round(soglia_radice, 3),
      "si va a sinistra, altrimenti a destra.")

nodo_sinistro = albero_scelto.tree_.children_left[0]
indice_seconda = albero_scelto.tree_.feature[nodo_sinistro]
if indice_seconda >= 0:
    soglia_seconda = albero_scelto.tree_.threshold[nodo_sinistro]
    print("Seconda regola (ramo sinistro): se", X.columns[indice_seconda],
          "<=", round(soglia_seconda, 3), "si va a sinistra, altrimenti a destra.")
else:
    print("Seconda regola: il ramo sinistro e' gia' una foglia.")

# Calcoliamo manualmente Gini alla radice con i dati di training.
p_maligni = (y_train == 0).mean()
p_benigni = (y_train == 1).mean()
gini_manual = 1 - (p_maligni ** 2 + p_benigni ** 2)
print("Gini manuale radice:", round(gini_manual, 6))
print("Gini dell'albero:", round(albero_scelto.tree_.impurity[0], 6))

# Lo scaling preserva l'ordine dei valori e quindi le divisioni dell'albero.
albero_scalato = DecisionTreeClassifier(max_depth=migliore_depth, random_state=42)
albero_scalato.fit(X_train_std, y_train)
print("Accuracy albero non scalato:", round(albero_scelto.score(X_val, y_val), 4))
print("Accuracy albero scalato:", round(albero_scalato.score(X_val_std, y_val), 4))

# Scegliamo in anticipo il modello clinico utilizzando SOLO la validation.
# Il recall della classe 0 misura quanti maligni vengono riconosciuti.
knn_selezionato = KNeighborsClassifier(n_neighbors=migliore_k)
knn_selezionato.fit(X_train_std, y_train)
recall_knn_val = recall_score(y_val, knn_selezionato.predict(X_val_std), pos_label=0)
recall_albero_val = recall_score(y_val, albero_scelto.predict(X_val), pos_label=0)

print("\nSCELTA CLINICA SULLA VALIDATION")
print("Recall maligni KNN:", round(recall_knn_val, 4))
print("Recall maligni albero:", round(recall_albero_val, 4))

# In caso di parita' scegliamo il modello con accuracy validation piu' alta.
if recall_albero_val > recall_knn_val:
    scelta_clinica = "Decision Tree"
elif recall_knn_val > recall_albero_val:
    scelta_clinica = "KNN"
elif migliore_accuracy_albero > migliore_accuracy_knn:
    scelta_clinica = "Decision Tree"
else:
    scelta_clinica = "KNN"

print("Modello scelto prima del test:", scelta_clinica)


# PUNTO 9 - VALUTAZIONE FINALE SUL TEST (UNA SOLA VOLTA)

# X_temp e y_temp contengono training + validation (80%).
# Rifacciamo lo scaler sul nuovo training senza usare il test per il fit.
scaler_finale = StandardScaler()
X_temp_std = scaler_finale.fit_transform(X_temp)
X_test_std = scaler_finale.transform(X_test)

knn_finale = KNeighborsClassifier(n_neighbors=migliore_k)
knn_finale.fit(X_temp_std, y_temp)

albero_finale = DecisionTreeClassifier(max_depth=migliore_depth, random_state=42)
albero_finale.fit(X_temp, y_temp)

dummy_finale = DummyClassifier(strategy="most_frequent")
dummy_finale.fit(X_temp, y_temp)

modelli_finali = {
    "Dummy": (dummy_finale, X_test),
    "KNN": (knn_finale, X_test_std),
    "Decision Tree": (albero_finale, X_test)
}

risultati_finali = []
matrici_finali = {}

for nome, (modello, dati_test) in modelli_finali.items():
    y_pred = modello.predict(dati_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, pos_label=0, zero_division=0)
    recall = recall_score(y_test, y_pred, pos_label=0, zero_division=0)
    f1 = f1_score(y_test, y_pred, pos_label=0, zero_division=0)
    matrice = confusion_matrix(y_test, y_pred, labels=[0, 1])
    matrici_finali[nome] = matrice

    risultati_finali.append({
        "Modello": nome,
        "Accuracy": accuracy,
        "Precision maligni": precision,
        "Recall maligni": recall,
        "F1 maligni": f1
    })

    print("\nCLASSIFICATION REPORT -", nome)
    print(classification_report(
        y_test, y_pred, labels=[0, 1],
        target_names=["Maligno", "Benigno"], zero_division=0
    ))

print("\nPUNTO 9 - TABELLA FINALE TEST")
df_finale = pd.DataFrame(risultati_finali)
print(df_finale.round(4).to_string(index=False))

# Disegniamo le matrici di confusione dei due modelli addestrati.
for nome in ["KNN", "Decision Tree"]:
    disp = ConfusionMatrixDisplay(
        confusion_matrix=matrici_finali[nome],
        display_labels=["Maligno (0)", "Benigno (1)"]
    )
    disp.plot()
    plt.title("Matrice di confusione - " + nome)
    plt.xlabel("Classe prevista")
    plt.ylabel("Classe reale")
    plt.show()


matrice_scelta = matrici_finali[scelta_clinica]
tp = matrice_scelta[0][0]
fn = matrice_scelta[0][1]
fp = matrice_scelta[1][0]
tn = matrice_scelta[1][1]

precision_manual = tp / (tp + fp) if tp + fp > 0 else 0
recall_manual = tp / (tp + fn) if tp + fn > 0 else 0

print("\nVERIFICA MANUALE -", scelta_clinica)
print("TP maligni riconosciuti:", tp)
print("TN benigni riconosciuti:", tn)
print("FP benigni segnalati maligni:", fp)
print("FN maligni non riconosciuti:", fn)
print("Precision manuale:", round(precision_manual, 4))
print("Recall manuale:", round(recall_manual, 4))


print("\nCONCLUSIONE CLINICA (4-5 RIGHE)")
print("1. Il nostro obiettivo principale e' limitare i falsi negativi dei maligni.")
print("2. Sulla validation abbiamo scelto:", scelta_clinica)
print("3. Sul test la recall dei maligni e':", round(recall_manual, 4))
print("4. I maligni non riconosciuti sul test sono:", fn, "su", tp + fn)
print("5. Il risultato e' su dati mai usati per addestrare o scegliere il modello.")

# Stima da comunicare alla direzione: recall dei maligni,
# numero di maligni sfuggiti e accuracy sul test indipendente.
if scelta_clinica == "KNN":
    y_scelto = knn_finale.predict(X_test_std)
else:
    y_scelto = albero_finale.predict(X_test)

print("\nSTIMA FINALE PER LA DIREZIONE")
print("Modello selezionato:", scelta_clinica)
print("Accuracy sul test:", round(accuracy_score(y_test, y_scelto), 4))
print("Recall maligni sul test:", round(recall_score(y_test, y_scelto, pos_label=0), 4))
print("Maligni non riconosciuti:", fn, "su", tp + fn)
print("Test indipendente: usato una sola volta alla fine.")
print("Limite: un solo split e pochi maligni nel test; servono altre verifiche.")
print("Esercizio didattico: non e' un sistema validato per uso clinico.")

# PUNTO 10 - BONUS 1: KNN CON VOTI PESATI PER DISTANZA

# Usiamo il training e la validation originali: non scegliamo sul test.
knn_uniform = KNeighborsClassifier(n_neighbors=migliore_k, weights="uniform")
knn_distance = KNeighborsClassifier(n_neighbors=migliore_k, weights="distance")
knn_uniform.fit(X_train_std, y_train)
knn_distance.fit(X_train_std, y_train)
print("\nBONUS 1 - PESI DEI VICINI")
print("Validation uniform:", round(knn_uniform.score(X_val_std, y_val), 4))
print("Validation distance:", round(knn_distance.score(X_val_std, y_val), 4))

# PUNTO 10 - BONUS 2: 5 SPLIT E CURVE DI VALIDATION

stati = [0, 10, 21, 42, 100]
plt.figure()

for stato in stati:
    # Separiamo il test di questo esperimento, senza utilizzarlo.
    X_t, X_test_bonus, y_t, y_test_bonus = train_test_split(
        X, y, test_size=0.2, random_state=stato, stratify=y
    )
    X_tr, X_v, y_tr, y_v = train_test_split(
        X_t, y_t, test_size=0.25, random_state=stato, stratify=y_t
    )

    scaler_bonus = StandardScaler()
    X_tr_std = scaler_bonus.fit_transform(X_tr)
    X_v_std = scaler_bonus.transform(X_v)
    accuracy_bonus = []
    k_bonus = None
    migliore_bonus = -1

    for k in valori_k:
        knn_bonus = KNeighborsClassifier(n_neighbors=k)
        knn_bonus.fit(X_tr_std, y_tr)
        risultato = knn_bonus.score(X_v_std, y_v)
        accuracy_bonus.append(risultato)
        if risultato > migliore_bonus:
            migliore_bonus = risultato
            k_bonus = k

    plt.plot(valori_k, accuracy_bonus, label="random_state=" + str(stato))
    print("BONUS 2 - Stato:", stato, "K migliore:", k_bonus,
          "Accuracy validation:", round(migliore_bonus, 4))

plt.title("Validation KNN con 5 suddivisioni")
plt.xlabel("Numero di vicini K")
plt.ylabel("Accuracy validation")
plt.legend()
plt.grid()
plt.show()

# Un singolo split puo' cambiare il migliore K.
# La cross-validation utilizza piu' suddivisioni per stimare meglio le prestazioni.


# PUNTO 10 - BONUS 3: CONFINI DI DECISIONE SU MAKE_MOONS


X_moons, y_moons = make_moons(n_samples=300, noise=0.25, random_state=42)
modelli_moons = {
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "Decision Tree": DecisionTreeClassifier(max_depth=5, random_state=42)
}

for nome, modello in modelli_moons.items():
    modello.fit(X_moons, y_moons)
    plt.figure()
    DecisionBoundaryDisplay.from_estimator(
        modello, X_moons, response_method="predict", alpha=0.3, ax=plt.gca()
    )
    for classe in [0, 1]:
        plt.scatter(X_moons[y_moons == classe, 0], X_moons[y_moons == classe, 1],
                    s=18, label="Classe " + str(classe))
    plt.legend()
    plt.title("Regioni di decisione - " + nome)
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.show()