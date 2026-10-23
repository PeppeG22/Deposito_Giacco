import pandas as pd  # importiamo la libreria Pandas per la gestione e l'analisi dei dati

# CARICAMENTO DEL DATASET

df = pd.read_csv("Corso Python/15_venerdi23/test_pratico/candy-data.csv")  # carichiamo il file CSV all'interno di un DataFrame


# ESPLORAZIONE INIZIALE DEI DATI

print(df.head())  # visualizziamo le prime 5 righe del DataFrame per capire come sono organizzati i dati

print(df.shape)  # visualizziamo le dimensioni del DataFrame, ovvero il numero di righe e colonne

df.info()  # visualizziamo le informazioni generali, i tipi di dati e il numero di valori non nulli per colonna


# CONTROLLO DEI VALORI MANCANTI E DUPLICATI

print(df.isnull().sum())  # controlliamo quanti valori mancanti sono presenti in ogni colonna

print(df.duplicated().sum())  # controlliamo il numero di righe completamente duplicate nel DataFrame


# ANALISI STATISTICA DESCRITTIVA

print(df.describe())  # visualizziamo le principali statistiche delle colonne numeriche:
                      # conteggio, media, deviazione standard, minimo, quartili e massimo


# CONTROLLO DEI VALORI DELLE COLONNE BINARIE

colonne_binarie = ["chocolate", "fruity", "caramel",
                   "peanutyalmondy", "nougat",
                   "crispedricewafer", "hard", "bar", "pluribus"]  # definiamo le colonne che devono contenere solo 0 e 1

for colonna in colonne_binarie:  # scorriamo tutte le colonne binarie
    print(colonna, df[colonna].unique())  # visualizziamo i valori presenti per verificare che siano solo 0 e 1


# CONTROLLO DEGLI INTERVALLI DELLE PERCENTUALI

print(df[["sugarpercent", "pricepercent", "winpercent"]].min())  # controlliamo i valori minimi delle tre colonne

print(df[["sugarpercent", "pricepercent", "winpercent"]].max())  # controlliamo i valori massimi delle tre colonne


# CONTROLLO DEI NOMI DUPLICATI

print(df["competitorname"].duplicated().sum())  # verifichiamo se ci sono prodotti con lo stesso nome

# in conclusione questo csv risulta pulito 