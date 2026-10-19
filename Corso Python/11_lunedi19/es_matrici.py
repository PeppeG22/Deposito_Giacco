import numpy as np  #importiamo la libreria NumPy


# PUNTO 1 - CREAZIONE DI UNA MATRICE 6X6

arr = np.random.randint(1, 101, size=36)  #creiamo un array di 36 numeri casuali tra 1 e 100

matrice = arr.reshape(6, 6)  #trasformiamo l'array in una matrice di 6 righe e 6 colonne


# PUNTO 2 - ESTRAZIONE DELLA MATRICE CENTRALE 4X4

matrice_centrale = matrice[1:5, 1:5]  #estraiamo le 4 righe e le 4 colonne centrali attraverso lo slicing


# PUNTO 3 - INVERSIONE DELLE RIGHE DELLA MATRICE CENTRALE

matrice_invertita = matrice_centrale[::-1]  #invertiamo l'ordine delle righe mantenendo tutte le colonne


# PUNTO 4 - ESTRAZIONE DELLA DIAGONALE PRINCIPALE

diagonale = np.diag(matrice_invertita)  #estraiamo la diagonale principale creando un array monodimensionale


# PUNTO 6 - STAMPA DELLE MATRICI PRIMA DELLA MODIFICA

print('\nMatrice originale 6x6:\n', matrice)  #stampiamo la matrice originale

print('\nMatrice centrale 4x4:\n', matrice_centrale)  #stampiamo la sottomatrice centrale

print('\nMatrice con righe invertite:\n', matrice_invertita)  #stampiamo la matrice invertita prima della modifica

print('\nDiagonale principale:\n', diagonale)  #stampiamo l'array contenente la diagonale


# PUNTO 5 - SOSTITUZIONE DEI MULTIPLI DI 3

matrice_invertita[matrice_invertita % 3 == 0] = -1  #sostituiamo tutti gli elementi multipli di 3 con -1


# PUNTO 6 - STAMPA DELLA MATRICE MODIFICATA

print('\nMatrice invertita modificata:\n', matrice_invertita)  #stampiamo la matrice dopo la sostituzione dei multipli di 3
