
# ==========================================================
# 1. MAKE_CLASSIFICATION
# ==========================================================

# make_classification crea un dataset sintetico per problemi di classificazione.
# La classificazione serve a prevedere una categoria (es. 0 oppure 1).
# Restituisce X (caratteristiche dei dati) e y (classi di appartenenza).

# PRINCIPALI PARAMETRI:

# n_samples = numero totale di osservazioni (righe del dataset).
# n_features = numero totale di caratteristiche (colonne di X).
# n_informative = numero di caratteristiche che contengono informazioni utili per distinguere le classi.
# n_redundant = numero di caratteristiche derivate da quelle informative.
# n_repeated = numero di caratteristiche duplicate.
# n_classes = numero di classi da distinguere (es. 2 per classificazione binaria).
# n_clusters_per_class = numero di gruppi di dati generati per ogni classe.
# weights = proporzione delle osservazioni appartenenti a ciascuna classe.
# flip_y = quantità di rumore introdotta nelle etichette delle classi.
# class_sep = distanza tra le classi; più è alto, più le classi sono separate.
# shuffle = mescola i dati generati (True oppure False).
# random_state = fissa la casualità per ottenere sempre gli stessi dati.

# NOTA: n_informative + n_redundant + n_repeated non deve superare n_features.

from sklearn.datasets import make_classification

X, y = make_classification(
    n_samples=100,
    n_features=4,
    n_informative=2,
    n_redundant=0,
    n_classes=2,
    random_state=42
)


# ==========================================================
# 2. MAKE_REGRESSION
# ==========================================================

# make_regression crea un dataset sintetico per problemi di regressione.
# La regressione serve a prevedere un valore numerico continuo.
# Esempio: prevedere il prezzo di una casa oppure il fatturato.
# Restituisce X (caratteristiche) e y (valori numerici da prevedere).

# PRINCIPALI PARAMETRI:

# n_samples = numero totale di osservazioni.
# n_features = numero totale di caratteristiche.
# n_informative = numero di caratteristiche realmente utili per prevedere y.
# n_targets = numero di valori da prevedere per ogni osservazione.
# noise = quantità di rumore aggiunta ai valori di y.
# bias = valore costante aggiunto al risultato della regressione.
# coef = se True, restituisce anche i coefficienti utilizzati per generare i dati.
# shuffle = mescola i dati.
# random_state = rende riproducibile la generazione del dataset.

from sklearn.datasets import make_regression

X, y = make_regression(
    n_samples=100,
    n_features=3,
    n_informative=2,
    noise=10,
    random_state=42
)


# ==========================================================
# 3. MAKE_BLOBS E MAKE_MOONS
# ==========================================================

# MAKE_BLOBS:
# Genera gruppi di punti distribuiti attorno a determinati centri.
# È utilizzato soprattutto per esercizi di clustering e classificazione.

# n_samples = numero di punti.
# n_features = numero di caratteristiche.
# centers = numero di gruppi da generare.
# cluster_std = dispersione dei punti attorno al centro.
# random_state = rende riproducibili i dati.

from sklearn.datasets import make_blobs

X, y = make_blobs(
    n_samples=100,
    centers=3,
    cluster_std=1.0,
    random_state=42
)


# MAKE_MOONS:
# Genera due gruppi di punti disposti a forma di mezzaluna.
# È utile per studiare problemi di classificazione non lineare.

# n_samples = numero totale di punti.
# noise = quantità di rumore che rende i punti meno ordinati.
# shuffle = mescola i dati.
# random_state = rende riproducibili i dati.

from sklearn.datasets import make_moons

X, y = make_moons(
    n_samples=100,
    noise=0.1,
    random_state=42
)


# ==========================================================
# 4. KNEIGHBORSCLASSIFIER (KNN)
# ==========================================================

# KNeighborsClassifier è un algoritmo di classificazione supervisionata.
# Classifica una nuova osservazione considerando le classi dei punti più vicini.
# KNN significa K-Nearest Neighbors (K vicini più prossimi).

# Esempio:
# Se scegliamo n_neighbors=3, il modello considera i 3 vicini più vicini.
# Se 2 appartengono alla classe 1 e 1 alla classe 0,
# la nuova osservazione viene classificata come classe 1.

# LE 5 FASI PRINCIPALI:

# 1. IMPORTAZIONE:
# Importiamo l'algoritmo dalla libreria sklearn.neighbors.

from sklearn.neighbors import KNeighborsClassifier

# 2. ISTANZA DEL MODELLO:
# Creiamo il modello e impostiamo gli iperparametri.
# n_neighbors=3 significa che consideriamo i 3 vicini più prossimi.

modello = KNeighborsClassifier(n_neighbors=3)

# 3. ADDESTRAMENTO:
# Il metodo fit() prepara il modello utilizzando i dati di addestramento.
# Nel KNN vengono principalmente memorizzati i dati e le rispettive classi.

# modello.fit(X_train, y_train)

# 4. PREDIZIONE:
# predict() permette di prevedere la classe di nuove osservazioni.

# y_pred = modello.predict(X_test)

# 5. VALUTAZIONE:
# Verifichiamo quanto il modello è accurato confrontando le previsioni
# con i valori reali attraverso accuracy_score() oppure modello.score().


# ==========================================================
# 5. DIFFERENZA TRA PARAMETRI E IPERPARAMETRI
# ==========================================================

# IPERPARAMETRI:
# Sono valori che impostiamo prima dell'addestramento del modello.
# Servono a controllare il comportamento dell'algoritmo.
# Esempio: n_neighbors=3 nel KNN.

# PARAMETRI:
# Sono valori che il modello apprende dai dati durante l'addestramento.
# Esempio: coefficienti di una regressione lineare.

# DIFFERENZA PRINCIPALE:
# Iperparametri = impostati prima dell'addestramento.
# Parametri = appresi dal modello durante l'addestramento.

# NOTA: il KNN è un caso particolare perché memorizza i dati di training
# anziché apprendere coefficienti come avviene nella regressione lineare.


# ==========================================================
# 6. TRAIN_TEST_SPLIT
# ==========================================================

# train_test_split divide il dataset in due parti:
# TRAINING SET = dati utilizzati per addestrare il modello.
# TEST SET = dati tenuti separati per valutare il modello dopo l'addestramento.

# È importante testare il modello su dati mai utilizzati per addestrarlo.

# La funzione restituisce 4 oggetti, in questo ordine:
# X_train = caratteristiche utilizzate per l'addestramento.
# X_test = caratteristiche utilizzate per il test.
# y_train = valori reali associati ai dati di addestramento.
# y_test = valori reali associati ai dati di test.

# PRINCIPALI PARAMETRI:

# test_size = percentuale di dati destinata al test.
# Esempio: test_size=0.2 significa 20% test e 80% training.
# train_size = percentuale di dati destinata al training.
# shuffle=True = mescola i dati prima della divisione (valore predefinito).
# random_state = rende riproducibile la suddivisione.

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    shuffle=True,
    random_state=42
)


# ==========================================================
# 7. ACCURACY (ACCURATEZZA)
# ==========================================================

# L'accuracy misura la percentuale di previsioni corrette del modello.
# Il risultato varia da 0 a 1.

# 0.0 = 0% di previsioni corrette.
# 0.5 = 50% di previsioni corrette.
# 0.8 = 80% di previsioni corrette.
# 1.0 = 100% di previsioni corrette.

# Possiamo calcolare l'accuracy in due modi:

# METODO 1: accuracy_score()
# Confronta direttamente i valori reali con quelli previsti.

from sklearn.metrics import accuracy_score

# accuracy = accuracy_score(y_test, y_pred)

# METODO 2: modello.score()
# Calcola direttamente l'accuratezza del classificatore sui dati di test.

# accuracy = modello.score(X_test, y_test)

# Nel KNeighborsClassifier i due metodi restituiscono lo stesso risultato
# se utilizzano le stesse osservazioni.

# NOTA: l'accuracy è una metrica di classificazione.
# Nei modelli di regressione, score() restituisce normalmente R².


# ==========================================================
# OVERFITTING E UNDERFITTING NEL KNN
# ==========================================================

# OVERFITTING (K PICCOLO):
# Quando K è piccolo, il modello considera pochi vicini.
# Diventa molto sensibile al rumore e ai singoli dati di addestramento.
# Rischia di adattarsi troppo ai dati di training e funzionare male su dati nuovi.
# Questo comportamento è associato ad alta varianza.

# UNDERFITTING (K GRANDE):
# Quando K è grande, il modello considera molti vicini.
# Le differenze tra le classi tendono ad appiattirsi.
# Il modello diventa troppo semplice e rischia di non riconoscere le caratteristiche dei dati.
# Questo comportamento è associato ad alto bias (distorsione).

# SCELTA DI K:
# Il valore predefinito di n_neighbors è 5.
# Spesso si scelgono valori dispari di K per ridurre il rischio di pareggi.
# Questa scelta è particolarmente utile nella classificazione binaria.
# Il valore ottimale di K dipende dal dataset e può essere scelto tramite validazione.


# ==========================================================
# ALTRI PARAMETRI E METODI DEL KNN
# ==========================================================

# weights="uniform":
# Tutti i vicini hanno lo stesso peso, quindi ogni vicino vale un voto.
# È il valore predefinito.

# weights="distance":
# I vicini più vicini hanno un peso maggiore rispetto a quelli lontani.
# La loro influenza diminuisce all'aumentare della distanza.

# METODO .kneighbors():
# Restituisce le distanze e gli indici dei K vicini più prossimi.
# Permette di individuare quali osservazioni sono più vicine a un nuovo dato.

# Esempio:
# distanze, indici = modello.kneighbors([[4, 25]])

# distanze = distanze dei vicini rispetto al nuovo dato.
# indici = posizioni dei vicini nel dataset utilizzato dal modello.
