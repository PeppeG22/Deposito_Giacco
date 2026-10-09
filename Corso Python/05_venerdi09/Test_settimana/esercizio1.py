'''Esercizio: Andare a creare un sistema ripetibile che permetta di inserire: sia al fondo
              che nella posizione che vogliamo noi, modificare, stampare ed eliminare liste,
              che sono divise dal tipo che viene scelto.'''


numeri = [] #creiamo una lista per i numeri
parole = [] #creiamo una lista per le parole


while True:

    print('\n MENU PRINCIPALE') #menu' principale che userò per entrambi gli esercizi 
    print('1. Lista numeri')
    print('2. Lista parole')
    print('3. Esci')

    scelta = input('\n Scegli la lista su cui lavorare: ') #raccogliamo la scelta del menu'

    match scelta:

        case '1':
            lista = numeri #selezioniamo la lista numeri

        case '2':
            lista = parole #selezioniamo la lista parole

        case '3':
            print('Programma terminato!')
            break #terminiamo il programma

        case _:
            print('Scelta non valida!')
            continue #torniamo al menu principale


    #MENU OPERAZIONI

    while True:

        print('\n MENU OPERAZIONI') #menù per inserire tutte le funzioni 
        print('1. Aggiungi elemento in fondo')
        print('2. Inserisci elemento in una posizione')
        print('3. Modifica elemento')
        print('4. Stampa lista')
        print('5. Elimina elemento')
        print('6. Svuota lista')
        print('7. Torna al menu principale')

        operazione = input('\n Scegli un operazione: ')

        match operazione:

            case '1':
                valore = input('Inserisci il valore da aggiungere: ')

                if scelta == '1':
                    valore = int(valore) #convertiamo il valore in numero

                lista.append(valore) #aggiungiamo il valore in fondo
                print('Elemento aggiunto!')


            case '2':
                valore = input('Inserisci il valore da aggiungere: ')

                if scelta == '1':
                    valore = int(valore) #convertiamo il valore in numero

                posizione = int(input('Inserisci la posizione: '))

                if 0 <= posizione <= len(lista):
                    lista.insert(posizione, valore) #inseriamo il valore nella posizione scelta
                    print('Elemento inserito!')

                else:
                    print('Posizione non valida!')


            case '3':
                print('Lista attuale:', lista)

                posizione = int(input('Quale posizione vuoi modificare? ')) #modifica in base alla posizione scelta

                if 0 <= posizione < len(lista):
                    valore = input('Inserisci il nuovo valore: ')

                    if scelta == '1':
                        valore = int(valore) #convertiamo il valore in numero

                    lista[posizione] = valore #modifichiamo il valore nella posizione scelta
                    print('Elemento modificato!')

                else:
                    print('Posizione non valida!')


            case '4':
                print('\n La lista contiene:', lista) #stampiamo la lista selezionata


            case '5':
                print('Lista attuale:', lista)

                posizione = int(input('Quale posizione vuoi eliminare? ')) #elimina in base alla posizione scelta

                if 0 <= posizione < len(lista):
                    lista.pop(posizione) #eliminiamo l'elemento nella posizione scelta
                    print('Elemento eliminato!')

                else:
                    print('Posizione non valida!') #nel caso in cui si scelga una posizione non presente


            case '6':
                lista.clear() #svuotiamo completamente la lista
                print('Lista svuotata!')


            case '7':
                print('Ritorno al menu principale!')
                break #usciamo dal secondo menu


            case _:
                print('Operazione non valida!')