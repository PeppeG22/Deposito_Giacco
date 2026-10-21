
'''
PANDAS - MANIPOLAZIONE E TRASFORMAZIONE DEI DATI

Pandas permette di manipolare, organizzare e trasformare i dati
attraverso diverse operazioni.

Tra le principali troviamo:

1. CONCATENAZIONE -> unisce più DataFrame lungo righe o colonne.
2. MERGE / JOIN -> unisce DataFrame attraverso colonne o indici comuni.
3. MULTIINDEX -> permette di utilizzare indici a più livelli.
4. PIVOT -> permette di riorganizzare la disposizione dei dati.
5. GROUPBY -> permette di raggruppare e analizzare i dati.

Queste operazioni sono particolarmente utilizzate
nell'analisi e nella pulizia dei dataset.
'''

import pandas as pd  #importiamo la libreria Pandas


'''
1. MULTIINDEX

MultiIndex è una struttura di Pandas che permette di creare
un indice a più livelli, utilizzando più colonne come riferimento.

È utile per organizzare dati gerarchici, ad esempio
vendite suddivise per Paese e Anno.

set_index() -> imposta una o più colonne come indice.
'''


# ESEMPIO 1 - MULTIINDEX

data_2 = {
    'Paese': ['Italia', 'Italia', 'Francia', 'Francia'],
    'Anno': [2023, 2024, 2025, 2026],
    'Vendite': [120, 123, 140, 160]
}  #creiamo un dizionario contenente Paese, Anno e Vendite

df_multi = pd.DataFrame(data_2)  #creiamo un DataFrame

df_multi = df_multi.set_index(['Paese', 'Anno'])  #impostiamo Paese e Anno come indici a due livelli

print(df_multi)  #stampiamo il DataFrame con MultiIndex


'''
2. LOC - SELEZIONE ATTRAVERSO ETICHETTE

loc permette di selezionare righe e colonne attraverso
le loro etichette, anziché attraverso la posizione numerica.

Può essere utilizzato anche con MultiIndex per selezionare
elementi attraverso più livelli di indice.

SINTASSI:
df.loc[etichetta_riga, etichetta_colonna]

ATTENZIONE:
loc utilizza le etichette degli indici e delle colonne,
non cerca genericamente un valore contenuto nel DataFrame.
'''


# ESEMPIO 2 - LOC CON MULTIINDEX

print(df_multi.loc['Italia'])  #selezioniamo tutte le righe relative all'Italia

print(df_multi.loc[('Italia', 2023)])  #selezioniamo la riga relativa all'Italia nel 2023


'''
3. PIVOT E PIVOT_TABLE

Pivot è una funzionalità di Pandas che permette di trasformare
e riorganizzare la disposizione dei dati senza modificarne
necessariamente i valori originali.

pivot() -> riorganizza i dati trasformando i valori
           di alcune colonne in nuove righe o colonne.
           Richiede combinazioni uniche tra indici e colonne.

pivot_table() -> permette di riorganizzare i dati e,
                 quando necessario, aggregare più valori
                 attraverso funzioni statistiche.

Pivot_table è quindi più flessibile di pivot,
perché permette anche di effettuare aggregazioni.

PARAMETRI PRINCIPALI:

values -> colonna contenente i valori da analizzare.
index -> colonna da utilizzare come indice delle righe.
columns -> colonna i cui valori diventano nuove colonne.
aggfunc -> funzione di aggregazione, ad esempio mean o sum.

AGGFUNC:
'mean' -> calcola la media.
'sum' -> calcola la somma.
'count' -> conta i valori non mancanti.

La funzione pivot_table() restituisce un nuovo DataFrame,
senza modificare direttamente quello originale.
'''


# ESEMPIO 3 - CREAZIONE DEL DATAFRAME

data = {
    'Data': ['2021-01-01', '2021-01-01', '2021-01-01',
             '2021-01-02', '2021-01-02'],
    'Città': ['Roma', 'Milano', 'Napoli', 'Roma', 'Milano'],
    'Prodotto': ['Mouse', 'Tastiera', 'Mouse', 'Tastiera', 'Mouse'],
    'Vendite': [100, 200, 150, 300, 250]
}  #creiamo un dizionario contenente i dati delle vendite

df = pd.DataFrame(data)  #trasformiamo il dizionario in un DataFrame

print(df)  #stampiamo il DataFrame originale


# ESEMPIO 4 - CREAZIONE DELLA TABELLA PIVOT

pivot_df = df.pivot_table(
    values='Vendite',  #selezioniamo la colonna contenente i valori
    index='Prodotto',  #utilizziamo i prodotti come indici delle righe
    columns='Città',  #utilizziamo le città come colonne
    aggfunc='mean'  #calcoliamo la media delle vendite per ogni combinazione
)

print(pivot_df)  #stampiamo la tabella pivot

#RISULTATO:
# Città     Milano  Napoli   Roma
# Prodotto
# Mouse      250.0   150.0  100.0
# Tastiera   200.0     NaN  300.0

#NaN indica che non abbiamo dati per quella combinazione
#in questo caso non risultano vendite di tastiere a Napoli


'''
4. SPLIT - APPLY - COMBINE

Split-Apply-Combine è un principio utilizzato da Pandas
per raggruppare ed elaborare i dati attraverso tre fasi:

1. SPLIT -> divide il DataFrame in gruppi in base a una colonna.

2. APPLY -> applica un'operazione a ciascun gruppo,
            ad esempio somma, media oppure conteggio.

3. COMBINE -> combina i risultati dei gruppi
              in un'unica struttura dati.

Questa procedura viene utilizzata attraverso groupby().

groupby() -> raggruppa i dati in base a una o più colonne.
'''


# ESEMPIO 5 - SPLIT APPLY COMBINE

gruppi = df.groupby('Prodotto')  #raggruppiamo le righe in base al prodotto

vendite_totali = gruppi['Vendite'].sum()  #calcoliamo la somma delle vendite per ogni gruppo

print(vendite_totali)  #stampiamo le vendite totali di ogni prodotto

#RISULTATO:
# Mouse       500
# Tastiera    500

#SPLIT -> dividiamo i dati in Mouse e Tastiera
#APPLY -> calcoliamo la somma delle vendite di ogni prodotto
#COMBINE -> Pandas restituisce i risultati raggruppati


'''
5. CONCATENAZIONE E UNIONE DEI DATAFRAME

Pandas permette di combinare più DataFrame.

concat() -> concatena i DataFrame aggiungendo righe o colonne.

merge() -> unisce due DataFrame in base a una colonna comune,
           attraverso una logica simile ai JOIN di SQL.

PARAMETRI PRINCIPALI:

concat():
axis=0 -> concatena i DataFrame verticalmente, aggiungendo righe.
axis=1 -> concatena i DataFrame orizzontalmente, aggiungendo colonne.
ignore_index=True -> ricrea gli indici numerici delle righe.

merge():
on -> indica la colonna comune da utilizzare.
how -> indica il tipo di unione (inner, left, right, outer).
'''


# ESEMPIO 6 - CONCATENAZIONE

nuove_vendite = pd.DataFrame({
    'Data': ['2021-01-03'],
    'Città': ['Roma'],
    'Prodotto': ['Mouse'],
    'Vendite': [120]
})  #creiamo un secondo DataFrame contenente una nuova vendita

df_completo = pd.concat([df, nuove_vendite], ignore_index=True)  #aggiungiamo la nuova riga al DataFrame

print(df_completo)  #stampiamo il DataFrame concatenato


# ESEMPIO 7 - MERGE

categorie = pd.DataFrame({
    'Prodotto': ['Mouse', 'Tastiera'],
    'Categoria': ['Accessori', 'Periferiche']
})  #creiamo un DataFrame con le categorie dei prodotti

df_unito = pd.merge(df, categorie, on='Prodotto', how='left')  #uniamo i DataFrame attraverso la colonna Prodotto

print(df_unito)  #stampiamo il DataFrame con la nuova colonna Categoria


'''
RIEPILOGO - PANDAS

set_index() -> imposta una o più colonne come indice.
MultiIndex -> permette di avere indici a più livelli.
loc[] -> seleziona righe e colonne attraverso etichette.

pivot() -> riorganizza la disposizione dei dati senza aggregarli.
pivot_table() -> riorganizza e aggrega i dati.
aggfunc -> definisce la funzione di aggregazione.

groupby() -> raggruppa i dati secondo una o più colonne.

SPLIT -> divide i dati in gruppi.
APPLY -> applica un'operazione a ogni gruppo.
COMBINE -> combina i risultati ottenuti.

concat() -> concatena DataFrame per righe o colonne.
merge() -> unisce DataFrame attraverso colonne comuni.
'''
