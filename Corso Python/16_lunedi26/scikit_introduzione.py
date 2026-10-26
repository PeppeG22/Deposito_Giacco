# SCIKIT-LEARN E LIBRERIE DI MACHINE LEARNING

# Scikit-learn: libreria Python utilizzata per il Machine Learning.
# PyTorch: libreria sviluppata originariamente da Meta, usata anche per il Deep Learning.
# TensorFlow: libreria sviluppata da Google per il Machine Learning e Deep Learning.
# Keras: libreria che semplifica la creazione di reti neurali.


# --------------------------------------------------
# 1. MODULI PRINCIPALI DI SCIKIT-LEARN
# --------------------------------------------------

# sklearn.datasets: contiene dataset di esempio e funzioni per generarli.
# sklearn.model_selection: permette di dividere i dati e fare la validazione incrociata.
# sklearn.metrics: contiene le misure per valutare le prestazioni dei modelli.
# sklearn.neighbors: contiene algoritmi come K-Nearest Neighbors (KNN).


# --------------------------------------------------
# 2. FUNZIONI PER OTTENERE I DATASET
# --------------------------------------------------

# Scikit-learn offre 3 principali famiglie di funzioni:

# load_: carica dataset già inclusi nella libreria.
# fetch_: scarica dataset generalmente più grandi da Internet.
# make_: genera dataset sintetici, cioè dati artificiali.

# ESEMPI DI DATASET INCLUSI:

# load_iris(): contiene 3 specie di fiori con le loro caratteristiche.
# load_digits(): contiene immagini di cifre scritte a mano da 0 a 9.
# load_wine(): contiene 3 classi di vino con relative analisi chimiche.
# load_breast_cancer(): contiene dati utilizzati per la classificazione di tumori.
# load_diabetes(): contiene dati utilizzati per un problema di regressione.


# --------------------------------------------------
# 3. STRUTTURA DEI DATASET
# --------------------------------------------------

# Le funzioni load_ restituiscono generalmente un oggetto Bunch,
# simile a un dizionario, che contiene diverse informazioni.

# .data: contiene le feature (X), organizzate in una matrice.
# .target: contiene il target (y), generalmente un vettore.
# .feature_names: contiene i nomi delle feature, se disponibili.
# .target_names: contiene i nomi delle classi, se disponibili.
# .DESCR: contiene la descrizione del dataset.

# ESEMPIO:
# dataset = load_iris()
# X = dataset.data
# y = dataset.target


# --------------------------------------------------
# 4. DATASET SINTETICI E NOISE
# --------------------------------------------------

# I dataset sintetici sono dati artificiali generati attraverso funzioni.

# make_classification(): genera dati per problemi di classificazione.
# make_regression(): genera dati per problemi di regressione.

# NOISE (RUMORE):
# È una componente casuale che introduce variabilità nei dati.
# Può rendere più difficile individuare le relazioni tra le variabili.

# RANDOM_STATE:
# Controlla la casualità nella generazione dei dati.
# Utilizzando lo stesso valore e gli stessi parametri,
# otteniamo sempre gli stessi dati.

# CLASS_SEP:
# Parametro di make_classification() che controlla la separazione
# tra le classi. Più è alto, più le classi tendono a essere distanti.