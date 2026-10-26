# MACHINE LEARNING (ML)

# Per il Machine Learning utilizziamo la libreria scikit-learn.
# Il Machine Learning permette al computer di imparare dai dati,
# individuando regolarità senza dover programmare esplicitamente ogni regola.

# Nel Machine Learning supervisionato il funzionamento è:
# DATI + RISPOSTE = REGOLE
# Forniamo al computer molti esempi già risolti e, attraverso
# l'addestramento, il modello impara a riconoscere le relazioni nei dati.

# OBIETTIVO:
# Automatizzare decisioni o effettuare previsioni su nuovi dati.

# ESEMPI DI UTILIZZO:
# - Filtro antispam: riconoscere le email indesiderate.
# - Prezzi immobiliari: prevedere il prezzo di una casa.
# - Rilevamento frodi: identificare operazioni sospette.
# - Raccomandazioni: suggerire contenuti sui social.

# QUANDO NON UTILIZZARE IL MACHINE LEARNING:
# Se una regola è già conosciuta, precisa e stabile, non serve ML.
# Esempi:
# - Calcolare l'IVA applicando una percentuale.
# - Convertire valori da un'unità di misura a un'altra.
# - Calcolare la somma di due numeri.


# --------------------------------------------------
# 1. TERMINOLOGIA DEL MACHINE LEARNING
# --------------------------------------------------

# ALGORITMO DI APPRENDIMENTO:
# È la procedura che cerca di individuare le regole e le relazioni nei dati.

# MODELLO:
# È il risultato dell'apprendimento.
# Una volta addestrato, può effettuare previsioni su nuovi dati.

# PARAMETRI (PESI):
# Sono i valori numerici interni al modello che vengono regolati
# durante l'addestramento per migliorare le previsioni.

# ADDESTRAMENTO (TRAINING):
# È il processo attraverso il quale l'algoritmo apprende dai dati
# e regola i parametri del modello per ridurre gli errori.

# INFERENZA / PREDIZIONE:
# È l'utilizzo di un modello già addestrato per effettuare
# previsioni su dati nuovi.

# PATTERN:
# Sono regolarità o schemi ricorrenti presenti nei dati.
# Il Machine Learning cerca pattern, non certezze assolute.


# --------------------------------------------------
# 2. METODI PRINCIPALI DI SCIKIT-LEARN
# --------------------------------------------------

# fit():
# Serve per addestrare il modello sui dati disponibili.
# Nel caso supervisionato riceve le feature (X) e il target (y).
# Esempio: modello.fit(X, y)

# predict():
# Serve per effettuare previsioni utilizzando un modello
# precedentemente addestrato.
# Esempio: modello.predict(X_nuovi)

# DIFFERENZA:
# fit() = il modello impara dai dati.
# predict() = il modello utilizza ciò che ha imparato.

# reshape(-1, 1):
# È un metodo di NumPy che modifica la forma di un array.
# Trasforma un vettore monodimensionale in una matrice
# con una colonna e tante righe quanti sono gli elementi.

# Esempio:
# [10, 20, 30] diventa:
# [[10],
#  [20],
#  [30]]

# Il valore -1 permette a NumPy di calcolare automaticamente
# il numero di righe, mentre 1 indica il numero di colonne.

# È utile perché scikit-learn richiede generalmente
# le feature X organizzate in una matrice bidimensionale.


# --------------------------------------------------
# 3. DATI E DATASET
# --------------------------------------------------

# DATASET:
# È l'insieme dei dati utilizzati per l'apprendimento.
# Possiamo rappresentarlo come una tabella di righe e colonne.

# CAMPIONE (SAMPLE):
# È una singola osservazione, rappresentata da una riga del dataset.
# Esempio: una casa con superficie, numero di stanze e prezzo.

# CAMPIONAMENTO (SAMPLING):
# È il processo di selezione di un insieme di campioni
# da una popolazione o da un insieme di dati.

# FEATURE:
# È una caratteristica che descrive un campione.
# Generalmente corrisponde a una colonna del dataset.
# Può essere chiamata anche attributo o variabile indipendente.
# Esempio: superficie di una casa, numero di stanze.

# TARGET:
# È la variabile che vogliamo prevedere.
# Viene chiamata anche etichetta (LABEL) o variabile dipendente.
# Esempio: il prezzo della casa.


# --------------------------------------------------
# 4. CONVENZIONE X E y
# --------------------------------------------------

# Per convenzione utilizziamo:

# X MAIUSCOLA:
# Contiene tutte le feature utilizzate dal modello.
# È una matrice con n_campioni righe e n_feature colonne.

# y MINUSCOLA:
# Contiene i valori del target che vogliamo prevedere.
# Generalmente è un vettore con n_campioni elementi.

# ESEMPIO:
# X = [[80, 3], [100, 4], [120, 5]]
# y = [150000, 200000, 250000]

# In questo esempio:
# X contiene superficie e numero di stanze di 3 case.
# y contiene i rispettivi prezzi delle case.

# DATI ETICHETTATI:
# Sono dati per i quali conosciamo già la risposta corretta.
# Abbiamo quindi sia X che y.

# DATI NON ETICHETTATI:
# Sono dati per i quali non abbiamo un target associato.
# Abbiamo solamente X.


# --------------------------------------------------
# 5. TIPI DI APPRENDIMENTO
# --------------------------------------------------

# Esistono 3 principali tipi di apprendimento:


# 1. APPRENDIMENTO SUPERVISIONATO

# Utilizza dati etichettati (X e y).
# Il modello impara la relazione tra le feature e il target.

# Si divide principalmente in:

# CLASSIFICAZIONE:
# Il target y rappresenta una categoria.
# Può essere binaria (2 categorie) o multiclasse (più categorie).
# Esempio: email SPAM oppure NON SPAM.

# REGRESSIONE:
# Il target y rappresenta un valore numerico continuo.
# Esempio: prevedere il prezzo di una casa.


# 2. APPRENDIMENTO NON SUPERVISIONATO

# Utilizza dati senza un target noto (solo X).
# Il modello cerca strutture, somiglianze o pattern nei dati.

# Si divide principalmente in:

# CLUSTERING:
# Raggruppa i campioni in gruppi con caratteristiche simili.
# Esempio: dividere i clienti in gruppi in base agli acquisti.

# RIDUZIONE DELLA DIMENSIONALITÀ:
# Riduce il numero di feature, cercando di conservare
# le informazioni più importanti del dataset.
# Esempio: riassumere 20 caratteristiche in 2 o 3 nuove variabili.


# 3. APPRENDIMENTO PER RINFORZO

# Un agente compie azioni all'interno di un ambiente
# e riceve ricompense o penalità in base ai risultati.

# Attraverso l'esperienza, impara a scegliere le azioni
# che permettono di ottenere le ricompense migliori.

# Esempi:
# - Videogiochi.
# - Robotica.
# - Sistemi di controllo automatico.


# --------------------------------------------------
# 6. COME SCEGLIERE IL TIPO DI APPRENDIMENTO?
# --------------------------------------------------

# La scelta dipende dall'obiettivo e dai dati disponibili.

# Se vogliamo prevedere una categoria:
# -> APPRENDIMENTO SUPERVISIONATO - CLASSIFICAZIONE.

# Se vogliamo prevedere un valore numerico continuo:
# -> APPRENDIMENTO SUPERVISIONATO - REGRESSIONE.

# Se vogliamo individuare gruppi simili senza target:
# -> APPRENDIMENTO NON SUPERVISIONATO - CLUSTERING.

# Se vogliamo ridurre il numero di caratteristiche:
# -> APPRENDIMENTO NON SUPERVISIONATO - RIDUZIONE DIMENSIONALITÀ.

# Se vogliamo che un agente impari attraverso azioni e ricompense:
# -> APPRENDIMENTO PER RINFORZO.

# IMPORTANTE:
# Non basta osservare il dataset per scegliere il tipo di ML.
# Bisogna considerare cosa vogliamo ottenere e se disponiamo
# delle risposte corrette (target) per addestrare il modello.