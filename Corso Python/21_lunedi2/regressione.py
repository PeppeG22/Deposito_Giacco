
# ==========================================================
# LEZIONE 2 NOVEMBRE - REGRESSIONE LINEARE
# ==========================================================

# La regressione lineare è un algoritmo di Machine Learning supervisionato.
# Viene utilizzata per prevedere un valore numerico continuo.

# ESEMPI:
# Prevedere il prezzo di una casa.
# Prevedere il consumo di energia.
# Prevedere il punteggio di uno studente.
# Prevedere il fatturato di un'attività.

# Il modello cerca di individuare una relazione tra
# una o più caratteristiche (X) e il valore da prevedere (y).

# La regressione lineare rappresenta questa relazione
# attraverso una retta oppure, con più feature, un piano o iperpiano.


# ==========================================================
# 1. REGRESSIONE LINEARE SEMPLICE
# ==========================================================

# La regressione lineare semplice utilizza una sola feature
# per prevedere un valore numerico.

# FORMULA:
# y_pred = w * x + b

# x = caratteristica utilizzata per effettuare la previsione.
# w = coefficiente o peso associato alla caratteristica.
# b = intercetta della retta.
# y_pred = valore previsto dal modello.

# COEFFICIENTE (w):
# Indica di quanto cambia il valore previsto di y
# quando x aumenta di un'unità.

# ESEMPIO:
# Se w = 2, aumentando x di 1,
# il valore previsto di y aumenta di 2.

# Se w è negativo, all'aumentare di x
# il valore previsto di y diminuisce.

# INTERCETTA (b):
# Rappresenta il valore previsto di y quando x = 0.

# ESEMPIO:
# y_pred = 2 * x + 5

# Se x = 0, y_pred = 5.
# Se x = 3, y_pred = 11.


# ==========================================================
# 2. REGRESSIONE LINEARE MULTIPLA
# ==========================================================

# La regressione lineare multipla utilizza più caratteristiche
# per prevedere un unico valore numerico.

# FORMULA:
# y_pred = w1*x1 + w2*x2 + ... + wn*xn + b

# x1, x2, ..., xn = caratteristiche del dataset.
# w1, w2, ..., wn = coefficienti associati alle caratteristiche.
# b = intercetta.
# y_pred = previsione finale.

# Ogni caratteristica ha un proprio coefficiente.

# ESEMPIO:
# Vogliamo prevedere il prezzo di una casa.

# x1 = superficie della casa.
# x2 = numero di stanze.
# x3 = età dell'immobile.

# Il modello assegna un coefficiente a ogni caratteristica
# per determinare quanto contribuisce alla previsione.

# ATTENZIONE:
# Il coefficiente indica l'effetto di una caratteristica
# sulla previsione, mantenendo costanti le altre caratteristiche.


# ==========================================================
# 3. COME IMPARA IL MODELLO - MINIMI QUADRATI
# ==========================================================

# Durante l'addestramento, la regressione lineare cerca
# i coefficienti e l'intercetta più adatti ai dati.

# L'obiettivo è ridurre la differenza tra
# i valori reali e quelli previsti.

# RESIDUO:
# È la differenza tra il valore reale e quello previsto.

# FORMULA:
# Residuo = y_reale - y_pred

# ESEMPIO:
# Valore reale = 100.
# Valore previsto = 90.
# Residuo = 100 - 90 = 10.

# METODO DEI MINIMI QUADRATI:
# Il modello cerca di minimizzare la somma
# dei quadrati dei residui.

# FORMULA:
# Somma dei quadrati = somma di (y_reale - y_pred)**2

# Perché utilizziamo il quadrato?

# 1. Evitiamo che errori positivi e negativi si annullino.
# 2. Penalizziamo maggiormente gli errori più grandi.
# 3. Possiamo individuare i coefficienti che minimizzano l'errore.

# Il modello cerca quindi la retta che meglio si adatta
# ai dati secondo il criterio dei minimi quadrati.


# ==========================================================
# 4. PARAMETRI DEL MODELLO
# ==========================================================

# Nella regressione lineare, i coefficienti e l'intercetta
# sono parametri appresi durante l'addestramento.

# Dopo aver utilizzato fit(), possiamo consultarli
# attraverso due attributi di Scikit-learn.

# coef_:
# Contiene i coefficienti associati alle caratteristiche.

# intercept_:
# Contiene l'intercetta del modello.

# ATTENZIONE:
# I parametri vengono appresi dal modello durante il fit.
# Gli iperparametri, invece, vengono impostati prima del fit.


# ==========================================================
# 5. LINEARREGRESSION IN SCIKIT-LEARN
# ==========================================================

from sklearn.linear_model import LinearRegression

# Creiamo un piccolo dataset con una sola caratteristica
X = [[1], [2], [3], [4], [5]]
y = [3, 5, 7, 9, 11]

# Creiamo il modello di regressione lineare
modello = LinearRegression()

# Addestriamo il modello
modello.fit(X, y)

# Stampiamo il coefficiente
print("Coefficiente:", modello.coef_)

# Stampiamo l'intercetta
print("Intercetta:", modello.intercept_)

# Prevediamo il valore corrispondente a x = 6
previsione = modello.predict([[6]])

# Stampiamo la previsione
print("Previsione:", previsione[0])


# ==========================================================
# 6. SPIEGAZIONE DEL CODICE
# ==========================================================

# LinearRegression():
# Crea un modello di regressione lineare.

# fit(X, y):
# Addestra il modello sui dati.
# Durante l'addestramento vengono appresi
# i coefficienti e l'intercetta.

# coef_:
# Restituisce i coefficienti appresi.
# Con una sola feature abbiamo un solo coefficiente.

# intercept_:
# Restituisce il valore dell'intercetta.

# predict():
# Permette di prevedere nuovi valori numerici.

# Nel nostro esempio:
# Coefficiente = 2.
# Intercetta = 1.

# La relazione appresa è:
# y_pred = 2*x + 1

# Per x = 6:
# y_pred = 2*6 + 1 = 13.


# ==========================================================
# 7. DIFFERENZA TRA CLASSIFICAZIONE E REGRESSIONE
# ==========================================================

# CLASSIFICAZIONE:
# Prevede una classe o una categoria.
# Esempio: tumore benigno o maligno.

# REGRESSIONE:
# Prevede un valore numerico continuo.
# Esempio: prezzo di una casa o fatturato.

# KNeighborsClassifier:
# Algoritmo per problemi di classificazione.

# KNeighborsRegressor:
# Algoritmo per problemi di regressione.

# DecisionTreeClassifier:
# Albero decisionale per classificazione.

# DecisionTreeRegressor:
# Albero decisionale per regressione.

# LinearRegression:
# Modello per problemi di regressione.


# ==========================================================
# 8. RIEPILOGO FINALE
# ==========================================================

# REGRESSIONE LINEARE:
# Modello supervisionato che prevede valori numerici continui.

# REGRESSIONE SEMPLICE:
# Utilizza una sola caratteristica.

# REGRESSIONE MULTIPLA:
# Utilizza più caratteristiche.

# COEFFICIENTE (w):
# Indica come cambia la previsione al variare della feature.

# INTERCETTA (b):
# Valore previsto quando tutte le feature sono uguali a zero.

# RESIDUO:
# Differenza tra valore reale e valore previsto.

# MINIMI QUADRATI:
# Metodo che minimizza la somma dei quadrati dei residui.

# coef_:
# Coefficienti appresi dal modello.

# intercept_:
# Intercetta appresa dal modello.

# fit():
# Addestra il modello.

# predict():
# Effettua nuove previsioni.

# OBIETTIVO:
# Individuare una relazione lineare tra le caratteristiche
# e il valore da prevedere, riducendo gli errori di previsione.
