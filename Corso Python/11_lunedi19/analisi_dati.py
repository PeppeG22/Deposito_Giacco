
'''
NUMPY - PANDAS - MATPLOTLIB

NumPy, Pandas e Matplotlib sono tre librerie distinte di Python
che possono collaborare tra loro per l'analisi e la gestione dei dati.

- NumPy -> permette di lavorare con array, matrici e calcoli numerici.
- Pandas -> permette di organizzare, gestire e analizzare i dati attraverso tabelle.
- Matplotlib -> permette di rappresentare i dati attraverso grafici.

Queste librerie sono molto utilizzate nell'analisi dei dati,
nella statistica e nel calcolo scientifico.


INSTALLAZIONE DELLE LIBRERIE - PIP

Le librerie possono essere installate attraverso pip,
il gestore dei pacchetti di Python (package installer for Python).

Pip permette di:

1. INSTALLARE -> scaricare e installare librerie e pacchetti.
2. GESTIRE LE DIPENDENZE -> installare le librerie necessarie al funzionamento
   di altri pacchetti e verificare i requisiti di versione.
3. AGGIORNARE E RIMUOVERE -> aggiornare o disinstallare i pacchetti.
4. AMBIENTI VIRTUALI -> installare pacchetti all'interno di ambienti
   virtuali, mantenendo separate le librerie dei diversi progetti.


'''


'''
COS'È NUMPY

NumPy è una libreria fondamentale per il calcolo scientifico
che mette a disposizione array e matrici multidimensionali.

A differenza delle liste tradizionali di Python, attraverso
le operazioni vettoriali possiamo eseguire calcoli direttamente
su tutti gli elementi di un array, senza dover utilizzare
necessariamente un ciclo for.

Gli array di NumPy contengono elementi di uno stesso tipo di dato,
permettendo una gestione più efficiente della memoria e dei calcoli.

NumPy è una libreria open source, quindi il suo codice è pubblico
e può essere utilizzato e modificato secondo la sua licenza.

È particolarmente importante perché molte operazioni sono
implementate in linguaggi come C, garantendo prestazioni elevate.
Permette inoltre di interagire con codice C e C++.
'''


# IMPORTAZIONE DELLA LIBRERIA NUMPY

import numpy as np  #importiamo la libreria NumPy utilizzando l'alias np


# ESEMPIO - DIFFERENZA TRA LISTA E ARRAY

numeri_lista = [1, 2, 3, 4]  #creiamo una lista tradizionale

numeri_array = np.array([1, 2, 3, 4])  #creiamo un array attraverso NumPy

print(numeri_lista * 2)  #ripete due volte gli elementi della lista
print(numeri_array * 2)  #moltiplica ogni elemento dell'array per 2


'''
PAROLE CHIAVE PRINCIPALI DI NUMPY


1. NDARRAY

ndarray (N-dimensional array) è la struttura dati principale
di NumPy e rappresenta un array che può avere una o più dimensioni.

Un array può essere:
- Monodimensionale -> una sequenza di elementi.
- Bidimensionale -> una matrice composta da righe e colonne.
- Multidimensionale -> una struttura con più di due dimensioni.

La funzione np.array() permette di creare un oggetto ndarray.
'''


# ESEMPIO - NDARRAY

array_1d = np.array([10, 20, 30])  #creiamo un array monodimensionale

array_2d = np.array([[1, 2, 3], [4, 5, 6]])  #creiamo un array bidimensionale

print(array_1d)  #stampiamo l'array monodimensionale
print(array_2d)  #stampiamo la matrice bidimensionale

print(type(array_1d))  #verifichiamo che l'oggetto sia di tipo ndarray


'''
2. DTYPE

dtype (data type) è un attributo che permette di conoscere
il tipo di dato contenuto all'interno di un array NumPy.

Ad esempio, possiamo avere:
- int -> numeri interi.
- float -> numeri decimali.
- bool -> valori booleani.

A differenza delle liste Python, gli array NumPy utilizzano
un tipo di dato comune per tutti gli elementi.
'''


# ESEMPIO - DTYPE

numeri = np.array([1, 2, 3, 4])  #creiamo un array di numeri interi

print(numeri.dtype)  #stampiamo il tipo di dato dell'array

decimali = np.array([1.5, 2.5, 3.5])  #creiamo un array di numeri decimali

print(decimali.dtype)  #stampiamo il tipo di dato dei numeri decimali


'''
3. SHAPE

shape è un attributo che permette di conoscere la forma
e le dimensioni di un array.

Restituisce una tupla che indica il numero di elementi
presenti lungo ogni dimensione.

Ad esempio, in una matrice bidimensionale:
(2, 3) -> indica 2 righe e 3 colonne.
'''


# ESEMPIO - SHAPE

matrice = np.array([[1, 2, 3], [4, 5, 6]])  #creiamo una matrice con 2 righe e 3 colonne

print(matrice.shape)  #stampiamo la forma della matrice (2, 3)


'''
4. ARANGE

arange() è una funzione che permette di generare automaticamente
una sequenza di numeri all'interno di un array NumPy.

Funziona in maniera simile a range() di Python.

Può ricevere tre parametri:
- start -> numero iniziale.
- stop -> limite finale escluso.
- step -> intervallo tra un numero e il successivo.
'''


# ESEMPIO - ARANGE

sequenza = np.arange(0, 10, 2)  #creiamo un array da 0 a 10 escluso, con passo 2

print(sequenza)  #stampiamo la sequenza: [0 2 4 6 8]


'''
5. RESHAPE

reshape() permette di modificare la forma di un array,
organizzando i suoi elementi in un numero diverso di dimensioni.

Ad esempio, possiamo trasformare un array monodimensionale
in una matrice composta da righe e colonne.

ATTENZIONE:
Il numero totale degli elementi deve rimanere invariato.
'''


# ESEMPIO - RESHAPE

numeri = np.array([1, 2, 3, 4, 5, 6])  #creiamo un array con 6 elementi

matrice = numeri.reshape(2, 3)  #trasformiamo l'array in una matrice di 2 righe e 3 colonne

print(matrice)  #stampiamo la nuova matrice
print(matrice.shape)  #controlliamo la nuova forma dell'array
