'''ESERCIZIO COMPLETO
   Esercizio su Python: Cicli e Condizioni'''


#PUNTO 1: utilizzo di if
#Scrivi un sistema che prende in input un numero e stampa "Pari"
#se il numero è pari e "Dispari" se il numero è dispari


num1 = int(input('Inserisci un numero: '))

if num1 % 2 == 0:  #se il resto della divisione per 2 è uguale a 0
    print('Pari')  #allora il numero è pari

else:  #se la condizione precedente non è vera
    print('Dispari')  #allora il numero è dispari



#PUNTO 2: utilizzo di while e range
#Scrivi un sistema che prende in input un numero intero positivo n
#e stampa tutti i numeri da n a 0 compreso, decrementando di 1.
#Deve potersi ripetere all'infinito.


while True:  #creiamo un ciclo infinito per poter ripetere il programma

    num2 = int(input('Inserisci un numero intero positivo: '))

    for i2 in range(num2, -1, -1):  #partiamo dal numero inserito e arriviamo fino a 0
        print(i2)

    scelta2 = input('Vuoi ripetere? si/no: ')

    if scelta2.lower() == 'no':  #se l'utente scrive no usciamo dal ciclo
        break



#PUNTO 3: utilizzo di for
#Scrivi un sistema che prende in input una lista di numeri
#e stampa il quadrato di ciascun numero nella lista.


lista3 = []  #creiamo una lista vuota

quantita3 = int(input('Quanti numeri vuoi inserire nella lista? '))


for i3 in range(quantita3):  #ripetiamo l'inserimento per il numero di volte scelto

    num3 = int(input('Inserisci un numero: '))

    lista3.append(num3)  #aggiungiamo il numero alla lista


for num3 in lista3:  #prendiamo uno alla volta tutti i numeri presenti nella lista

    quadrato3 = num3 * num3  #calcoliamo il quadrato del numero

    print('Il quadrato di', num3, 'è', quadrato3)



#PUNTO 4: utilizzo di if, while e for insieme
#Scrivi un sistema che prende in input una lista di numeri interi
#che precedentemente è stata valorizzata dall'utente.
#Il sistema deve:
#1. Utilizzare un ciclo for per trovare il numero massimo nella lista.
#2. Utilizzare un ciclo while per contare quanti numeri sono presenti nella lista.
#3. Utilizzare una condizione if per stampare "Lista Vuota" se la lista è vuota,
#   altrimenti stampare il numero massimo trovato e il numero di elementi nella lista.


lista4 = []  #creiamo una lista vuota

quantita4 = int(input('Quanti numeri vuoi inserire nella lista? '))


for i4 in range(quantita4):  #facciamo inserire i numeri all'utente

    num4 = int(input('Inserisci un numero: '))

    lista4.append(num4)  #aggiungiamo ogni numero alla lista


if len(lista4) == 0:  #controlliamo se la lista è vuota

    print('Lista Vuota')

else:

    massimo4 = lista4[0]  #consideriamo inizialmente il primo numero come massimo


    for num4 in lista4:  #controlliamo uno alla volta tutti i numeri della lista

        if num4 > massimo4:  #se troviamo un numero maggiore del massimo

            massimo4 = num4  #il nuovo numero diventa il massimo


    contatore4 = 0  #inizializziamo il contatore degli elementi


    while contatore4 < len(lista4):  #continuiamo finché non arriviamo alla fine della lista

        contatore4 += 1  #aumentiamo il contatore di 1 per ogni elemento


    print('Il numero massimo è:', massimo4)

    print('I numeri presenti nella lista sono:', contatore4)