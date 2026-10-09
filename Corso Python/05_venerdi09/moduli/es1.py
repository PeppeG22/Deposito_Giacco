
#MENU CON OPERAZIONI
#richiamiamo le funzioni dal modulo importato 

import utility as ty

while True: #menu ripetibile ->

    print('\n MENU CALCOLATRICE')
    print('1. Somma')
    print('2. Sottrazione')
    print('3. Moltiplicazione')
    print('4. Divisione')
    print('0. Esci')

    scelta = input('\n Scegli un operazione: ') #prendiamo la scelta dell'utente

    if scelta == '0': #controlliamo se l'utente vuole uscire
        print('Programma terminato!')
        break #interrompiamo il ciclo

    elif scelta in ['1', '2', '3', '4']: #controlliamo che la scelta sia valida

        n1 = float(input('Inserisci il primo numero: ')) #richiesta numeri da calcolare
        n2 = float(input('Inserisci il secondo numero: '))

        match scelta: #controlliamo quale operazione eseguire in base a -scelta- 

            case '1': #richiamiamo somma da utility
                risultato = ty.somma(n1, n2) #richiamiamo la funzione 
                print('Il risultato della somma è:', risultato)

            case '2': #richiamiamo sottrazione da utility
                risultato = ty.sottrazione(n1, n2) #richiamiamo la funzione 
                print('Il risultato della sottrazione è:', risultato)

            case '3': #richiamiamo moltiplicazione da utility
                risultato = ty.moltiplicazione(n1, n2) #richiamiamo la funzione 
                print('Il risultato della moltiplicazione è:', risultato)

            case '4': #richiamiamo divisione da utility
                risultato = ty.divisione(n1, n2) #richiamiamo la funzione 

                if risultato != None: #controlliamo che la divisione sia valida
                    print('Il risultato della divisione è:', risultato)

    else:
        print('Operazione non valida!') #in caso in cui non scelga un operazione inserita