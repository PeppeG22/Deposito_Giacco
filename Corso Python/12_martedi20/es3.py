
'''
ESERCIZIO 2 - NUMPY: LINSPACE, RANDOM E SUM

1. Creare un array di 50 numeri equidistanti tra 0 e 10.
2. Creare un array di 50 numeri casuali tra 0 e 1.
3. Sommare i due array elemento per elemento.
4. Calcolare la somma totale del nuovo array.
5. Calcolare la somma degli elementi maggiori di 5.
6. Stampare gli array originali, quello risultante e le somme.
7. Salvare i risultati su un file TXT a ogni esecuzione.
8. Rendere ripetibile il processo attraverso un ciclo while.
9. Chiedere all'utente se vuole sovrascrivere il file TXT.

'''

import numpy as np  #importiamo la libreria NumPy


# MENU PRINCIPALE - ESERCIZIO NUMPY

while True:  #creiamo un menu ripetibile

    print('\n--- ESERCIZIO NUMPY ---')  #stampiamo il titolo del programma
    print('1. Esegui esercizio')  #opzione per eseguire le operazioni
    print('0. Esci')  #opzione per uscire dal programma

    scelta = int(input('\nInserisci la tua scelta: '))  #chiediamo la scelta all'utente

    match scelta:  #controlliamo la scelta effettuata

        case 1:  #eseguiamo tutte le operazioni dell'esercizio

            # PUNTO 1 - CREAZIONE ARRAY CON LINSPACE

            arr1 = np.linspace(0, 10, 50)  #generiamo 50 numeri equidistanti tra 0 e 10


            # PUNTO 2 - CREAZIONE ARRAY CASUALE

            arr2 = np.random.random(50)  #generiamo 50 numeri casuali tra 0 e 1


            # PUNTO 3 - SOMMA DEGLI ARRAY

            nuovo_arr = arr1 + arr2  #sommiamo i due array elemento per elemento


            # PUNTO 4 - SOMMA TOTALE

            somma_totale = np.sum(nuovo_arr)  #calcoliamo la somma di tutti gli elementi


            # PUNTO 5 - SOMMA DEI VALORI MAGGIORI DI 5

            maggiori_5 = nuovo_arr[nuovo_arr > 5]  #selezioniamo gli elementi maggiori di 5

            somma_maggiori = np.sum(maggiori_5)  #calcoliamo la somma degli elementi selezionati


            # PUNTO 6 - STAMPA DEI RISULTATI

            print('\nPrimo array:\n', arr1)  #stampiamo il primo array

            print('\nSecondo array:\n', arr2)  #stampiamo il secondo array

            print('\nArray risultante:\n', nuovo_arr)  #stampiamo l'array ottenuto dalla somma

            print('\nSomma totale:', somma_totale)  #stampiamo la somma totale

            print('\nElementi maggiori di 5:\n', maggiori_5)  #stampiamo gli elementi maggiori di 5

            print('\nSomma elementi maggiori di 5:', somma_maggiori)  #stampiamo la somma parziale


            # PUNTO 9 - SCELTA DELLA MODALITÀ DI SALVATAGGIO

            while True:  #creiamo un ciclo per controllare la risposta dell'utente

                risposta = input('\nVuoi sovrascrivere il file TXT? (s/n): ').lower()  #chiediamo se vuole sovrascrivere il file

                if risposta == 's':  #caso in cui l'utente vuole sovrascrivere il file

                    modalita = 'w'  #impostiamo la modalità di scrittura
                    break  #interrompiamo il ciclo dopo una risposta valida

                elif risposta == 'n':  #caso in cui l'utente vuole mantenere il contenuto precedente

                    modalita = 'a'  #impostiamo la modalità aggiunta
                    break  #interrompiamo il ciclo dopo una risposta valida

                else:  #caso in cui l'utente inserisce una risposta non valida

                    print('Risposta non valida, inserisci s oppure n!')  #chiediamo di riprovare


            # PUNTO 7 - SALVATAGGIO DEI RISULTATI SU FILE TXT

            with open('risultati_numpy.txt', modalita) as file:  #apriamo il file con la modalità scelta dall'utente

                file.write('\n--- NUOVA ESECUZIONE ---\n')  #separiamo i risultati delle varie esecuzioni

                file.write(f'Primo array:\n{arr1}\n')  #salviamo il primo array

                file.write(f'Secondo array:\n{arr2}\n')  #salviamo il secondo array

                file.write(f'Array risultante:\n{nuovo_arr}\n')  #salviamo il nuovo array

                file.write(f'Somma totale: {somma_totale}\n')  #salviamo la somma totale

                file.write(f'Elementi maggiori di 5:\n{maggiori_5}\n')  #salviamo gli elementi maggiori di 5

                file.write(f'Somma elementi maggiori di 5: {somma_maggiori}\n')  #salviamo la somma parziale

            print('\nRisultati salvati correttamente!')  #confermiamo il salvataggio del file


        case 0:  #caso in cui l'utente vuole uscire dal programma

            print('Chiusura del programma...')  #stampiamo il messaggio di chiusura
            break  #interrompiamo il ciclo principale


        case _:  #caso in cui l'utente inserisce una scelta non valida

            print('Scelta non valida, riprova!')  #segnaliamo la scelta non valida
