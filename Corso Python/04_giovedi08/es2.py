
import random

#EXTRA: UTILIZZARE DECORATORI E GENERATORI

#ESERCIZIO:
#1. chiedi un numero intero positivo, se non lo inserisce richiedere
#2. genera una lista tra 1 e n, la lunghezza è n
#3. usa un for per calcolare e stampare la somma dei pari
#4. usa un for per stampare tutti i dispari
#5. usa un for determinare se un numero è primo, deve restituire True se è primo
#6. usa un for per stampare tutti i primi dalla lista
#7. fai la somma di tutti i numeri e stampa, controlla se è un primo
#8. tutto tramite funzioni nel menu'

#iniziamo creando il menu' per tutti i metodi

scelta = -1  #utilizziamo questa variabile per il menu'

numeri = []  #creiamo una lista vuota


#DECORATORE EXTRA

def decoratore(funzione):  #riceviamo una funzione

    def wrapper():  #creiamo una funzione interna
        print('\n--- Inizio decoratore ---')

        funzione()  #eseguiamo la funzione 

        print('--- Fine decoratore ---\n')

    return wrapper  #restituiamo la funzione interna


#PUNTO 1 E 2 - GENERAZIONE LISTA

def genera_lista():  #funzione per generare la lista

    num = int(input('Inserisci un intero positivo! '))

    while num <= 0:  #continuiamo finché il numero non è positivo
        
        print('Non hai inserito un numero valido!')
        num = int(input('Inserisci un intero positivo! '))

    numeri.clear()  #svuotiamo la lista precedente 

    for i in range(num):  #generiamo n numeri casuali
       
        casuale = random.randint(1, num)  #numero casuale tra 1 e n
        numeri.append(casuale)  #aggiungiamo il numero alla lista

    print('Lista generata:', numeri)


#PUNTO 3 - SOMMA DEI PARI

def sum_pari(numeri):

    somma = 0  #inizializziamo la somma a zero

    for i in numeri: 
        if i % 2 == 0:  #controlliamo se il numero è pari
            somma += i  #aggiungiamo il numero alla somma

    print('La somma dei pari è: ', somma)


#PUNTO 4 - STAMPA DEI DISPARI

def stampa_dispari(numeri):

    dispari = []  #creiamo una lista per i dispari

    for i in numeri:  
        if i % 2 != 0:  #controlliamo se il numero è dispari
            dispari.append(i)  #aggiungiamo il numero come stringa

    print('I dispari sono: ', dispari)  #stampiamo i numeri dispari


#PUNTO 5 - CONTROLLO NUMERO PRIMO

def is_primo(num):

    if num < 2:  #i numeri minori di 2 non sono primi
        return False

    for i in range(2, num):  #controlliamo i divisori del numero
        if num % i == 0:  #se il resto è zero non è primo
            return False

    return True  #se non troviamo divisori il numero è primo


#PUNTO 6 - GENERATORE NUMERI PRIMI

def genera_primi(numeri):  #creiamo un generatore

    for i in numeri:  
        if is_primo(i):  #controlliamo se il numero è primo
            yield i  #restituiamo un numero alla volta


def stampa_primi(numeri):

    primi = []  #creiamo una lista per i numeri primi

    for i in genera_primi(numeri):  #utilizziamo il generatore
        primi.append(str(i))  #aggiungiamo i numeri primi alla lista

    print('I numeri primi sono:', ', '.join(primi))


#PUNTO 7 - SOMMA TOTALE E CONTROLLO PRIMO

def somma_totale(numeri):

    somma = 0  #inizializziamo la somma

    for i in numeri:  #scorriamo tutti i numeri
        somma += i  #aggiungiamo ogni numero alla somma

    print('La somma totale è:', somma)

    if is_primo(somma):  #controlliamo se la somma è un numero primo
        print('La somma è un numero primo!')

    else:
        print('La somma non è un numero primo!')


#PUNTO 8 - MENU PRINCIPALE

@decoratore  #applichiamo il decoratore al menu
def mostra_menu():

    print('Scegli quale azione eseguire:')
    print('1 - Genera lista di numeri casuali')
    print('2 - Somma dei numeri pari')
    print('3 - Stampa numeri dispari')
    print('4 - Stampa numeri primi')
    print('5 - Somma totale e controllo numero primo')
    print('0 - Esci')


while scelta != 0:  #continua finché l'utente non sceglie 0

    mostra_menu()  #richiamiamo la funzione del menu'

    scelta = int(input('Inserisci la tua scelta: '))

    match scelta:

        case 1:
            genera_lista()  #richiamiamo la funzione

        case 2:
            sum_pari(numeri)  #sommiamo i numeri pari

        case 3:
            stampa_dispari(numeri)  #stampiamo i numeri dispari

        case 4:
            stampa_primi(numeri)  #stampiamo tutti i numeri primi

        case 5:
            somma_totale(numeri)  #sommiamo tutti i numeri e controlliamo se è primo

        case 0:
            print('Uscita dal programma!')

        case _:
            print('Scelta non valida!')
