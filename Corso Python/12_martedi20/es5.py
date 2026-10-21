
import numpy as np  #importiamo la libreria NumPy

matrice = None  #inizializziamo la variabile che conterrà la matrice


# MENU PRINCIPALE - GESTIONE MATRICE NUMPY

while True:  #creiamo un menu ripetibile

    print('1. Creare una nuova matrice')
    print('2. Estrarre la matrice centrale')
    print('3. Trasporre la matrice')
    print('4. Calcolare la somma degli elementi')
    print('5. Esci')

    scelta = int(input('\nScegli un operazione: '))  #chiediamo la scelta all'utente

    match scelta:  #controlliamo la scelta effettuata

        # PUNTO 1 - CREAZIONE DELLA MATRICE

        case 1:  #creiamo una nuova matrice

            righe = int(input('Inserisci il numero di righe: '))  #chiediamo il numero di righe
            colonne = int(input('Inserisci il numero di colonne: '))  #chiediamo il numero di colonne

            if righe > 0 and colonne > 0:  #controlliamo che le dimensioni siano positive

                matrice = np.random.randint(1, 101, size=(righe, colonne))  #creiamo la matrice con numeri casuali tra 1 e 100

                print('\nMatrice creata:\n', matrice)  #stampiamo la matrice generata

                with open('risultati_numpy.txt', 'a') as file:  #apriamo il file in modalità aggiunta
                    file.write(f'\nMatrice creata:\n{matrice}\n')  #salviamo la matrice nel file

            else:  #caso in cui le dimensioni non sono valide
                print('Le dimensioni devono essere maggiori di zero!')  #segnaliamo l'errore


        # PUNTO 2 - ESTRAZIONE DELLA MATRICE CENTRALE

        case 2:  #estraiamo la sottomatrice centrale

            if matrice is not None:  #controlliamo che sia stata creata una matrice

                if matrice.shape[0] >= 3 and matrice.shape[1] >= 3:  #controlliamo che possiamo estrarre una parte centrale

                    centrale = matrice[1:-1, 1:-1]  #escludiamo la prima e l'ultima riga e colonna

                    print('\nMatrice centrale:\n', centrale)  #stampiamo la matrice centrale

                    with open('risultati_numpy.txt', 'a') as file:  #apriamo il file in modalità aggiunta
                        file.write(f'\nMatrice centrale:\n{centrale}\n')  #salviamo la matrice centrale

                else:  #caso in cui la matrice è troppo piccola
                    print('La matrice deve avere almeno 3 righe e 3 colonne!')

            else:  #caso in cui la matrice non esiste
                print('Devi prima creare una matrice!')


        # PUNTO 3 - TRASPOSIZIONE DELLA MATRICE

        case 3:  #trasponiamo la matrice

            if matrice is not None:  #controlliamo che la matrice esista

                matrice = matrice.T  #trasponiamo la matrice scambiando righe e colonne

                print('\nMatrice trasposta:\n', matrice)  #stampiamo la matrice trasposta

                with open('risultati_numpy.txt', 'a') as file:  #apriamo il file in modalità aggiunta
                    file.write(f'\nMatrice trasposta:\n{matrice}\n')  #salviamo la matrice trasposta

            else:  #caso in cui la matrice non esiste
                print('Devi prima creare una matrice!')


        # PUNTO 4 - SOMMA DEGLI ELEMENTI

        case 4:  #calcoliamo la somma di tutti gli elementi

            if matrice is not None:  #controlliamo che la matrice esista

                somma = np.sum(matrice)  #calcoliamo la somma di tutti gli elementi

                print('\nSomma degli elementi:', somma)  #stampiamo la somma totale

                with open('risultati_numpy.txt', 'a') as file:  #apriamo il file in modalità aggiunta
                    file.write(f'\nSomma degli elementi: {somma}\n')  #salviamo la somma nel file

            else:  #caso in cui la matrice non esiste
                print('Devi prima creare una matrice!')


        # PUNTO 5 - USCITA DAL PROGRAMMA

        case 5:  #caso in cui l'utente vuole uscire
            print('Chiusura del programma...')  #stampiamo il messaggio di chiusura
            break  #interrompiamo il ciclo while


        case _:  #caso in cui l'utente inserisce una scelta non valida
            print('Scelta non valida, riprova!')  #segnaliamo la scelta non valida
