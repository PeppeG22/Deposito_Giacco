'''EXTRA: Andare a creare un sistema che gestisca dinamicamente, quindi ripetibile, le liste,
permettendo ad un utente, di modificare aggiungere, rimuovere e visualizzare l'intera lista'''


lista = []

scelta = -1

while scelta != 0:   #continua finché l'utente non sceglie 0

    print('Scegli quale aziene eseguire:')  #stampa menu' iniziale
    print('1 - Aggiungi elemento')
    print('2 - Rimuovi elemento')
    print('3 - Modifica elemento')
    print('4 - Stampa la lista')
    print('0 - Esci')

    scelta = int(input('Inserisci la tua scelta: '))  #raccoglie la scelta del menu'


    #AGGIUNGI ELEMENTO
    if scelta == 1:

        elemento = input('\nInserisci elemento da aggiungere: ')

        lista.append(elemento)

        print('Elemento aggiunto!')


    #RIMUOVI ELEMENTO
    elif scelta == 2:

        elemento = input('Inserisci elemento da rimuovere: ')

        if elemento in lista:

            lista.remove(elemento)

            print('Elemento rimosso!')

        else:

            print('Elemento non presente nella lista!')


    #MODIFICA ELEMENTO
    elif scelta == 3:

        print(lista)

        posizione = int(input('Quale posizione vuoi modificare? '))

        nuovo = input('Inserisci il nuovo elemento: ')

        lista[posizione] = nuovo

        print(lista)


    #STAMPA LISTA
    elif scelta == 4:

        print('\nLista completa:')

        if len(lista) == 0:

            print('La lista è vuota!')

        else:

            for i in range(len(lista)):

                print(i, '-', lista[i])


    #ESCI
    elif scelta == 0:

        print('\nProgramma terminato!')


    #SCELTA NON VALIDA
    else:

        print('\nScelta non valida!')