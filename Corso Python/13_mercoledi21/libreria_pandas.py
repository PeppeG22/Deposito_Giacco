
'''
PANDAS - INTRODUZIONE E GESTIONE DEI DATI

Pandas è una libreria Python utilizzata per la gestione,
la manipolazione, la pulizia e l'analisi dei dati.

Offre un insieme di funzionalità strettamente correlate
a NumPy, su cui si basa per molte operazioni.

Pandas introduce due strutture dati fondamentali:

1. DATAFRAME

Il DataFrame è una struttura dati bidimensionale,
composta da righe e colonne, simile a un foglio Excel
oppure a una tabella di un database SQL.

Ogni colonna possiede un nome e può contenere
un tipo di dato differente rispetto alle altre colonne.

Possiamo creare un DataFrame attraverso un dizionario:
- Le chiavi rappresentano i nomi delle colonne.
- I valori rappresentano i dati contenuti nelle colonne.

2. SERIES

La Series è una struttura dati monodimensionale
che può essere vista come una singola colonna di un DataFrame.

Ogni elemento è associato a un indice, utilizzato
per identificare la sua posizione o etichetta.


FUNZIONI PRINCIPALI DI PANDAS

head(n=5) -> mostra le prime n righe del DataFrame.
             Per impostazione predefinita mostra le prime 5.

tail(n=5) -> mostra le ultime n righe del DataFrame.
             Per impostazione predefinita mostra le ultime 5.

describe() -> restituisce statistiche descrittive come
              media, deviazione standard, minimo,
              massimo e percentili delle colonne numeriche.
              Per impostazione predefinita analizza i dati numerici.

info() -> mostra le informazioni generali del DataFrame:
          numero di righe e colonne, nomi delle colonne,
          tipi di dato, valori non nulli e memoria utilizzata.
'''


import pandas as pd  #importiamo la libreria Pandas con alias pd


# ESEMPIO 1 - CREAZIONE DI UN DATAFRAME

data = {
    'Nome': ['Alice', 'Bob', 'Carla'],  #creiamo la colonna contenente i nomi
    'Età': [25, 30, 22],  #creiamo la colonna contenente le età
    'Città': ['Roma', 'Milano', 'Napoli']  #creiamo la colonna contenente le città
}

data['Sesso'] = ['F', 'M', 'F']  #aggiungiamo una nuova chiave al dizionario con i relativi valori

df = pd.DataFrame(data)  #trasformiamo il dizionario in un DataFrame

print(df)  #stampiamo il DataFrame completo

df.info()  #visualizziamo le informazioni generali del DataFrame


# ESEMPIO 2 - SERIES

nomi = df['Nome']  #selezioniamo una colonna del DataFrame ottenendo una Series

print(nomi)  #stampiamo la Series contenente i nomi


'''
3. GESTIONE DEI FILE CSV

CSV (Comma-Separated Values) è un formato di file testuale
utilizzato per memorizzare dati organizzati in righe e colonne.

I valori sono separati da un delimitatore,
generalmente una virgola oppure un punto e virgola.

Pandas permette di leggere e salvare file CSV
attraverso due funzioni principali:

pd.read_csv() -> legge un file CSV e lo trasforma in un DataFrame.

df.to_csv() -> salva il contenuto di un DataFrame in un file CSV.

PARAMETRI PRINCIPALI:

read_csv():
filepath -> nome o percorso del file da leggere.
sep -> separatore utilizzato nel CSV (virgola di default).
header -> indica quale riga contiene i nomi delle colonne.

to_csv():
path_or_buf -> nome o percorso del file da salvare.
index=False -> evita di salvare gli indici del DataFrame.
sep -> permette di scegliere il separatore.

ATTENZIONE:
Se il file CSV non esiste, read_csv() genera un errore.
'''


# ESEMPIO 3 - SALVATAGGIO DI UN DATAFRAME IN CSV

df.to_csv('persone.csv', index=False)  #salviamo il DataFrame in un file CSV senza gli indici

print('File CSV salvato correttamente!')  #confermiamo il salvataggio


# ESEMPIO 4 - LETTURA DI UN FILE CSV

df_csv = pd.read_csv('persone.csv')  #leggiamo il file CSV e lo trasformiamo in un DataFrame

print(df_csv)  #stampiamo i dati caricati dal file CSV


'''
4. PULIZIA DEI DATI - DATA CLEANING

La pulizia dei dati consiste nell'individuare e correggere
eventuali problemi presenti in un insieme di dati.

Tra le operazioni principali troviamo:

- Eliminazione dei valori duplicati.
- Gestione dei valori mancanti (NaN).
- Sostituzione dei valori mancanti.

NaN (Not a Number) viene utilizzato da Pandas e NumPy
per rappresentare molti valori numerici mancanti.

Pandas riconosce anche altri valori mancanti, come None e pd.NA.


FUNZIONI PRINCIPALI:

drop_duplicates() -> elimina le righe duplicate del DataFrame.
                     Con subset possiamo scegliere le colonne
                     da considerare per individuare i duplicati.

dropna() -> elimina le righe contenenti valori mancanti.
            Con axis=1 possiamo eliminare le colonne
            contenenti valori mancanti.

fillna() -> sostituisce i valori mancanti con un valore scelto,
            ad esempio 0, una stringa oppure una media.

isna() -> individua i valori mancanti restituendo True o False.

ATTENZIONE:
Questi metodi restituiscono normalmente un nuovo DataFrame
senza modificare automaticamente quello originale.
'''


# ESEMPIO 5 - CREAZIONE DI DATI CON DUPLICATI E VALORI MANCANTI

data_sporchi = {
    'Nome': ['Alice', 'Bob', 'Bob', 'Carla'],  #creiamo una colonna con un nome duplicato
    'Età': [25, None, None, 22],  #inseriamo alcuni valori mancanti
    'Città': ['Roma', 'Milano', 'Milano', None]  #inseriamo una città mancante
}

df_sporco = pd.DataFrame(data_sporchi)  #creiamo il DataFrame con dati da pulire

print(df_sporco)  #stampiamo il DataFrame originale


# ESEMPIO 6 - ELIMINAZIONE DEI DUPLICATI

df_senza_duplicati = df_sporco.drop_duplicates()  #eliminiamo le righe completamente duplicate

print(df_senza_duplicati)  #stampiamo il DataFrame senza duplicati


# ESEMPIO 7 - INDIVIDUAZIONE DEI VALORI MANCANTI

mancanti = df_sporco.isna()  #controlliamo quali elementi contengono valori mancanti

print(mancanti)  #stampiamo True dove il valore è mancante


# ESEMPIO 8 - ELIMINAZIONE DEI VALORI MANCANTI

df_senza_nan = df_sporco.dropna()  #eliminiamo tutte le righe contenenti almeno un valore mancante

print(df_senza_nan)  #stampiamo il DataFrame senza valori mancanti


# ESEMPIO 9 - SOSTITUZIONE DEI VALORI MANCANTI

df_riempito = df_sporco.fillna({'Età': 0, 'Città': 'Non specificata'})  #sostituiamo i valori mancanti nelle colonne indicate

print(df_riempito)  #stampiamo il DataFrame con i valori sostituiti


# ESEMPIO 10 - PULIZIA COMPLETA E SALVATAGGIO IN CSV

df_pulito = df_sporco.drop_duplicates()  #eliminiamo le righe duplicate

df_pulito = df_pulito.fillna({'Età': 0, 'Città': 'Non specificata'})  #riempiamo i valori mancanti

df_pulito.to_csv('persone_pulite.csv', index=False)  #salviamo il DataFrame pulito in un nuovo file CSV

print(df_pulito)  #stampiamo il DataFrame pulito


'''
RIEPILOGO - PANDAS

pd.DataFrame() -> crea un DataFrame.
pd.Series() -> crea una Series.

df.head() -> mostra le prime righe.
df.tail() -> mostra le ultime righe.
df.describe() -> restituisce statistiche descrittive.
df.info() -> mostra le informazioni generali.

pd.read_csv() -> legge un file CSV.
df.to_csv() -> salva un DataFrame in formato CSV.

df.drop_duplicates() -> elimina le righe duplicate.
df.dropna() -> elimina righe o colonne con valori mancanti.
df.fillna() -> sostituisce i valori mancanti.
df.isna() -> individua i valori mancanti.

PANDAS E NUMPY:

NumPy -> utilizzato principalmente per array e calcoli numerici.
Pandas -> utilizzato per organizzare, pulire e analizzare dati tabellari.
'''
