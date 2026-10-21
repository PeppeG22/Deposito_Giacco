import numpy as np  #importiamo la libreria NumPy

# ESERCIZIO 1 - SOMMA E MEDIA DI ELEMENTI

arr1 = np.random.randint(1, 101, size=15)  #creiamo un array di 15 numeri casuali interi tra 1 e 100

somma = np.sum(arr1)  #calcoliamo la somma di tutti gli elementi dell'array

media = np.mean(arr1)  #calcoliamo la media di tutti gli elementi dell'array

print('Array:', arr1)  #stampiamo l'array generato
print('Somma:', somma)  #stampiamo la somma degli elementi
print('Media:', media)  #stampiamo la media degli elementi


# ESERCIZIO 2 - MANIPOLAZIONE DI ARRAY MULTIDIMENSIONALI


matrice = np.arange(1, 26).reshape(5, 5)  #creiamo una matrice 5x5 con numeri sequenziali da 1 a 25

seconda_colonna = matrice[:, 1]  #estraiamo la seconda colonna della matrice

terza_riga = matrice[2, :]  #estraiamo la terza riga della matrice

diagonale_principale = np.diag(matrice)  #estraiamo la diagonale principale della matrice

somma_diagonale = np.sum(diagonale_principale)  #calcoliamo la somma degli elementi della diagonale principale

print('\nESERCIZIO 2')  #stampiamo il titolo dell'esercizio
print('Matrice:\n', matrice)  #stampiamo la matrice completa
print('Seconda colonna:', seconda_colonna)  #stampiamo la seconda colonna
print('Terza riga:', terza_riga)  #stampiamo la terza riga
print('Diagonale principale:', diagonale_principale)  #stampiamo la diagonale principale
print('Somma diagonale principale:', somma_diagonale)  #stampiamo la somma della diagonale principale

# ESERCIZIO 3 - OPERAZIONI CON FANCY INDEXING


arr3 = np.random.randint(10, 51, size=(4, 4))  #creiamo una matrice 4x4 con numeri casuali interi tra 10 e 50

righe = [0, 1, 2, 3]  #indichiamo gli indici delle righe degli elementi da selezionare
colonne = [1, 3, 2, 0]  #indichiamo gli indici delle colonne degli elementi da selezionare

elementi_selezionati = arr3[righe, colonne]  #selezioniamo gli elementi agli indici (0,1), (1,3), (2,2) e (3,0)

righe_dispari = arr3[[1, 3], :]  #selezioniamo tutte le righe dispari considerando che si parte da 0

arr3[righe, colonne] = arr3[righe, colonne] + 10  #modifichiamo gli elementi selezionati aggiungendo 10 al loro valore

print('Array 4x4 originale con modifiche:\n', arr3)  #stampiamo l'array dopo la modifica
print('Elementi selezionati con fancy indexing:', elementi_selezionati)  #stampiamo gli elementi selezionati
print('Righe dispari:\n', righe_dispari)  #stampiamo le righe dispari