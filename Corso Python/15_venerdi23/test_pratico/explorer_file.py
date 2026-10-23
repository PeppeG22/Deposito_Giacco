import pandas as pd  # importiamo Pandas per la gestione dei dati
import numpy as np  # importiamo NumPy per le operazioni numeriche
import matplotlib.pyplot as plt  # importiamo Matplotlib per i grafici


# CARICAMENTO DEI DATASET

df_dati = pd.read_csv("Corso Python/15_venerdi23/test_pratico/candy-data.csv")  # carichiamo il primo CSV

df_vendite = pd.read_csv("Corso Python/15_venerdi23/test_pratico/candy-vendite.csv")  # carichiamo il secondo CSV


# UNIONE DEI DATAFRAME

df_unito = pd.merge(df_dati, df_vendite, on="competitorname", how="inner")  # uniamo i due DataFrame attraverso i nomi dei prodotti


# ESPLORAZIONE DF OTTENUTO

print(df_unito.head())  # visualizziamo le prime 5 righe del nuovo DataFrame

print(df_unito.shape)  # controlliamo il numero di righe e colonne

df_unito.info()  # visualizziamo le informazioni generali

print(df_unito.isnull().sum())  # controlliamo i valori mancanti

print(df_unito.duplicated().sum())  # controlliamo eventuali duplicati

# ANALISI DEI PRODOTTI

# Calcoliamo il fatturato moltiplicando le unità vendute per il prezzo di vendita
df_unito["fatturato"] = df_unito["unita_vendute"] * df_unito["prezzo_euro"]

# Calcoliamo il costo totale dei prodotti venduti
df_unito["costo_totale"] = df_unito["unita_vendute"] * df_unito["costo_unitario_euro"]

# Calcoliamo il guadagno lordo sottraendo i costi dal fatturato
df_unito["guadagno_lordo"] = df_unito["fatturato"] - df_unito["costo_totale"]

# Visualizziamo le prime 5 righe con i nuovi dati
print(df_unito[["competitorname", "fatturato", "costo_totale", "guadagno_lordo"]].head())


# ANALISI DEI RISULTATI TOTALI

print("Fatturato totale:", df_unito["fatturato"].sum())  # sommiamo il fatturato di tutti i prodotti

print("Costi totali:", df_unito["costo_totale"].sum())  # sommiamo i costi dei prodotti venduti

print("Guadagno lordo totale:", df_unito["guadagno_lordo"].sum())  # calcoliamo il guadagno lordo complessivo

# ANALISI DEI PRODOTTI PIÙ VENDUTI

# Ordiniamo i prodotti per unità vendute, dalla quantità maggiore alla minore
df_ordinato = df_unito.sort_values(by="unita_vendute", ascending=False)

# Selezioniamo i primi 5 prodotti più venduti
top_5 = df_ordinato.head(5)

# stampiamo i nomi dei prodotti e le relative quantità vendute
print(top_5[["competitorname", "unita_vendute"]])


# GRAFICO DEI 5 PRODOTTI PIÙ VENDUTI

plt.bar(top_5["competitorname"], top_5["unita_vendute"])  # creiamo un grafico a barre

plt.title("I 5 prodotti più venduti")  # inseriamo il titolo del grafico

plt.xlabel("Prodotti")  # inseriamo il nome dell'asse X

plt.ylabel("Unità vendute")  # inseriamo il nome dell'asse Y

plt.xticks(rotation=45)  # ruotiamo i nomi dei prodotti per migliorarne la leggibilità

plt.tight_layout()  # sistemiamo automaticamente gli spazi del grafico

plt.show()  # visualizziamo il grafico

# ANALISI DEI 5 PRODOTTI CON IL MAGGIORE GUADAGNO LORDO

# Ordiniamo i prodotti in base al guadagno lordo, dal maggiore al minore
df_guadagno = df_unito.sort_values(by="guadagno_lordo", ascending=False)

# Selezioniamo i primi 5 prodotti con il maggiore guadagno lordo
top_5_guadagno = df_guadagno.head(5)

# Visualizziamo il nome, le unità vendute e il guadagno lordo dei 5 prodotti
print(top_5_guadagno[["competitorname", "unita_vendute", "guadagno_lordo"]])


# GRAFICO DEI 5 PRODOTTI CON IL MAGGIORE GUADAGNO LORDO

plt.bar(top_5_guadagno["competitorname"], top_5_guadagno["guadagno_lordo"])  # creiamo il grafico a barre

plt.title("I 5 prodotti con il maggiore guadagno lordo")  # inseriamo il titolo

plt.xlabel("Prodotti")  # inseriamo il nome dell'asse X

plt.ylabel("Guadagno lordo (€)")  # inseriamo il nome dell'asse Y

plt.xticks(rotation=45)  # ruotiamo i nomi dei prodotti per renderli leggibili

plt.tight_layout()  # sistemiamo gli spazi del grafico

plt.show()  # visualizziamo il grafico