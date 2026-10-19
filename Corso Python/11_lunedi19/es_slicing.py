

import numpy as np  #importiamo la libreria NumPy


# PUNTO 1 - CREAZIONE ARRAY

arr = np.random.randint(10, 51, size=20)  #creiamo un array di 20 numeri casuali tra 10 e 50

print('Array originale:', arr)  #stampiamo l'array prima delle modifiche


# PUNTO 2 - PRIMI 10 ELEMENTI

primi_10 = arr[:10]  #selezioniamo i primi 10 elementi dell'array


# PUNTO 3 - ULTIMI 5 ELEMENTI

ultimi_5 = arr[-5:]  #selezioniamo gli ultimi 5 elementi dell'array


# PUNTO 4 - ELEMENTI DALL'INDICE 5 AL 15

elementi = arr[5:15]  #selezioniamo gli elementi dall'indice 5 al 15 escluso


# PUNTO 5 - OGNI TERZO ELEMENTO

terzo_elemento = arr[::3]  #selezioniamo gli elementi con passo 3


# PUNTO 6 - MODIFICA ATTRAVERSO SLICING

arr[5:10] = 99  #assegniamo il valore 99 agli elementi dall'indice 5 al 10 escluso


# PUNTO 7 - STAMPA DEI RISULTATI

print('Array modificato:', arr)  #stampiamo l'array dopo la modifica
print('Primi 10 elementi:', primi_10)  #stampiamo i primi 10 elementi
print('Ultimi 5 elementi:', ultimi_5)  #stampiamo gli ultimi 5 elementi
print('Elementi dall indice 5 al 15:', elementi)  #stampiamo gli elementi selezionati
print('Ogni terzo elemento:', terzo_elemento)  #stampiamo gli elementi selezionati con passo 3
