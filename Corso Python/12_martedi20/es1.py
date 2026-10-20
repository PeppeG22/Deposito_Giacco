import numpy as np  #importiamo la libreria NumPy


# PUNTO 1 - CREAZIONE DELL'ARRAY

arr1 = np.arange(0, 50)  #creiamo un array con 50 numeri da 0 a 49

arr2 = np.random.randint(49, 101, size=50)  #creiamo un array di 50 numeri casuali da 49 a 100

arr = np.concatenate((arr1, arr2))  #uniamo i due array in un unico array di 100 elementi

print('Array originale:', arr)  #stampiamo l'array
print('Tipo di dato:', arr.dtype)  #stampiamo il tipo di dato
print('Dimensioni:', arr.shape)  #stampiamo la forma dell'array


# PUNTO 2 - CONVERSIONE IN FLOAT64

arr = arr.astype('float64')  #convertiamo gli elementi dell'array in float64

print('Nuovo tipo di dato:', arr.dtype)  #verifichiamo il nuovo tipo di dato
print('Dimensioni:', arr.shape)  #verifichiamo nuovamente la forma dell'array


# PUNTO 3 - SLICING DELL'ARRAY

primi_10 = arr[:10]  #estraiamo i primi 10 elementi dell'array

ultimi_7 = arr[-7:]  #estraiamo gli ultimi 7 elementi dell'array

elementi_5_20 = arr[5:20]  #estraiamo gli elementi dall'indice 5 al 20 escluso

ogni_quarto = arr[::4]  #estraiamo ogni quarto elemento dell'array


# PUNTO 4 - MODIFICA ATTRAVERSO SLICING

arr[10:15] = 999  #sostituiamo con 999 gli elementi dall'indice 10 al 15 escluso


# PUNTO 5 - FANCY INDEXING E BOOLEAN INDEXING

indici = [0, 3, 7, 12, 25, 33, 48]  #lista con gli indici da selezionare

fancy = arr[indici]  #selezioniamo gli elementi attraverso il fancy indexing

pari = arr[arr % 2 == 0]  #selezioniamo tutti gli elementi pari attraverso il boolean indexing

media = np.mean(arr)  #calcoliamo la media di tutti gli elementi dell'array

maggiori_media = arr[arr > media]  #selezioniamo tutti gli elementi maggiori della media


# PUNTO 6 - STAMPA DEI RISULTATI

print('\n--- ARRAY MODIFICATO ---')
print(arr)  #stampiamo l'array dopo tutte le modifiche

print('\n--- SLICING ---')
print('Primi 10 elementi:', primi_10)  #stampiamo i primi 10 elementi
print('Ultimi 7 elementi:', ultimi_7)  #stampiamo gli ultimi 7 elementi
print('Elementi da 5 a 20:', elementi_5_20)  #stampiamo gli elementi dall'indice 5 al 20 escluso
print('Ogni quarto elemento:', ogni_quarto)  #stampiamo gli elementi selezionati con passo 4

print('\n--- FANCY INDEXING ---')
print('Elementi selezionati:', fancy)  #stampiamo gli elementi selezionati attraverso gli indici

print('\n--- BOOLEAN INDEXING ---')
print('Elementi pari:', pari)  #stampiamo tutti i valori pari
print('Media:', media)  #stampiamo la media dell'array
print('Elementi maggiori della media:', maggiori_media)  #stampiamo gli elementi maggiori della media
