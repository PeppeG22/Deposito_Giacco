import pandas as pd  


# PUNTO 1 - CREAZIONE DEL DATAFRAME

data = {
    'Prodotto': ['Mouse', 'Tastiera', 'Monitor', 'Mouse', 'Cuffie',
                 'Monitor', 'Tastiera', 'Mouse', 'Cuffie', 'Monitor'],
    'Quantità': [12, 8, 5, 20, 15, 4, 10, 18, 12, 6],
    'Prezzo Unitario': [25, 70, 250, 25, 60, 250, 70, 25, 60, 250],
    'Città': ['Roma', 'Milano', 'Roma', 'Napoli', 'Milano',
              'Roma', 'Napoli', 'Roma', 'Napoli', 'Milano']
}  #creiamo un dizionario contenente le vendite dei prodotti

df = pd.DataFrame(data)  #trasformiamo il dizionario in un DataFrame

print('\nDATAFRAME ORIGINALE:\n', df)  #stampiamo il DataFrame originale


# PUNTO 2 - AGGIUNTA DELLA COLONNA TOTALE VENDITE

df['Totale Vendite'] = df['Quantità'] * df['Prezzo Unitario']  #calcoliamo il totale di ogni vendita

print('\nDATAFRAME AGGIORNATO:\n', df)  #stampiamo il DataFrame con la nuova colonna


# PUNTO 3 - RAGGRUPPAMENTO DELLE VENDITE PER PRODOTTO

vendite_prodotti = df.groupby('Prodotto')['Totale Vendite'].sum()  #raggruppiamo i prodotti e sommiamo le vendite

print('\nTOTALE VENDITE PER PRODOTTO:\n', vendite_prodotti)  #stampiamo le vendite totali di ogni prodotto


# PUNTO 4 - PRODOTTO PIÙ VENDUTO IN QUANTITÀ

quantita_prodotti = df.groupby('Prodotto')['Quantità'].sum()  #calcoliamo la quantità totale venduta per ogni prodotto

prodotto_piu_venduto = quantita_prodotti.idxmax()  #individuiamo il prodotto con la quantità maggiore

print('\nPRODOTTO PIÙ VENDUTO:', prodotto_piu_venduto)  #stampiamo il nome del prodotto


# PUNTO 5 - CITTÀ CON MAGGIOR VOLUME DI VENDITE

vendite_citta = df.groupby('Città')['Totale Vendite'].sum()  #calcoliamo il totale delle vendite per ogni città

citta_maggiore = vendite_citta.idxmax()  #individuiamo la città con il totale maggiore

print('\nVENDITE PER CITTÀ:\n', vendite_citta)  #stampiamo i totali delle città

print('\nCITTÀ CON MAGGIORI VENDITE:', citta_maggiore)  #stampiamo la città con maggiori vendite


# PUNTO 6 - FILTRO DELLE VENDITE SUPERIORI A 1000 EURO

vendite_superiori = df[df['Totale Vendite'] > 1000]  #selezioniamo solamente le vendite superiori a 1000 euro

print('\nVENDITE SUPERIORI A 1000 EURO:\n', vendite_superiori)  #stampiamo il nuovo DataFrame


# PUNTO 8 - NUMERO DI VENDITE PER OGNI CITTÀ

numero_vendite = df['Città'].value_counts()  #contiamo quante operazioni di vendita sono presenti per ogni città

print('\nNUMERO DI VENDITE PER CITTÀ:\n', numero_vendite)  #stampiamo il numero delle vendite
