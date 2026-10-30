
# ==========================================================
# MATRICE DI CONFUSIONE E METRICHE DI CLASSIFICAZIONE
# ==========================================================

# La matrice di confusione (Confusion Matrix) è uno strumento
# utilizzato per valutare le prestazioni di un modello di classificazione.

# Permette di confrontare le classi reali (y_true)
# con le classi previste dal modello (y_pred).

# A differenza dell'accuracy, permette di capire
# quali tipi di errori vengono commessi dal modello.


# ==========================================================
# 1. MATRICE DI CONFUSIONE BINARIA
# ==========================================================

# In un problema di classificazione binaria abbiamo due classi:
# Classe negativa (0).
# Classe positiva (1).

# La classe positiva è quella che vogliamo individuare.
# Per esempio, in una diagnosi medica:
# 0 = assenza della malattia.
# 1 = presenza della malattia.

# La matrice di confusione contiene quattro valori:

#                         PREDIZIONE
#                         0        1
# CLASSE REALE     0      TN       FP
#                  1      FN       TP

# Le righe rappresentano le classi reali.
# Le colonne rappresentano le classi previste.

# TN (TRUE NEGATIVE):
# Il modello prevede negativo e la classe reale è negativa.
# La previsione è corretta.

# FP (FALSE POSITIVE):
# Il modello prevede positivo ma la classe reale è negativa.
# Il modello genera un falso allarme.

# FN (FALSE NEGATIVE):
# Il modello prevede negativo ma la classe reale è positiva.
# Il modello non riconosce un caso realmente positivo.

# TP (TRUE POSITIVE):
# Il modello prevede positivo e la classe reale è positiva.
# La previsione è corretta.

# La gravità di un falso positivo o di un falso negativo
# dipende dal problema che stiamo analizzando.

# ESEMPIO - DIAGNOSI MEDICA:
# FP = una persona sana viene classificata come malata.
# FN = una persona malata viene classificata come sana.
# In molti contesti diagnostici un FN può essere particolarmente grave.

# ESEMPIO - FILTRO SPAM:
# FP = un'email importante viene classificata come spam.
# FN = un'email spam non viene riconosciuta.
# Un FP può essere più grave perché rischiamo di perdere email importanti.


# ==========================================================
# 2. CONFUSION_MATRIX IN SCIKIT-LEARN
# ==========================================================

# confusion_matrix(y_true, y_pred):
# Confronta i valori reali con quelli previsti dal modello.
# Restituisce una matrice contenente TN, FP, FN e TP.

# Per una classificazione binaria con etichette 0 e 1,
# la matrice è organizzata in questo ordine:

# [[TN, FP],
#  [FN, TP]]

# Possiamo utilizzare .ravel() per trasformare la matrice
# bidimensionale in un array monodimensionale.

# ESEMPIO:
# tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# In questo modo assegniamo direttamente
# i quattro valori a quattro variabili differenti.

# ATTENZIONE:
# Questo ordine vale quando le classi sono ordinate come [0, 1].
# Se utilizziamo etichette differenti, dobbiamo controllare
# l'ordine delle classi nella matrice.


# ==========================================================
# 3. METRICHE DERIVATE DALLA MATRICE DI CONFUSIONE
# ==========================================================

# Dalla matrice di confusione possiamo calcolare
# diverse metriche per valutare il classificatore.

# Le principali sono:
# 1. Accuracy.
# 2. Precision.
# 3. Recall.
# 4. F1-score.


# ==========================================================
# 4. ACCURACY (ACCURATEZZA)
# ==========================================================

# L'accuracy misura la proporzione di previsioni corrette
# rispetto al numero totale delle osservazioni.

# FORMULA:
# Accuracy = (TP + TN) / (TP + TN + FP + FN)

# TP e TN rappresentano le previsioni corrette.
# FP e FN rappresentano le previsioni sbagliate.

# ESEMPIO:
# TP = 40
# TN = 50
# FP = 5
# FN = 5

# Accuracy = (40 + 50) / 100 = 0.90

# Il modello ha classificato correttamente il 90% dei casi.

# ATTENZIONE:
# L'accuracy può essere poco rappresentativa
# quando le classi sono molto sbilanciate.

# ESEMPIO:
# Abbiamo 100 osservazioni:
# 95 negative e 5 positive.

# Se il modello prevede sempre negativo,
# ottiene comunque un'accuracy del 95%.
# Tuttavia non riconosce nessun caso positivo.


# ==========================================================
# 5. PRECISION
# ==========================================================

# La precision misura quanti dei casi previsti come positivi
# sono realmente positivi.

# Risponde alla domanda:
# "Quando il modello dice positivo, quanto spesso ha ragione?"

# FORMULA:
# Precision = TP / (TP + FP)

# ESEMPIO:
# TP = 40
# FP = 10

# Precision = 40 / (40 + 10) = 0.80

# Significa che l'80% dei casi classificati come positivi
# appartiene realmente alla classe positiva.

# La precision è importante quando vogliamo ridurre
# il numero di falsi positivi (FP).

# ESEMPIO - FILTRO SPAM:
# Vogliamo evitare che email importanti
# vengano erroneamente classificate come spam.

# ESEMPIO - CAMPAGNE COMMERCIALI:
# Se contattare un cliente è costoso,
# vogliamo che i clienti individuati come interessati
# siano effettivamente interessati.


# ==========================================================
# 6. RECALL (SENSIBILITÀ)
# ==========================================================

# Il recall misura quanti dei casi realmente positivi
# vengono individuati correttamente dal modello.

# Risponde alla domanda:
# "Tra tutti i positivi reali, quanti ne riconosciamo?"

# FORMULA:
# Recall = TP / (TP + FN)

# ESEMPIO:
# TP = 40
# FN = 10

# Recall = 40 / (40 + 10) = 0.80

# Significa che il modello riconosce correttamente
# l'80% dei casi realmente positivi.

# Il recall è importante quando vogliamo ridurre
# il numero di falsi negativi (FN).

# ESEMPIO - DIAGNOSI MEDICA:
# Vogliamo individuare il maggior numero possibile
# di persone realmente malate.

# ESEMPIO - RILEVAMENTO FRODI:
# Vogliamo riconoscere il maggior numero possibile
# di operazioni fraudolente.

# ATTENZIONE:
# Aumentare il recall può comportare
# un aumento dei falsi positivi.


# ==========================================================
# 7. F1-SCORE
# ==========================================================

# L'F1-score combina precision e recall
# attraverso la loro media armonica.

# FORMULA:
# F1 = 2 * (Precision * Recall) / (Precision + Recall)

# Il risultato varia generalmente da 0 a 1.

# F1 = 1:
# Precision e recall sono entrambi perfetti.

# F1 = 0:
# Almeno una delle due metriche è pari a zero.

# La media armonica penalizza gli squilibri
# tra precision e recall.

# ATTENZIONE:
# La media armonica non utilizza i logaritmi.
# Il logaritmo compare invece nella formula dell'entropia.

# ESEMPIO:
# Precision = 0.90
# Recall = 0.50

# F1 = 2 * (0.90 * 0.50) / (0.90 + 0.50)
# F1 = circa 0.64

# Nonostante la precision sia elevata,
# l'F1-score diminuisce perché il recall è basso.

# L'F1-score è utile quando vogliamo considerare
# sia i falsi positivi sia i falsi negativi.

# È spesso utilizzato anche con dataset sbilanciati,
# ma dobbiamo sempre valutare il contesto del problema.


# ==========================================================
# 8. QUANDO UTILIZZARE LE DIVERSE METRICHE?
# ==========================================================

# ACCURACY:
# Utile quando vogliamo conoscere la percentuale
# complessiva di previsioni corrette.
# È particolarmente interpretabile con classi bilanciate
# e costi degli errori simili.

# PRECISION:
# Da privilegiare quando i falsi positivi sono costosi.
# Esempi: filtro spam, campagne commerciali.

# RECALL:
# Da privilegiare quando i falsi negativi sono gravi.
# Esempi: diagnosi mediche, rilevamento frodi.

# F1-SCORE:
# Da utilizzare quando vogliamo bilanciare
# precision e recall.
# È utile anche in presenza di classi sbilanciate.

# IMPORTANTE:
# Non esiste una metrica migliore in assoluto.
# La scelta dipende dall'obiettivo del problema
# e dalla gravità dei diversi tipi di errore.


# ==========================================================
# 9. CLASSIFICAZIONE MULTICLASSE
# ==========================================================

# Nei problemi multiclasse abbiamo più di due classi.

# ESEMPIO:
# Nel dataset load_wine abbiamo tre classi:
# 0, 1 e 2.

# La matrice di confusione non sarà più 2x2,
# ma avrà una riga e una colonna per ogni classe.

# ESEMPIO CON TRE CLASSI:

#                  PREDIZIONE
#                  0    1    2
# REALE       0   15    2    1
#             1    1   18    2
#             2    0    3   17

# I valori sulla diagonale principale
# rappresentano le previsioni corrette.

# I valori fuori dalla diagonale
# rappresentano gli errori di classificazione.

# Possiamo calcolare precision, recall e F1-score
# separatamente per ogni classe.

# Per calcolare queste metriche, ogni classe viene
# considerata positiva rispetto a tutte le altre.


# ==========================================================
# 10. SUPPORT
# ==========================================================

# Il support indica il numero di osservazioni reali
# appartenenti a una determinata classe.

# ESEMPIO:
# Classe 0 = 20 osservazioni.
# Classe 1 = 30 osservazioni.
# Classe 2 = 10 osservazioni.

# Il support sarà:
# Classe 0 = 20
# Classe 1 = 30
# Classe 2 = 10

# Il support non misura la qualità delle previsioni.
# Indica soltanto quante osservazioni reali
# appartengono a ciascuna classe nel dataset valutato.


# ==========================================================
# 11. MACRO AVG
# ==========================================================

# Macro avg significa media semplice tra le metriche
# calcolate per ciascuna classe.

# Ogni classe ha la stessa importanza,
# indipendentemente dal numero di osservazioni.

# ESEMPIO:
# Precision classe 0 = 0.90
# Precision classe 1 = 0.80
# Precision classe 2 = 0.40

# Macro avg = (0.90 + 0.80 + 0.40) / 3
# Macro avg = 0.70

# È utile quando vogliamo dare la stessa importanza
# a tutte le classi, anche a quelle meno frequenti.


# ==========================================================
# 12. WEIGHTED AVG
# ==========================================================

# Weighted avg significa media pesata delle metriche.

# Ogni classe contribuisce alla media in base
# al proprio support, cioè al numero di osservazioni.

# Le classi più numerose hanno un peso maggiore.

# ESEMPIO:
# Classe 0: precision = 0.90, support = 50
# Classe 1: precision = 0.80, support = 30
# Classe 2: precision = 0.40, support = 20

# Weighted avg = (0.90*50 + 0.80*30 + 0.40*20) / 100
# Weighted avg = 0.77

# DIFFERENZA PRINCIPALE:

# MACRO AVG:
# Tutte le classi hanno lo stesso peso.

# WEIGHTED AVG:
# Le classi hanno un peso proporzionale
# al numero di osservazioni reali.

# ATTENZIONE:
# La weighted avg può nascondere prestazioni basse
# sulle classi meno rappresentate.


# ==========================================================
# 13. STRUMENTI SCIKIT-LEARN
# ==========================================================

# confusion_matrix():
# Restituisce la matrice di confusione.
# Permette di osservare le previsioni corrette
# e gli errori del classificatore.

# ConfusionMatrixDisplay:
# Permette di rappresentare graficamente
# la matrice di confusione.

# classification_report():
# Restituisce un riepilogo delle principali metriche:
# precision, recall, F1-score e support.
# Nei problemi multiclasse mostra anche le medie
# macro avg e weighted avg.


# ==========================================================
# 14. ESEMPIO PRATICO - MATRICE DI CONFUSIONE
# ==========================================================

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

import matplotlib.pyplot as plt

# Carichiamo il dataset
dataset = load_breast_cancer()

# Separiamo le caratteristiche dalle etichette
X = dataset.data
y = dataset.target

# Dividiamo i dati in training e test
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,
    random_state=42
)

# Creiamo il modello KNN con 5 vicini
modello = KNeighborsClassifier(n_neighbors=5)

# Addestriamo il modello
modello.fit(X_train, y_train)

# Effettuiamo le previsioni
y_pred = modello.predict(X_test)

# Calcoliamo la matrice di confusione
matrice = confusion_matrix(y_test, y_pred)

# Stampiamo la matrice
print("\nMATRICE DI CONFUSIONE")
print(matrice)

# Estraiamo i quattro valori della matrice
tn, fp, fn, tp = matrice.ravel()

# Stampiamo i risultati
print("\nTrue Negative:", tn)
print("False Positive:", fp)
print("False Negative:", fn)
print("True Positive:", tp)

# Calcoliamo l'accuracy
accuracy = accuracy_score(y_test, y_pred)

# Calcoliamo la precision
precision = precision_score(y_test, y_pred)

# Calcoliamo il recall
recall = recall_score(y_test, y_pred)

# Calcoliamo l'F1-score
f1 = f1_score(y_test, y_pred)

# Stampiamo le metriche
print("\nMETRICHE DI CLASSIFICAZIONE")
print("Accuracy:", round(accuracy, 4))
print("Precision:", round(precision, 4))
print("Recall:", round(recall, 4))
print("F1-score:", round(f1, 4))

# Stampiamo il classification report
print("\nCLASSIFICATION REPORT")
print(classification_report(y_test, y_pred))

# Visualizziamo graficamente la matrice
ConfusionMatrixDisplay.from_predictions(y_test, y_pred)

# Mostriamo il grafico
plt.show()


# ==========================================================
# 15. ATTENZIONE ALLE CLASSI DEL DATASET
# ==========================================================

# Nel dataset load_breast_cancer di Scikit-learn:
# Classe 0 = malignant (maligno).
# Classe 1 = benign (benigno).

# Per impostazione predefinita, le metriche binarie
# precision_score(), recall_score() e f1_score()
# considerano positiva la classe 1.

# Quindi nell'esempio precedente la classe positiva
# è quella dei tumori benigni.

# Se vogliamo considerare positiva la classe dei tumori maligni,
# dobbiamo specificare pos_label=0.

# ESEMPIO:
# recall_score(y_test, y_pred, pos_label=0)

# È importante scegliere correttamente la classe positiva
# prima di interpretare FP, FN, precision e recall.


# ==========================================================
# 16. RIEPILOGO FINALE
# ==========================================================

# MATRICE DI CONFUSIONE:
# Confronta le classi reali con quelle previste.

# TN:
# Negativo previsto correttamente.

# FP:
# Negativo classificato erroneamente come positivo.

# FN:
# Positivo classificato erroneamente come negativo.

# TP:
# Positivo previsto correttamente.

# ACCURACY:
# Percentuale complessiva di previsioni corrette.

# PRECISION:
# Tra i positivi previsti, quanti sono realmente positivi?

# RECALL:
# Tra i positivi reali, quanti vengono riconosciuti?

# F1-SCORE:
# Media armonica tra precision e recall.

# SUPPORT:
# Numero di osservazioni reali di ogni classe.

# MACRO AVG:
# Media semplice delle metriche delle classi.

# WEIGHTED AVG:
# Media pesata in base al support delle classi.

# CONCLUSIONE:
# L'accuracy da sola non basta sempre per valutare un modello.
# Dobbiamo analizzare anche gli errori e scegliere
# le metriche più adatte al problema che stiamo studiando.
