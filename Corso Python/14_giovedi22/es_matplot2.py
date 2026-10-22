import numpy as np  # importiamo numpy per generare i dati
import pandas as pd  # importiamo pandas per analizzare i dati
import matplotlib.pyplot as plt  # importiamo pyplot per creare i grafici

# 1. GENERAZIONE DEI DATI

visitatori = np.random.normal(2000, 500, size=365)  # generiamo 365 valori da una distribuzione normale con media 2000 e deviazione standard 500

visitatori = visitatori.round().astype(int)  # arrotondiamo e convertiamo i valori in numeri interi

visitatori[visitatori < 0] = 0  # sostituiamo eventuali valori negativi con zero

date = pd.date_range(start="2026-01-01", periods=365)  # generiamo 365 date consecutive dal primo gennaio

# 2. CREAZIONE DEL DATAFRAME

dati = {"Visitatori": visitatori}  # creiamo il dizionario con il numero di visitatori

df = pd.DataFrame(dati, index=date)  # creiamo il DataFrame utilizzando le date come indice

# 3. ANALISI DEI DATI

media_mensile = df.groupby(df.index.month)["Visitatori"].mean()  # raggruppiamo per numero del mese e calcoliamo la media

deviazione_mensile = df.groupby(df.index.month)["Visitatori"].std()  # calcoliamo la deviazione standard per ogni mese

print("Media mensile dei visitatori:")  # stampiamo il titolo
print(media_mensile)  # stampiamo le medie mensili

print("Deviazione standard per mese:")  # stampiamo il titolo
print(deviazione_mensile)  # stampiamo le deviazioni standard mensili

media_mobile = df["Visitatori"].rolling(window=7).mean()  # per ogni giorno calcoliamo la media di quel giorno e dei 6 precedenti

# 4. GRAFICO DEI VISITATORI GIORNALIERI E DELLA MEDIA MOBILE

plt.figure()  # creiamo la prima figura

plt.plot(df.index, df["Visitatori"], label="Visitatori giornalieri")  # disegniamo i visitatori giornalieri

plt.plot(df.index, media_mobile, label="Media mobile a 7 giorni")  # aggiungiamo la media mobile allo stesso grafico

plt.title("Visitatori giornalieri del parco")  # aggiungiamo il titolo
plt.xlabel("Data")  # indichiamo cosa rappresenta l'asse x
plt.ylabel("Numero di visitatori")  # indichiamo cosa rappresenta l'asse y
plt.legend()  # mostriamo le etichette delle due linee

plt.show()  # mostriamo il primo grafico

# 5. GRAFICO DELLA MEDIA MENSILE

plt.figure()  # creiamo la seconda figura

plt.bar(media_mensile.index, media_mensile)  # creiamo una barra per la media di ogni mese

plt.title("Media mensile dei visitatori")  # aggiungiamo il titolo
plt.xlabel("Mese")  # indichiamo cosa rappresenta l'asse x
plt.ylabel("Numero medio di visitatori")  # indichiamo cosa rappresenta l'asse y
plt.xticks(range(1, 13))  # mostriamo tutti i numeri dei mesi da 1 a 12

plt.show()  # mostriamo il secondo grafico