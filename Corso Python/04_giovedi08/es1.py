#ESERCIZIO: indovina il numero casuale

import random  #importiamo la libreria random

def randomize():  #creiamo una funzione per iniziare il gioco

    x = random.randint(1, 100)  #generiamo un numero casuale tra 1 e 100

    while True:  #continuiamo finché non indoviniamo

        try:
            num = int(input('Indovina il numero da 1 a 100: '))

        except ValueError:  #se inseriamo lettere invece di numeri
            print('Devi inserire un numero valido')
            continue  #torniamo all'inizio del ciclo

        if 1 <= num <= 100:  #controlliamo che il numero sia valido

            if num > x:  #se il numero è maggiore di quello casuale
                print('Prova con un numero più piccolo')

            elif num < x:  #se il numero è minore di quello casuale
                print('Prova con un numero più grande')

            else:  #se il numero è uguale a quello casuale
                print('Complimenti hai indovinato!')
                break  #terminiamo la partita

        else:  #se il numero è fuori dalla soglia richiesta
            print('Devi inserire un numero da 1 a 100')


#MENU PRINCIPALE

while True:  #chiediamo se l'utente vuole giocare

    scelta = input('Vuoi giocare? si | no \n')

    if scelta.lower() == 'si' or scelta.lower() == 's':
        randomize()  #iniziamo una nuova partita

    elif scelta.lower() == 'no' or scelta.lower() == 'n':
        print('Gioco terminato!')
        break  #usciamo dal programma

    else:  #se la risposta non è valida
        print('Devi rispondere si oppure no')
        
        
#ES 2 - Sequenza di Fibonacci

numeri = [0, 1]  #inseriamo i primi due numeri della sequenza

seq = int(input('Inserisci il numero massimo della sequenza di Fibonacci \n'))

if seq < 0:  #se il numero massimo è negativo
    numeri = []  #la sequenza sarà vuota

elif seq == 0:  #se il numero massimo è zero
    numeri = [0]  #inseriamo soltanto lo zero


while True:  #continuiamo il ciclo finché non superiamo il numero massimo

    if numeri[-1] + numeri[-2] <= seq:  #controlliamo che la somma degli ultimi due numeri non superi il massimo

        new = numeri[-1] + numeri[-2]  #sommiamo l'ultimo e il penultimo numero della lista

        numeri.append(new)  #aggiungiamo il nuovo numero alla lista

    else:  #se la somma supera il numero massimo inserito dall'utente
        break  #interrompiamo il ciclo


print(numeri)  #stampiamo la sequenza completa