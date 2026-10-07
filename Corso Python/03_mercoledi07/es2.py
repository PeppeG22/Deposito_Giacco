'''ESERCIZIO COMPLETO
   Esercizio su Python: Cicli e Condizioni'''


#PUNTO 1: utilizzo di if
#Scrivi un sistema che prende in input un numero e stampa "Pari"
#se il numero è pari e "Dispari" se il numero è dispari


num = int(input('Inserisci un numero: '))

if num % 2 == 0:  #se il resto della divisione per 2 è uguale a 0
    print('Pari')  #allora il numero è pari

else:  #se la condizione precedente non è vera
    print('Dispari')  #allora il numero è dispari



#PUNTO 2: utilizzo di while e range
#Scrivi un sistema che prende in input un numero intero positivo n
#e stampa tutti i numeri da n a 0 compreso, decrementando di 1.
#Deve potersi ripetere all'infinito.


while True:  #creiamo un ciclo infinito per poter ripetere il programma

    num = int(input('Inserisci un numero intero positivo: '))

    for i in range(num, -1, -1):  #partiamo dal numero inserito e arriviamo fino a 0
        print(i)

    scelta = input('Vuoi ripetere? si/no: ')

    if scelta.lower() == 'no':  #se l'utente scrive no usciamo dal ciclo
        break



#PUNTO 3: utilizzo di for
#Scrivi un sistema che prende in input una lista di numeri
#e stampa il quadrato di ciascun numero nella lista.


lista = []  #creiamo una lista vuota

quantita = int(input('Quanti numeri vuoi inserire nella lista? '))


for i in range(quantita):  #ripetiamo l'inserimento per il numero di volte scelto

    num = int(input('Inserisci un numero: '))

    lista.append(num)  #aggiungiamo il numero alla lista


for num in lista:  #prendiamo uno alla volta tutti i numeri presenti nella lista

    quadrato = num * num  #calcoliamo il quadrato del numero

    print('Il quadrato di', num, 'è', quadrato)



#PUNTO 4: utilizzo di if, while e for insieme
#Scrivi un sistema che prende in input una lista di numeri interi
#che precedentemente è stata valorizzata dall'utente.
#Il sistema deve:
#1. Utilizzare un ciclo for per trovare il numero massimo nella lista.
#2. Utilizzare un ciclo while per contare quanti numeri sono presenti nella lista.
#3. Utilizzare una condizione if per stampare "Lista Vuota" se la lista è vuota,
#   altrimenti stampare il numero massimo trovato e il numero di elementi nella lista.


lista = []  #creiamo una lista vuota

quantita = int(input('Quanti numeri vuoi inserire nella lista? '))


for i in range(quantita):  #facciamo inserire i numeri all'utente

    num = int(input('Inserisci un numero: '))

    lista.append(num)  #aggiungiamo ogni numero alla lista


if len(lista) == 0:  #controlliamo se la lista è vuota

    print('Lista Vuota')

else:

    massimo = lista[0]  #consideriamo inizialmente il primo numero come massimo


    for num in lista:  #controlliamo uno alla volta tutti i numeri della lista

        if num > massimo:  #se troviamo un numero maggiore del massimo

            massimo = num  #il nuovo numero diventa il massimo


    contatore = 0  #inizializziamo il contatore degli elementi


    while contatore < len(lista):  #continuiamo finché non arriviamo alla fine della lista

        contatore += 1  #aumentiamo il contatore di 1 per ogni elemento


    print('Il numero massimo è:', massimo)

    print('I numeri presenti nella lista sono:', contatore)