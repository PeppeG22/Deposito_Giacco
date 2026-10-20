import numpy as np

#operazioni vettoriali : si apprica sui singoli vettori 

# ufuncs: funzioni universali come sin cos exp ecc... si applica su insiemi di elementi

#funzioni matematiche e statistiche: aritmetiche - matematiche - statistica 

#linspace: genera un array di numeri equidistanti es -> 

'''
6. LINSPACE

linspace() permette di generare un numero specifico di valori
distribuiti in maniera uniforme tra un valore iniziale e uno finale.

A differenza di arange(), dove specifichiamo il passo,
con linspace() indichiamo quanti valori vogliamo ottenere.

Il valore finale è incluso per impostazione predefinita.
'''


# ESEMPIO - LINSPACE

valori = np.linspace(0, 10, 5)  #generiamo 5 valori equidistanti tra 0 e 10

print(valori)  #stampiamo i valori: [0.  2.5  5.  7.5 10.]


'''
7. RANDOM

random è un modulo di NumPy che permette di generare
numeri casuali e array contenenti valori casuali.

Possiamo utilizzarlo per simulazioni, esperimenti statistici
e generazione di dati di prova.

Ad esempio, randint() genera numeri interi casuali
all'interno di un intervallo specificato.
'''


# ESEMPIO - RANDOM

numeri_casuali = np.random.randint(1, 11, size=5)  #generiamo 5 numeri casuali da 1 a 10

print(numeri_casuali)  #stampiamo i numeri casuali generati



'''

8. SUM

sum() è una funzione che permette di calcolare
la somma di tutti gli elementi presenti in un array.

È utile per eseguire rapidamente operazioni matematiche
senza utilizzare necessariamente un ciclo for.
'''


# ESEMPIO - SUM

numeri = np.array([10, 20, 30, 40])  #creiamo un array di numeri

totale = np.sum(numeri)  #calcoliamo la somma di tutti gli elementi

print('La somma è:', totale)  #stampiamo il risultato: 100


'''

9. MEAN

mean() è una funzione che permette di calcolare
la media aritmetica degli elementi presenti in un array.

La media viene calcolata dividendo la somma di tutti
i valori per il numero totale degli elementi.

È particolarmente utilizzata nell'analisi statistica.
'''


# ESEMPIO - MEAN



voti = np.array([20, 25, 30, 25])  #creiamo un array contenente alcuni voti

media = np.mean(voti)  #calcoliamo la media aritmetica dei voti

print('La media è:', media)  #stampiamo il risultato: 25.0



#std è un metodo che permette di trovare la deviazione standard su determinati valori

# ESEMPIO - STD (da fare)


'''
RIEPILOGO - NUMPY

np.array()         -> crea un array NumPy.
ndarray            -> rappresenta la struttura degli array NumPy.
dtype              -> indica il tipo di dato degli elementi.
shape              -> restituisce la forma e le dimensioni dell'array.
np.arange()        -> genera una sequenza di numeri con un passo.
reshape()          -> modifica la forma di un array.
np.linspace()      -> genera valori equidistanti in un intervallo.
np.random          -> permette di generare numeri casuali.
np.sum()           -> calcola la somma degli elementi.
np.mean()          -> calcola la media aritmetica degli elementi.
np.std()           -> calcola la deviazione standard degli elementi
'''