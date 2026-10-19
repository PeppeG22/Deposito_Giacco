
'''
NUMPY - INDEXING E SLICING

NumPy permette di selezionare gli elementi di un array attraverso:

1. INDEXING -> seleziona un elemento attraverso il suo indice.
2. SLICING -> seleziona una porzione di elementi attraverso start, stop e step.
3. BOOLEAN INDEXING -> seleziona gli elementi che rispettano una condizione.
4. FANCY INDEXING -> seleziona elementi utilizzando indici interi specifici.
'''

import numpy as np  #importiamo la libreria NumPy


'''
1. INDEXING

L'indexing permette di accedere a un elemento attraverso
il suo indice, che parte da 0.

Negli array bidimensionali utilizziamo [riga, colonna].
'''

arr = np.array([10, 20, 30, 40, 50])  #creiamo un array

print(arr[2])  #stampiamo l'elemento con indice 2 -> 30
print(arr[-1])  #stampiamo l'ultimo elemento -> 50


'''
2. SLICING

Lo slicing permette di selezionare una parte di un array.

Sintassi: arr[start:stop:step]

start -> indice iniziale incluso.
stop -> indice finale escluso.
step -> passo tra gli elementi.

Possiamo omettere start, stop e step.
Lo slicing restituisce generalmente una vista dell'array originale.
'''

arr = np.arange(10)  #creiamo un array da 0 a 9

print(arr[1:8:2])  #selezioniamo da indice 1 a 7 con passo 2 -> [1 3 5 7]
print(arr[:5])  #selezioniamo i primi 5 elementi -> [0 1 2 3 4]
print(arr[5:])  #selezioniamo dall'indice 5 alla fine -> [5 6 7 8 9]
print(arr[-5:])  #selezioniamo gli ultimi 5 elementi -> [5 6 7 8 9]
print(arr[:-5])  #escludiamo gli ultimi 5 elementi -> [0 1 2 3 4]


'''
3. SLICING BIDIMENSIONALE

Permette di selezionare righe, colonne oppure entrambe.

Sintassi: matrice[righe, colonne]

Il simbolo : indica tutti gli elementi della dimensione.
'''

matrice = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])  #creiamo una matrice 3x3

print(matrice[0:2, :])  #selezioniamo le prime due righe
print(matrice[:, 1:3])  #selezioniamo la seconda e terza colonna
print(matrice[0:2, 1:3])  #slicing misto: prime due righe e ultime due colonne


'''
4. BOOLEAN INDEXING

Il boolean indexing permette di selezionare gli elementi
che rispettano una condizione booleana (True o False).

Esempio: arr[arr > 2]

ATTENZIONE: 2 rappresenta il VALORE, non l'indice.

Restituisce una copia degli elementi selezionati.
'''

arr = np.array([1, 2, 3, 4, 5])  #creiamo un array

print(arr[arr > 2])  #selezioniamo i valori maggiori di 2 -> [3 4 5]
print(arr[arr % 2 == 0])  #selezioniamo i numeri pari -> [2 4]


'''
5. FANCY INDEXING

Il fancy indexing permette di selezionare elementi
attraverso una lista o un array di indici interi.

Gli indici possono essere non consecutivi e in ordine diverso.
Restituisce una copia e non una vista dell'array originale.
'''

arr = np.array([10, 20, 30, 40, 50])  #creiamo un array

print(arr[[0, 2, 4]])  #selezioniamo gli elementi agli indici 0, 2 e 4 -> [10 30 50]


'''
DIFFERENZA TRA SLICING E FANCY INDEXING

SLICING:
- Utilizza start, stop e step.
- Seleziona porzioni regolari dell'array.
- Restituisce generalmente una vista, non una copia.

FANCY INDEXING:
- Utilizza liste o array di indici interi.
- Permette di scegliere posizioni specifiche.
- Restituisce una copia indipendente.

BOOLEAN INDEXING:
- Utilizza condizioni sui valori.
- Seleziona gli elementi per cui la condizione è True.
- Restituisce una copia.
'''
