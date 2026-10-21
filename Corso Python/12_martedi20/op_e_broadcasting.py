
'''
NUMPY - OPERAZIONI VETTORIALI, FUNZIONI MATEMATICHE,
ALGEBRA LINEARE, FOURIER E BROADCASTING
'''

import numpy as np  #importiamo la libreria NumPy


'''
OPERAZIONI VETTORIALI

Le operazioni vettoriali permettono di eseguire calcoli
direttamente sugli elementi di un array, senza utilizzare
necessariamente un ciclo for.

Le operazioni vengono applicate elemento per elemento.

UFUNCS (UNIVERSAL FUNCTIONS)

Le ufuncs sono funzioni universali di NumPy che permettono
di applicare operazioni matematiche a tutti gli elementi
di uno o più array.

Esempi:
np.sin() -> calcola il seno.
np.cos() -> calcola il coseno.
np.exp() -> calcola la funzione esponenziale.
np.sqrt() -> calcola la radice quadrata.

FUNZIONI MATEMATICHE E STATISTICHE

NumPy mette a disposizione funzioni per eseguire operazioni:

- Aritmetiche -> somma, sottrazione, moltiplicazione e divisione.
- Matematiche -> seno, coseno, radici ed esponenziali.
- Statistiche -> media, somma, varianza e deviazione standard.
'''


# ESEMPIO - OPERAZIONI VETTORIALI E UFUNCS

arr = np.array([1, 2, 3, 4])  #creiamo un array di numeri

risultato = arr * 2  #moltiplichiamo ogni elemento dell'array per 2

radice = np.sqrt(arr)  #calcoliamo la radice quadrata di ogni elemento

print(risultato)  #stampiamo l'array moltiplicato -> [2 4 6 8]
print(radice)  #stampiamo le radici quadrate


'''
1. LINSPACE

linspace() permette di generare un numero specifico di valori
distribuiti in maniera uniforme tra un valore iniziale e uno finale.

A differenza di arange(), dove specifichiamo il passo,
con linspace() indichiamo quanti valori vogliamo ottenere.

Il valore finale è incluso per impostazione predefinita.

PARAMETRI:
start -> valore iniziale.
stop -> valore finale.
num -> numero di valori da generare.
endpoint -> indica se includere il valore finale (True di default).
'''


# ESEMPIO - LINSPACE

valori = np.linspace(0, 10, 5)  #generiamo 5 valori equidistanti tra 0 e 10

print(valori)  #stampiamo i valori -> [0. 2.5 5. 7.5 10.]


'''
2. RANDOM

random è un modulo di NumPy che permette di generare
numeri casuali e array contenenti valori casuali.

Possiamo utilizzarlo per simulazioni, esperimenti statistici
e generazione di dati di prova.

FUNZIONI PRINCIPALI:

np.random.randint() -> genera numeri interi casuali.
np.random.rand() -> genera numeri decimali casuali tra 0 e 1.
np.random.random() -> genera numeri decimali casuali tra 0 e 1.
np.random.uniform() -> genera numeri decimali in un intervallo.

PARAMETRI DI RANDINT:
low -> valore minimo incluso.
high -> valore massimo escluso.
size -> quantità o dimensioni dei valori da generare.
'''


# ESEMPIO - RANDOM

numeri_casuali = np.random.randint(1, 11, size=5)  #generiamo 5 numeri interi casuali da 1 a 10

print(numeri_casuali)  #stampiamo i numeri casuali generati


'''
3. SUM

sum() è una funzione che permette di calcolare
la somma di tutti gli elementi presenti in un array.

È utile per eseguire rapidamente operazioni matematiche
senza utilizzare necessariamente un ciclo for.

PARAMETRO:
axis=None -> somma tutti gli elementi.
axis=0 -> somma gli elementi di ogni colonna.
axis=1 -> somma gli elementi di ogni riga.
'''


# ESEMPIO - SUM

numeri = np.array([10, 20, 30, 40])  #creiamo un array di numeri

totale = np.sum(numeri)  #calcoliamo la somma di tutti gli elementi

print('La somma è:', totale)  #stampiamo il risultato -> 100


'''
4. MEAN

mean() è una funzione che permette di calcolare
la media aritmetica degli elementi presenti in un array.

La media viene calcolata dividendo la somma di tutti
i valori per il numero totale degli elementi.

È particolarmente utilizzata nell'analisi statistica.

PARAMETRO:
axis -> permette di calcolare la media per righe o colonne.
'''
#funzione vettoriali: viene applicata a uno piu elementi all' interno del vettore 
#                   : viene 

# ESEMPIO - MEAN

voti = np.array([20, 25, 30, 25])  #creiamo un array contenente alcuni voti

media = np.mean(voti)  #calcoliamo la media aritmetica dei voti

print('La media è:', media)  #stampiamo il risultato -> 25.0


'''
5. STD - DEVIAZIONE STANDARD

std() è una funzione che permette di calcolare
la deviazione standard di un insieme di valori.

La deviazione standard misura quanto i dati
sono dispersi rispetto alla loro media.

Una deviazione standard bassa indica valori vicini alla media,
mentre una deviazione alta indica valori più dispersi.

PARAMETRI:
axis -> permette di calcolarla per righe o colonne.
ddof=0 -> calcolo predefinito della deviazione standard.
ddof=1 -> utilizza la correzione per la stima campionaria.
'''


# ESEMPIO - STD

voti = np.array([20, 25, 30, 25])  #creiamo un array contenente alcuni voti

deviazione = np.std(voti)  #calcoliamo la deviazione standard dei voti

print('Deviazione standard:', deviazione)  #stampiamo il risultato -> circa 3.54


'''
RIEPILOGO - FUNZIONI NUMPY

np.array() -> crea un array NumPy.
ndarray -> rappresenta la struttura degli array NumPy.
dtype -> indica il tipo di dato degli elementi.
shape -> restituisce la forma e le dimensioni dell'array.
np.arange() -> genera una sequenza di numeri con un passo.
reshape() -> modifica la forma di un array.
np.linspace() -> genera valori equidistanti.
np.random -> permette di generare numeri casuali.
np.sum() -> calcola la somma degli elementi.
np.mean() -> calcola la media aritmetica.
np.std() -> calcola la deviazione standard.
'''


# ---------------------------------------------------------------------


'''
NUMPY - ALGEBRA LINEARE, FOURIER E BROADCASTING
'''


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

Il broadcasting è la capacità di NumPy di eseguire
operazioni vettoriali tra array di forme diverse,
facendoli lavorare insieme quando sono compatibili.

Permette di eseguire operazioni elemento per elemento,
senza utilizzare necessariamente un ciclo for.

Il broadcasting rende più semplice, veloce ed efficiente
la scrittura e l'esecuzione del codice.

Uno scalare è un singolo valore numerico.

NumPy può applicare automaticamente uno scalare a tutti
gli elementi di un array, senza duplicarlo fisicamente.


PRINCIPI DEL BROADCASTING

1. ALLINEAMENTO DELLE DIMENSIONI

NumPy confronta le dimensioni dei due array
partendo da destra verso sinistra.

2. ESPANSIONE DELLE DIMENSIONI

Se un array presenta una dimensione uguale a 1,
NumPy può estenderla virtualmente per renderla
compatibile con la dimensione dell'altro array.

3. APPLICAZIONE DELLE OPERAZIONI

Una volta rese compatibili le forme degli array,
NumPy esegue l'operazione elemento per elemento.


REGOLE DEL BROADCASTING

1. AGGIUNGERE DIMENSIONI LEADING

Se gli array hanno un numero diverso di dimensioni,
NumPy considera implicitamente dimensioni iniziali
di grandezza 1 per quello con meno dimensioni.

Esempio:
(3,) diventa virtualmente (1, 3) se confrontato con (2, 3).

2. ALLINEAMENTO DA DESTRA A SINISTRA

Le dimensioni vengono confrontate a partire
dall'ultima, procedendo verso la prima.

3. COMPATIBILITÀ DELLE DIMENSIONI

Due dimensioni sono compatibili quando:
- Sono uguali.
- Almeno una delle due è uguale a 1.

Se queste condizioni non sono rispettate,
l'operazione di broadcasting non è possibile.

4. ESPANSIONE AUTOMATICA

Le dimensioni uguali a 1 vengono considerate
come se fossero estese alla dimensione necessaria.

L'espansione è generalmente virtuale,
quindi non richiede di duplicare tutti i dati.


VANTAGGI DEL BROADCASTING

EFFICIENZA -> evita copie inutili dei dati e cicli espliciti.
VELOCITÀ -> sfrutta le operazioni ottimizzate di NumPy.
SEMPLICITÀ -> permette di scrivere meno codice.

ATTENZIONE:
Non tutti gli array di forme diverse sono compatibili.
'''


# ESEMPIO 5 - BROADCASTING CON UNO SCALARE

arr = np.array([1, 2, 3, 4])  #creiamo un array monodimensionale

scalar = 10  #definiamo un valore scalare

result = arr + scalar  #sommiamo lo scalare a ogni elemento dell'array

print(result)  #stampiamo il risultato -> [11 12 13 14]

#NumPy applica virtualmente il valore 10 a ogni elemento
#senza dover utilizzare un ciclo for


# ESEMPIO 6 - BROADCASTING CON UNA MATRICE

matrice = np.array([[1, 2, 3],
                    [4, 5, 6]])  #creiamo una matrice 2x3

valori = np.array([10, 20, 30])  #creiamo un array con 3 elementi

risultato = matrice + valori  #sommiamo i 3 valori a ogni riga della matrice

print(risultato)  #stampiamo la matrice risultante

#RISULTATO:
# [[11 22 33]
#  [14 25 36]]

#la matrice ha shape (2, 3)
#l'array valori ha shape (3,)
#NumPy considera virtualmente la shape (1, 3)
#la dimensione 1 viene estesa fino a 2
#i tre valori vengono quindi applicati a entrambe le righe


'''
RIEPILOGO FINALE

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

PRINCIPI:
- Allineamento delle dimensioni.
- Espansione delle dimensioni.
- Applicazione delle operazioni.

REGOLE:
- Aggiunta virtuale di dimensioni iniziali uguali a 1.
- Confronto delle dimensioni da destra verso sinistra.
- Dimensioni compatibili se uguali o se una è 1.
- Espansione automatica delle dimensioni compatibili.

VANTAGGI:
- Efficienza.
- Velocità.
- Semplicità.
'''
