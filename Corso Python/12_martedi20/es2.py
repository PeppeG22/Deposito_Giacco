
'''
ESERCIZIO - NUMPY: LINSPACE, RESHAPE E RANDOM

1. Creare un array utilizzando linspace con 12 numeri.
2. Trasformare l'array in una matrice 3x4.
3. Generare una matrice 3x4 con numeri casuali tra 0 e 1.
4. Calcolare e stampare la somma degli elementi di entrambe le matrici.

EXTRA:
Convertire tutti gli elementi dell'array originale in numeri interi.
'''

import numpy as np  #importiamo la libreria NumPy


# PUNTO 1 - CREAZIONE ARRAY CON LINSPACE

arr = np.linspace(0, 1, 12)  #generiamo 12 valori equidistanti tra 0 e 1

print(arr) #stampa prima della conversione in interi


# PUNTO 2 - TRASFORMAZIONE IN MATRICE 3X4

matr = arr.reshape(3, 4)  #trasformiamo l'array in una matrice di 3 righe e 4 colonne


# PUNTO 3 - CREAZIONE MATRICE CON NUMERI CASUALI

matr_random = np.random.rand(3, 4)  #creiamo una matrice 3x4 con numeri casuali tra 0 e 1


# PUNTO 4 - CALCOLO DELLA SOMMA DELLE MATRICI

somma_matr = np.sum(matr)  #calcoliamo la somma di tutti gli elementi della prima matrice

somma_random = np.sum(matr_random)  #calcoliamo la somma degli elementi della matrice casuale


# STAMPA DEI RISULTATI

print('\nPrima matrice:\n', matr)  #stampiamo la prima matrice
print('Somma prima matrice:', somma_matr)  #stampiamo la somma della prima matrice

print('\nMatrice casuale:\n', matr_random)  #stampiamo la matrice casuale
print('Somma matrice casuale:', somma_random)  #stampiamo la somma della matrice casuale


# EXTRA - CONVERSIONE IN NUMERI INTERI

arr = arr.astype('int32')  #convertiamo tutti gli elementi dell'array originale in numeri interi



print('\nArray iniziale convertito:\n', arr)  #stampiamo la matrice con i numeri interi
print('Tipo di dato:', arr.dtype)  #verifichiamo il tipo di dato degli elementi
