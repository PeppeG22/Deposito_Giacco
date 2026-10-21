import pandas as pd  #importiamo la libreria pandas
import numpy as np  #importiamo la libreria numpy


# PUNTO 1 - CREAZIONE DEL DATAFRAME

eta = np.random.randint(10, 81, size=6)  #generiamo 6 età casuali

salari = np.random.randint(1000, 4001, size=6)  #generiamo 6 salari casuali

data = {
    'Nome': ['Alice', 'Marco', 'Giulia', 'Luca', 'Anna', 'Paolo', 'Alice'],
    'Età': [eta[0], eta[1], None, eta[3], eta[4], eta[5], eta[0]],
    'Città': ['Roma', 'Milano', 'Napoli', 'Torino', 'Bari', 'Roma', 'Roma'],
    'Salario': [salari[0], salari[1], salari[2], None, salari[4], salari[5], salari[0]]
}  #creiamo un dizionario con dati casuali, valori mancanti e una riga duplicata

df = pd.DataFrame(data)  #trasformiamo il dizionario in un DataFrame

print(df)  #stampiamo il DataFrame originale


# PUNTO 2 - VISUALIZZAZIONE DELLE RIGHE

print(df.head())  #stampiamo le prime 5 righe

print(df.tail())  #stampiamo le ultime 5 righe


# PUNTO 3 - TIPI DI DATO

df.info()  #visualizziamo le informazioni e i tipi di dato delle colonne


# PUNTO 4 - STATISTICHE DESCRITTIVE

print(df.describe())  #stampiamo le principali statistiche descrittive

print(df[['Età', 'Salario']].mean())  #calcoliamo la media delle colonne 

print(df[['Età', 'Salario']].median())  #calcoliamo la mediana delle colonne 

print(df[['Età', 'Salario']].std())  #calcoliamo la deviazione standard


# PUNTO 5 - ELIMINAZIONE DEI DUPLICATI

print(df.duplicated())  #individuiamo le righe duplicate 

df = df.drop_duplicates()  #eliminiamo le righe duplicate

print(df)  #stampiamo il df senza duplicati


# PUNTO 6 - GESTIONE DEI VALORI MANCANTI

df['Età'] = df['Età'].fillna(df['Età'].median())  #sostituiamo le età mancanti con la mediana

df['Salario'] = df['Salario'].fillna(df['Salario'].median())  #sostituiamo i salari mancanti con la mediana

print(df)  #stampiamo il DataFrame senza valori mancanti


# PUNTO 7 - CATEGORIA ETÀ

categorie = []  #creiamo una lista vuota per contenere le categorie

for eta in df['Età']:  #scorriamo tutti i valori della colonna Età

    if eta <= 18:  #controlliamo se la persona è giovane
        categorie.append('Giovane')  #aggiungiamo la categoria Giovane

    elif eta <= 65:  #controlliamo se la persona è adulta
        categorie.append('Adulto')  #aggiungiamo la categoria Adulto

    else:  #caso in cui la persona ha più di 65 anni
        categorie.append('Senior')  #aggiungiamo la categoria Senior

df['Categoria Età'] = categorie  #aggiungiamo la nuova colonna al DataFrame

print('\nDataFrame finale:\n', df)  #stampiamo il DataFrame completo
