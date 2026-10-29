
# ==========================================================
# TRAINING, VALIDATION, TEST, OVERFITTING E UNDERFITTING
# ==========================================================

# Nel Machine Learning dobbiamo verificare quanto un modello
# riesca a effettuare previsioni corrette sui dati conosciuti
# e soprattutto sui dati nuovi.

# L'obiettivo principale è la GENERALIZZAZIONE:
# la capacità del modello di fare previsioni corrette
# su osservazioni mai viste durante l'addestramento.


# ==========================================================
# 1. ERRORE DI TRAINING ED ERRORE DI TEST
# ==========================================================

# ERRORE DI TRAINING:
# Misura quanto il modello sbaglia sui dati utilizzati
# durante l'addestramento.
# Un errore basso indica che il modello si adatta bene
# ai dati che ha già visto.

# ERRORE DI TEST:
# Misura quanto il modello sbaglia su dati nuovi,
# mai utilizzati durante l'addestramento.
# Serve a valutare la capacità di generalizzazione.

# Nella classificazione possiamo utilizzare l'accuracy:
# Accuracy = numero di previsioni corrette / numero totale di previsioni.

# L'accuracy varia da 0 a 1:
# 1.0 = 100% di previsioni corrette.
# 0.8 = 80% di previsioni corrette.
# 0.5 = 50% di previsioni corrette.

# Se l'errore è la percentuale di previsioni sbagliate:
# Errore = 1 - Accuracy.

# Esempio:
accuracy = 0.90
errore = 1 - accuracy

print("Accuracy:", accuracy)
print("Errore:", errore)

# ATTENZIONE:
# Un modello con accuracy molto alta sul training
# non è necessariamente un buon modello.
# Dobbiamo verificare anche le prestazioni sui dati nuovi.


# ==========================================================
# 2. BIAS E VARIANZA
# ==========================================================

# BIAS (DISTORSIONE):
# Rappresenta la tendenza del modello a commettere
# errori sistematici a causa di ipotesi troppo semplici.

# BIAS ALTO:
# Il modello è troppo semplice.
# Non riesce a riconoscere le relazioni presenti nei dati.
# Questo comportamento è associato all'UNDERFITTING.

# BIAS BASSO:
# Il modello è più flessibile e riesce a rappresentare
# anche relazioni più complesse.

# VARIANZA:
# Rappresenta quanto cambiano le previsioni del modello
# quando viene addestrato su campioni differenti.

# VARIANZA ALTA:
# Il modello è instabile.
# È molto sensibile ai dati utilizzati durante l'addestramento.
# Rischia di imparare anche rumore e particolarità dei dati.
# Questo comportamento è associato all'OVERFITTING.

# VARIANZA BASSA:
# Il modello è più stabile.
# Le sue previsioni cambiano meno al variare dei dati di training.

# DIFFERENZA PRINCIPALE:
# Bias alto = modello troppo semplice.
# Varianza alta = modello troppo sensibile ai dati.

# L'obiettivo è trovare un equilibrio tra bias e varianza.


# ==========================================================
# 3. OVERFITTING E UNDERFITTING
# ==========================================================

# OVERFITTING:
# Si verifica quando il modello si adatta eccessivamente
# ai dati di addestramento.
# Il modello può imparare anche il rumore presente nei dati.
# Ottiene risultati molto buoni sul training,
# ma risultati peggiori sui dati nuovi.
# È generalmente associato ad alta varianza.

# UNDERFITTING:
# Si verifica quando il modello è troppo semplice.
# Non riesce a comprendere le relazioni importanti nei dati.
# Ottiene risultati scarsi sia sul training sia sul test.
# È generalmente associato ad alto bias.

# NEL KNN:

# K PICCOLO:
# Il modello considera pochi vicini.
# Diventa molto sensibile ai singoli dati e al rumore.
# Aumenta il rischio di overfitting.

# K GRANDE:
# Il modello considera molti vicini.
# Le differenze tra le classi tendono ad appiattirsi.
# Aumenta il rischio di underfitting.

# K INTERMEDIO:
# Può offrire un buon equilibrio tra bias e varianza.
# Il valore migliore dipende dal dataset.


# ==========================================================
# 4. TRAINING, VALIDATION E TEST
# ==========================================================

# Per valutare correttamente un modello possiamo dividere
# il dataset in tre parti:

# TRAINING SET:
# Contiene i dati utilizzati per addestrare il modello.
# Su questi dati utilizziamo il metodo fit().

# VALIDATION SET:
# Contiene dati utilizzati per confrontare modelli diversi.
# Serve soprattutto per scegliere gli iperparametri migliori.
# Esempio: scegliere il valore migliore di K nel KNN.

# TEST SET:
# Contiene dati che rimangono separati durante
# l'addestramento e la scelta degli iperparametri.
# Serve per valutare il modello finale.

# Esempio di suddivisione:
# 60% Training.
# 20% Validation.
# 20% Test.

# IMPORTANTE:
# Non dobbiamo scegliere gli iperparametri utilizzando il test.
# Altrimenti rischiamo di adattare indirettamente il modello
# anche ai dati che dovrebbero servire alla valutazione finale.


# ==========================================================
# 5. ESEMPIO INTERMEDIO - TRAINING, VALIDATION E TEST
# ==========================================================

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Carichiamo il dataset e separiamo X e y
X, y = load_breast_cancer(return_X_y=True)

# Prima suddivisione:
# 80% dei dati temporanei e 20% dei dati per il test
X_temp, X_test, y_temp, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Seconda suddivisione:
# Dividiamo l'80% precedente in training e validation
X_train, X_val, y_train, y_val = train_test_split(
    X_temp, y_temp,
    test_size=0.25,
    random_state=42
)

# ATTENZIONE:
# Il 25% dell'80% corrisponde al 20% del dataset originale.

# Suddivisione finale:
# X_train = 60% del dataset.
# X_val = 20% del dataset.
# X_test = 20% del dataset.

# Creiamo due variabili per memorizzare il risultato migliore
migliore_k = None
migliore_val = None

# Proviamo tutti i valori dispari di K da 1 a 29
for k in range(1, 31, 2):

    # Creiamo il modello con il valore corrente di K
    knn = KNeighborsClassifier(n_neighbors=k)

    # Addestriamo il modello sui dati di training
    knn.fit(X_train, y_train)

    # Calcoliamo l'accuracy sui dati di validation
    val = knn.score(X_val, y_val)

    # Verifichiamo se il risultato è migliore del precedente
    if migliore_val is None or val > migliore_val:

        # Salviamo la migliore accuracy
        migliore_val = val

        # Salviamo il valore di K corrispondente
        migliore_k = k

# Una volta trovato il miglior K, creiamo il modello finale
finale = KNeighborsClassifier(n_neighbors=migliore_k)

# Addestriamo il modello sull'80% dei dati
# Riuniamo quindi training e validation
finale.fit(X_temp, y_temp)

# Stampiamo il miglior valore di K
print("\nK scelto:", migliore_k)

# Valutiamo il modello finale sui dati di test
print("Accuracy finale sul test:", round(finale.score(X_test, y_test), 3))


# ==========================================================
# 6. SPIEGAZIONE DELL'ESEMPIO PRECEDENTE
# ==========================================================

# return_X_y=True:
# Restituisce direttamente le caratteristiche X
# e le etichette y del dataset.

# test_size=0.2:
# Destina il 20% dei dati al test.

# test_size=0.25:
# Nella seconda divisione destina il 25% dei dati
# temporanei alla validation.

# random_state=42:
# Permette di ottenere sempre la stessa suddivisione casuale.

# migliore_k:
# Memorizza il valore di K che ha ottenuto il risultato migliore.

# migliore_val:
# Memorizza la migliore accuracy sulla validation.

# range(1, 31, 2):
# Genera i valori dispari da 1 a 29.

# knn.fit(X_train, y_train):
# Addestra il modello utilizzando soltanto il training set.

# knn.score(X_val, y_val):
# Valuta il modello sul validation set.
# Nel KNeighborsClassifier score() restituisce l'accuracy.

# if migliore_val is None or val > migliore_val:
# Controlla se è il primo risultato
# oppure se la nuova accuracy è migliore della precedente.

# finale.fit(X_temp, y_temp):
# Addestra nuovamente il modello utilizzando
# training e validation insieme.

# finale.score(X_test, y_test):
# Valuta il modello finale sul test set.

# CONCLUSIONE:
# Utilizziamo il training per addestrare,
# la validation per scegliere K
# e il test per valutare il modello finale.


# ==========================================================
# 7. ESEMPIO PRATICO - OVERFITTING E UNDERFITTING
# ==========================================================

from sklearn.datasets import make_moons

# Generiamo un dataset con 400 osservazioni
# noise=0.35 introduce una quantità elevata di rumore
X, y = make_moons(
    n_samples=400,
    noise=0.35,
    random_state=42
)

# Dividiamo i dati in 70% training e 30% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=42
)

# Confrontiamo due valori differenti di K
for k in [1, 15]:

    # Creiamo il modello con il valore corrente di K
    knn = KNeighborsClassifier(n_neighbors=k)

    # Addestriamo il modello sui dati di training
    knn.fit(X_train, y_train)

    # Calcoliamo l'accuracy sui dati di training
    accuracy_train = knn.score(X_train, y_train)

    # Calcoliamo l'accuracy sui dati di test
    accuracy_test = knn.score(X_test, y_test)

    # Stampiamo i risultati
    print("\nK:", k)
    print("Accuracy training:", round(accuracy_train, 2))
    print("Accuracy test:", round(accuracy_test, 2))


# ==========================================================
# 8. INTERPRETAZIONE DEI RISULTATI
# ==========================================================

# RISULTATI MOSTRATI DAL PROFESSORE:

# K = 1:
# Accuracy training = 1.00
# Accuracy test = 0.83

# K = 15:
# Accuracy training = 0.87
# Accuracy test = 0.89

# CON K = 1:
# Il modello considera soltanto il vicino più prossimo.
# Sul training ottiene accuracy pari a 1.
# Questo accade perché ogni punto trova se stesso
# come vicino a distanza zero.
# Sul test l'accuracy diminuisce.
# Il modello è troppo sensibile ai dati di addestramento.
# Questo è un comportamento tipico dell'overfitting.

# CON K = 15:
# Il modello considera 15 vicini.
# È meno sensibile ai singoli punti e al rumore.
# L'accuracy sul training è inferiore,
# ma sul test il risultato è migliore.
# In questo caso il modello generalizza meglio.

# CONCLUSIONE:
# Un'accuracy elevata sul training non garantisce
# buone prestazioni sui dati nuovi.
# Dobbiamo valutare la capacità di generalizzazione.


# ==========================================================
# 9. ESEMPIO AVANZATO - CURVA DI COMPLESSITÀ DEL KNN
# ==========================================================

import matplotlib.pyplot as plt

# Generiamo nuovamente il dataset make_moons
X, y = make_moons(
    n_samples=400,
    noise=0.35,
    random_state=42
)

# Dividiamo i dati in training e test
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=42
)

# Creiamo una sequenza di valori di K da 1 a 251
# Aumentiamo K di 5 a ogni iterazione
valori_k = range(1, 252, 5)

# Creiamo due liste vuote per salvare le accuracy
acc_train = []
acc_test = []

# Ripetiamo l'addestramento per ogni valore di K
for k in valori_k:

    # Creiamo il modello con il valore corrente di K
    knn = KNeighborsClassifier(n_neighbors=k)

    # Addestriamo il modello
    knn.fit(X_train, y_train)

    # Calcoliamo e salviamo l'accuracy sul training
    acc_train.append(knn.score(X_train, y_train))

    # Calcoliamo e salviamo l'accuracy sul test
    acc_test.append(knn.score(X_test, y_test))

# Creiamo il grafico dell'accuracy sul training
plt.plot(valori_k, acc_train, label="Training")

# Creiamo il grafico dell'accuracy sul test
plt.plot(valori_k, acc_test, label="Test")

# Impostiamo le etichette degli assi
plt.xlabel("K (a sinistra complesso, a destra semplice)")
plt.ylabel("Accuratezza")

# Mostriamo la legenda
plt.legend()

# Impostiamo il titolo del grafico
plt.title("Curva di complessità del KNN")

# Mostriamo il grafico
plt.show()


# ==========================================================
# 10. SPIEGAZIONE DEL GRAFICO
# ==========================================================

# valori_k = range(1, 252, 5):
# Genera i valori di K partendo da 1 fino a 251
# con incrementi di 5.

# acc_train = []:
# Lista utilizzata per salvare le accuracy sul training.

# acc_test = []:
# Lista utilizzata per salvare le accuracy sul test.

# append():
# Aggiunge un nuovo elemento alla fine della lista.
# In questo caso aggiungiamo l'accuracy ottenuta dal modello.

# plt.plot():
# Crea un grafico a linee.

# plt.xlabel():
# Imposta il nome dell'asse X.

# plt.ylabel():
# Imposta il nome dell'asse Y.

# plt.legend():
# Mostra la legenda delle due linee.

# plt.title():
# Imposta il titolo del grafico.

# plt.show():
# Visualizza il grafico.


# ==========================================================
# 11. COME INTERPRETARE LA CURVA DI COMPLESSITÀ
# ==========================================================

# PARTE SINISTRA DEL GRAFICO:
# K è piccolo.
# Il modello è molto complesso.
# L'accuracy sul training tende a essere molto alta.
# L'accuracy sul test può essere più bassa.
# Aumenta il rischio di overfitting.

# PARTE CENTRALE DEL GRAFICO:
# K assume valori intermedi.
# Il modello può raggiungere un equilibrio tra bias e varianza.
# L'accuracy sui dati nuovi può raggiungere i valori migliori.

# PARTE DESTRA DEL GRAFICO:
# K è grande.
# Il modello diventa progressivamente più semplice.
# Considera molti vicini e tende ad appiattire le differenze.
# Aumenta il rischio di underfitting.

# ATTENZIONE:
# In questo esempio il professore utilizza il test
# per mostrare graficamente le prestazioni al variare di K.
# Se volessimo scegliere il miglior K, sarebbe più corretto
# utilizzare un validation set al posto del test.
# Il test dovrebbe rimanere separato fino alla valutazione finale.


# ==========================================================
# 12. RIEPILOGO FINALE
# ==========================================================

# TRAINING:
# Serve per addestrare il modello.

# VALIDATION:
# Serve per scegliere gli iperparametri migliori.

# TEST:
# Serve per valutare il modello finale su dati nuovi.

# BIAS ALTO:
# Modello troppo semplice.
# Rischio di underfitting.

# VARIANZA ALTA:
# Modello instabile e troppo sensibile ai dati.
# Rischio di overfitting.

# K PICCOLO:
# Modello complesso, maggior rischio di overfitting.

# K GRANDE:
# Modello semplice, maggior rischio di underfitting.

# K INTERMEDIO:
# Può rappresentare un buon equilibrio tra bias e varianza.

# OBIETTIVO FINALE:
# Non dobbiamo ottenere soltanto un'accuracy elevata
# sui dati di training.
# Dobbiamo costruire un modello capace di generalizzare
# correttamente anche sui dati mai visti.
