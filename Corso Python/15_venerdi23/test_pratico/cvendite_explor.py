import pandas as pd  # importiamo la libreria Pandas
import numpy as np  # importiamo la libreria NumPy

# CARICAMENTO DEL DATASET

df = pd.read_csv("Corso Python/15_venerdi23/test_pratico/candy-vendite.csv")  # carichiamo il file CSV

# ESPLORAZIONE DEI DATI

print(df.head())  # visualizziamo le prime 5 righe

print(df.shape)  # visualizziamo il numero di righe e colonne

print(df.info())  # controlliamo i tipi di dati e i valori non nulli

print(df.isnull().sum())  # contiamo i valori mancanti per colonna

print(df.duplicated().sum())  # contiamo le righe duplicate

print(df.describe())  # visualizziamo le statistiche descrittive

# CONTROLLO DEI NOMI DUPLICATI

print(df["competitorname"].duplicated().sum())  # controlliamo se ci sono prodotti con lo stesso nome


# CONTROLLO DEI VALORI NEGATIVI

print(df.select_dtypes(include="number").min())  # controlliamo che le colonne numeriche non contengano valori negativi


# CONTROLLO DEI PREZZI

print(df[df["prezzo_euro"] < df["costo_unitario_euro"]])  # cerchiamo prodotti venduti a un prezzo inferiore al costo


# CONTROLLO DELLE VALUTAZIONI

print(df["valutazione_clienti"].min())  # visualizziamo la valutazione minima

print(df["valutazione_clienti"].max())  # visualizziamo la valutazione massima


# CONTROLLO DELLE AREE DI VENDITA

print(df["area_vendita"].unique())  # visualizziamo le diverse aree geografiche presenti