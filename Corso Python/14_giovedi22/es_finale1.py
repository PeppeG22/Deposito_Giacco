import pandas as pd  # importiamo pandas
import numpy as np  # importiamo numpy

dati = {  # creiamo il dizionario con alcuni valori mancanti e una vendita negativa
    "Data": [
        "2026-10-01", "2026-10-04", "2026-10-08",
        "2026-10-12", "2026-10-16", "2026-10-20",
        "2026-10-24", "2026-10-28", "2026-10-31"
    ],  # date delle vendite
    "Città": [
        "Roma", "Milano", "Napoli",
        "Roma", "Milano", None,
        "Roma", "Milano", "Napoli"
    ],  # inseriamo una città mancante
    "Prodotto": [
        "Caffè", "Gelato", "Cornetto",
        "Gelato", "Cornetto", "Caffè",
        None, "Caffè", "Gelato"
    ],  # inseriamo un prodotto mancante
    "Vendite": [
        120, 85, 60,
        95, None, -150,
        55, 130, 100
    ]  # inseriamo una vendita mancante e una negativa
}

# GENERAZIONE DI DATI

dati["Prezzo"] = np.random.randint(1, 11, size=9)  # aggiungiamo 9 prezzi casuali da 1 a 10 euro

df = pd.DataFrame(dati)  # creiamo il DataFrame

# ANALISI E PULIZIA

df.info()  # visualizziamo le informazioni generali del DataFrame

print(df.shape)  # stampiamo il numero di righe e colonne

print(df.isna().sum())  # contiamo i valori mancanti per ogni colonna

duplicati = df.duplicated().sum()  # contiamo le righe completamente duplicate

print(duplicati)  # stampiamo il numero di duplicati

df = df.drop_duplicates()  # eliminiamo eventuali righe completamente duplicate

df["Città"] = df["Città"].fillna("Sconosciuta")  # riempiamo la città mancante

df["Prodotto"] = df["Prodotto"].fillna("Sconosciuto")  # riempiamo il prodotto mancante

df["Vendite"] = df["Vendite"].abs()  # trasformiamo la vendita negativa in positiva: -150 diventa 150

media_vendite = df["Vendite"].mean()  # calcoliamo la media ignorando il valore mancante

df["Vendite"] = df["Vendite"].fillna(media_vendite)  # riempiamo la vendita mancante con la media

print(df)  # stampiamo il DataFrame pulito

print(df.describe())  # visualizziamo le statistiche delle colonne numeriche

# TABELLA PIVOT

tabella_pivot = df.pivot_table(
    values="Vendite",  # valori su cui calcolare la media
    index="Prodotto",  # prodotti sulle righe
    columns="Città",  # città sulle colonne
    aggfunc="mean"  # calcoliamo la media
)

print(tabella_pivot)  # stampiamo la tabella pivot

# GROUPBY

vendite_totali = df.groupby("Prodotto")["Vendite"].sum()  # calcoliamo le vendite totali per ogni prodotto

print(vendite_totali)  # stampiamo i totali