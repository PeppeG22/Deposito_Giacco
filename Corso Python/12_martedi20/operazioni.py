import numpy as np

#operazioni vettoriali : si apprica sui singoli vettori 

# ufuncs: funzioni universali come sin cos exp ecc... si applica su insiemi di elementi

#funzioni matematiche e statistiche: aritmetiche - matematiche - statistica 

#linspace: genera un array di numeri equidistanti es -> 

'''
1. LINSPACE

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
2. RANDOM

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

3. SUM

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

4. MEAN

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

#---------------------------------------------------------------------------------------------------


# NUMPY - ALGEBRA LINEARE, FOURIER E BROADCASTING

import numpy as np  #importiamo la libreria NumPy


'''
1. ALGEBRA LINEARE - NUMPY.LINALG

NumPy contiene un modulo chiamato linalg che permette
di eseguire operazioni di algebra lineare su vettori e matrici.

FUNZIONI PRINCIPALI:

np.dot() -> calcola il prodotto scalare tra vettori o il prodotto tra matrici 2D.
np.matmul() -> esegue il prodotto matriciale.
np.linalg.det() -> calcola il determinante di una matrice quadrata.
np.linalg.eig() -> calcola gli autovalori e gli autovettori di una matrice.
np.linalg.inv() -> calcola l'inversa di una matrice.
np.linalg.norm() -> calcola la norma di un vettore o di una matrice.
np.linalg.solve() -> risolve un sistema di equazioni lineari.
'''


# ESEMPIO 1 - INVERSA DI UNA MATRICE

A = np.array([[1, 2], [3, 4]])  #creiamo una matrice quadrata 2x2

A_inv = np.linalg.inv(A)  #calcoliamo l'inversa della matrice

print(A_inv)  #stampiamo la matrice inversa

#la matrice inversa, moltiplicata per quella originale,
#restituisce la matrice identità attraverso il prodotto matriciale
#l'inversa esiste soltanto se il determinante è diverso da zero


# ESEMPIO 2 - NORMA DI UN VETTORE

v = np.array([3, 4])  #creiamo un vettore con due elementi

norma = np.linalg.norm(v)  #calcoliamo la norma euclidea del vettore

print(norma)  #stampiamo il risultato -> 5.0

#la norma euclidea misura la lunghezza del vettore
#in questo caso: radice quadrata di (3² + 4²) = 5


# ESEMPIO 3 - RISOLUZIONE DI SISTEMI LINEARI

'''
np.linalg.solve(A, B)

Permette di risolvere sistemi di equazioni lineari
nella forma Ax = B.

A -> matrice quadrata dei coefficienti.
B -> vettore o matrice dei termini noti.
x -> soluzione del sistema.

Per ottenere una soluzione unica, A deve essere invertibile.
'''

A = np.array([[3, 1], [1, 2]])  #creiamo la matrice dei coefficienti

B = np.array([9, 8])  #creiamo il vettore dei termini noti

x = np.linalg.solve(A, B)  #risolviamo il sistema lineare

print(x)  #stampiamo le soluzioni -> [2. 3.]


'''
2. TRASFORMATA DI FOURIER - NUMPY.FFT

La trasformata di Fourier discreta (DFT) permette di
analizzare un segnale individuando le frequenze che lo compongono.

np.fft.fft() -> calcola la trasformata di Fourier discreta
attraverso un algoritmo veloce chiamato FFT.

np.fft.fftfreq() -> restituisce le frequenze associate
ai coefficienti della trasformata.

PARAMETRI PRINCIPALI:

np.fft.fft(a)
a -> array contenente il segnale da analizzare.

np.fft.fftfreq(n, d)
n -> numero di campioni del segnale.
d -> intervallo di tempo tra due campioni.
'''


# ESEMPIO 4 - TRASFORMATA DI FOURIER

t = np.linspace(0, 1, 400, endpoint=False)  #creiamo 400 istanti di tempo in un secondo

sig = np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 120 * t)  #creiamo un segnale con frequenze di 50 e 120 Hz

fft_sig = np.fft.fft(sig)  #calcoliamo la trasformata di Fourier del segnale

freqs = np.fft.fftfreq(len(fft_sig), d=1/400)  #calcoliamo le frequenze associate in Hz

print('Trasformata di Fourier:', fft_sig)  #stampiamo i coefficienti della trasformata

print('Frequenze associate:', freqs)  #stampiamo le frequenze

#np.pi rappresenta il valore di pi greco
#np.sin() calcola il seno degli elementi
#la FFT restituisce coefficienti generalmente complessi
#le frequenze principali del segnale sono 50 e 120 Hz


'''
3. BROADCASTING

Il broadcasting è un meccanismo di NumPy che permette
di eseguire operazioni tra array di dimensioni differenti,
purché le loro forme siano compatibili.

Ad esempio, possiamo sommare uno scalare a tutti
gli elementi di un array senza utilizzare un ciclo for.

Uno scalare è un singolo valore numerico.

NumPy tratta automaticamente lo scalare come se fosse
applicato a tutti gli elementi dell'array, senza doverlo
duplicare materialmente in memoria.

Il broadcasting funziona anche tra array di forme diverse,
quando le loro dimensioni rispettano le regole di compatibilità.
'''


# ESEMPIO 5 - BROADCASTING CON UNO SCALARE

arr = np.array([1, 2, 3, 4])  #creiamo un array monodimensionale

scalar = 10  #definiamo un valore scalare

result = arr + scalar  #sommiamo lo scalare a ogni elemento dell'array

print(result)  #stampiamo il risultato -> [11 12 13 14]


# ESEMPIO 6 - BROADCASTING CON UNA MATRICE

matrice = np.array([[1, 2, 3],
                    [4, 5, 6]])  #creiamo una matrice 2x3

valori = np.array([10, 20, 30])  #creiamo un array con 3 elementi

risultato = matrice + valori  #sommiamo i 3 valori a ogni riga della matrice

print(risultato)  #stampiamo la matrice risultante

#RISULTATO:
# [[11 22 33]
#  [14 25 36]]


'''
RIEPILOGO

ALGEBRA LINEARE:
np.linalg.inv() -> inversa di una matrice.
np.linalg.norm() -> norma di un vettore o matrice.
np.linalg.solve() -> soluzione di sistemi lineari.
np.linalg.det() -> determinante.
np.linalg.eig() -> autovalori e autovettori.
np.dot() / np.matmul() -> prodotti tra vettori o matrici.

FOURIER:
np.fft.fft() -> calcola la trasformata di Fourier.
np.fft.fftfreq() -> calcola le frequenze associate.

BROADCASTING:
Permette di eseguire operazioni tra array di forme differenti,
purché compatibili, senza utilizzare cicli espliciti.
'''
