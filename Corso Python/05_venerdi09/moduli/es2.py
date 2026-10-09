
#ALLA SCOPERTA DI PYTHON

list = []  #creiamo una lista vuota

#creiamo una funzione per salutare l'utente
def saluta(nome):
    ciao = f"Ciao, {nome}"  #creiamo una stringa con il nome ricevuto
    return ciao  #restituiamo il risultato della funzione


while True:  #menu ripetibile finché l'utente non decide di uscire

    #stampiamo il menu principale
    print('\n--------------------------- \n')
    print('\nALLA SCOPERTA DI PYTHON \n')
    print('1. Introduzione a Hello World ')
    print('2. Variabili')
    print('3. Collezioni')
    print('4. Controllo del flusso')
    print('5. Funzioni')
    print('6. Coming soon! ')
    print('0. Esci')

    scelta = int(input('\nScegli un argomento: '))  #prendiamo la scelta dell'utente

    match scelta:  #controlliamo il numero scelto dall'utente

        case 0:  #caso in cui usciamo dal menu principale
            print('Programma terminato!')
            break  #interrompiamo il ciclo while

        case 1:  #l'utente sceglie il numero 1 del menu
            print('Python è un linguaggio di programmazione di alto livello, interpretato, dinamico e orientato agli oggetti.')

        case 2:  #l'utente sceglie il numero 2 del menu
            print("\nUna variabile è un nome utilizzato per fare riferimento a un valore all'interno di un programma.")

        case 3:  #l'utente sceglie le collezioni
            print('Le liste sono collezioni che permettono di raggruppare più elementi sotto un unico nome.')

            num = 0  #inizializziamo la variabile

            while True:  #creiamo un ciclo per inserire più numeri

                scelta2 = input('Vuoi inserire un numero nella lista? si|no ')  #chiediamo se vuole continuare

                if scelta2.lower() == 'si':  #controlliamo se l'utente ha risposto si

                    num = int(input('Inserisci un numero nella tua lista: '))  #prendiamo il numero
                    list.append(num)  #aggiungiamo il numero alla lista

                else:  #se l'utente non vuole inserire altri numeri
                    print(list)  #stampiamo la lista completa
                    break  #interrompiamo il ciclo interno

        case 4:  #l'utente sceglie i controllori del flusso

            print("I controllori del flusso permettono di gestire l'esecuzione di un programma, decidendo quali istruzioni eseguire, in quale ordine e quante volte.")

            #stampiamo il secondo menu
            print('\n--- CONTROLLORI DEL FLUSSO ---')
            print('1. Ciclo While ')
            print('2. Ciclo For ')
            print('3. If/else ')
            print('4. Match - Case ')

            scelta3 = int(input('\nScegli cosa vuoi approfondire: '))  #prendiamo la scelta come numero intero

            match scelta3:  #controlliamo quale argomento vuole approfondire

                case 1:  #l'utente sceglie il ciclo while
                    print('Il ciclo while ripete un blocco di codice finché la sua condizione è vera (True). La condizione viene controllata prima di ogni iterazione.')

                case 2:  #l'utente sceglie il ciclo for
                    print('Il ciclo for permette di iterare, cioè passare attraverso gli elementi di una sequenza, come una lista o una stringa, eseguendo un blocco di codice per ogni elemento.')

                case 3:  #l'utente sceglie if/else
                    print("La parola chiave if permette di eseguire un blocco di codice soltanto se una condizione è vera (True). Else permette di specificare un blocco alternativo, eseguito quando la condizione dell'if è falsa (False).")

                case 4:  #l'utente sceglie match-case
                    print('Match permette di confrontare un valore con diversi casi, definiti attraverso case. È utile quando bisogna gestire diverse possibilità per uno stesso valore.')

                case _:  #se l'utente inserisce un numero non presente
                    print('Scelta non corretta! ')

        case 5:  #l'utente sceglie le funzioni

            print('In Python si utilizza la parola chiave def per definire una funzione. \n')

            print(saluta('Mirko'))  #richiamiamo la funzione e stampiamo il risultato restituito

        case 6:  #argomento non ancora disponibile
            print('Coming soon! ')

        case _:  #nel caso in cui l'utente non scelga un numero del menu
            print('Scelta non corretta! ')
