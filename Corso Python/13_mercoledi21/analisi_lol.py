
import pandas as pd  

# IMPORTAZIONE DEL DATASET

df = pd.read_csv('Corso Python/13_mercoledi21/LoLChampions.csv')  #importiamo il file CSV trasformandolo in un DataFrame

print(df.head())  #visualizziamo le prime 5 righe del dataset

df.info()  #visualizziamo le informazioni generali del df

print(df.shape)  #stampiamo il numero di righe e colonne del dataset


# CONTROLLO DEI VALORI MANCANTI E DUPLICATI

duplicati = df.duplicated()  #numero di righe completamente duplicate

print(duplicati)  #stampiamo il numero di righe duplicate

# ANALISI STATISTICHE ELEMENTI DEL CSV

print(df.describe())  #visualizziamo le statistiche descrittive delle colonne numeriche

print('\nValori minimi:\n', df[['hp', 'armor', 'magicResist', 'attackDamage', 'attackSpeed']].min())  #controlliamo i valori minimi

print('\nValori massimi:\n', df[['hp', 'armor', 'magicResist', 'attackDamage', 'attackSpeed']].max())  #controlliamo i valori massimi


# AGGIUNTA DI DUE NUOVE COLONNE

df['Difesa'] = df['armor'] + df['magicResist']  #creiamo una colonna sommando armatura e mr

df['DPS'] = df['attackDamage'] * df['attackSpeed']  #calcoliamo il danno al secondo degli attacchi base

print('\nDataFrame con nuove colonne:\n', df.head())  #stampiamo le prime 5 righe del df aggiornato

df.info()  # vediamo le info delle nuove colonne

df.to_csv('lol_champions_pulito.csv')  #salviamo il df aggiornato 