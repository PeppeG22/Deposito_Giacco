#esercizio 1 : scrivi un programma che chieda all'utente l'età, poi stampare un messaggio in base all'eta per il film.
#esercizio 2 : fare una calcolatrice, con particolare attenzione alla divisione per 0


#ES 1

eta = int(input("Quanti anni hai? ")) #facciamo inserire l'età dell'utente

match eta: #usiamo il match per confrontare l'età dell'utente con i casi possibili

    case eta if eta < 18: #caso in cui l'utente è minorenne

        print("Non puoi vedere il film, sei minorenne!\n")

    case eta if eta >= 18: #caso in cui l'utente è maggiorenne

        print("Puoi vedere il film, sei maggiorenne!\n")


#-----------------------------------------------------------------------

#ES 2

num1 = float(input("Inserisci il primo numero: ")) #facciamo inserire il primo numero

num2 = float(input("Inserisci il secondo numero: ")) #facciamo inserire il secondo numero

operazione = input("Inserisci l'operazione (+, -, *, /): ") #facciamo inserire l'operazione


match operazione:

    case "+": #caso in cui l'operazione è somma

        risultato = num1 + num2

        print("Il risultato della somma è:", risultato, "\n")


    case "-": #caso in cui l'operazione è sottrazione

        risultato = num1 - num2

        print("Il risultato della sottrazione è:", risultato, "\n")


    case "*": #caso in cui l'operazione è moltiplicazione

        risultato = num1 * num2

        print("Il risultato della moltiplicazione è:", risultato, "\n")


    case "/": #caso in cui l'operazione è divisione

        if num2 != 0: #controlliamo che il secondo numero sia diverso da 0

            risultato = num1 / num2

            print("Il risultato della divisione è:", risultato, "\n")

        else:

            print("Errore: Divisione per zero non consentita.\n")
    
    case _: #caso in cui l'utente non inserisca un operatore matematico
        
        print('Operazione non permessa!')
        
    


