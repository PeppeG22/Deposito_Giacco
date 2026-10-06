#CREO UN IF CHE PRENDE IN INPUT UN VALORE 

print("Benvenuto alla macchinetta del caffè!") #stampo un messaggio di benvenuto

bevanda = int(input("1. caffè / 2. te / 3. cappuccino: ")) #prendo in input un numero intero
zucchero = int(input("Quanti zuccheri vuoi? (0-3 bustine): ")) #prendo in input un numero intero
bicchiere = int(input("Che tipo di bicchiere vuoi? 1. vetro / 2. plastica: / 3. carta: ")) #prendo in input un numero intero


if bevanda == 1: #SE ABBIAMO SCELTO IL NUMERO 1---------------------------->
    print("Hai scelto il caffè") #stampo un messaggio
    if zucchero == 0: #se lo zucchero è uguale a 0
        print("Hai scelto senza zucchero") #stampo un messaggio
        if bicchiere == 1: #se il bicchiere è uguale a 1
            print("Hai scelto il bicchiere di vetro") #stampo un messaggio
        elif bicchiere == 2: #se il bicchiere è uguale a 2
            print("Hai scelto il bicchiere di plastica") #stampo un messaggio
        elif bicchiere == 3: #se il bicchiere è uguale a
             print("Hai scelto il bicchiere di carta") #stampo un messaggio
        else: #se il bicchiere non è uguale a nessuno dei valori precedenti
            print("Scelta non valida per il bicchiere") #stampo un messaggio
    elif zucchero == 1: #se lo zucchero è uguale a 1
        print("Hai scelto con 1 bustina di zucchero") #stampo un messaggio
        if bicchiere == 1: #se il bicchiere è uguale a 1
            print("Hai scelto il bicchiere di vetro") #stampo un messaggio
        elif bicchiere == 2: #se il bicchiere è uguale a 2
            print("Hai scelto il bicchiere di plastica") #stampo un messaggio
        elif bicchiere == 3: #se il bicchiere è uguale a 3
            print("Hai scelto il bicchiere di carta") #stampo un messaggio
        else: #se il bicchiere non è uguale a nessuno dei valori precedenti
            print("Scelta non valida per il bicchiere") #stampo un messaggio
    elif zucchero == 2: #se lo zucchero è uguale a 2
        print("Hai scelto con 2 bustine di zucchero") #stampo un messaggio
        if bicchiere == 1: #se il bicchiere è uguale a 1
            print("Hai scelto il bicchiere di vetro") #stampo un messaggio
        elif bicchiere == 2: #se il bicchiere è uguale a 2
            print("Hai scelto il bicchiere di plastica") #stampo un messaggio
        elif bicchiere == 3: #se il bicchiere è uguale a 3
            print("Hai scelto il bicchiere di carta") #stampo un messaggio
        else: #se il bicchiere non è uguale a nessuno dei valori precedenti
            print("Scelta non valida per il bicchiere") #stampo un messaggio
    elif zucchero == 3: #se lo zucchero è uguale a 3
        print("Hai scelto con 3 bustine di zucchero") #stampo un messaggio
        if bicchiere == 1: #se il bicchiere è uguale a 1
            print("Hai scelto il bicchiere di vetro") #stampo un messaggio
        elif bicchiere == 2: #se il bicchiere è uguale a 2
            print("Hai scelto il bicchiere di plastica") #stampo un messaggio
        elif bicchiere == 3: #se il bicchiere è uguale a 3
            print("Hai scelto il bicchiere di carta") #stampo un messaggio
        else: #se il bicchiere non è uguale a nessuno dei valori precedenti
            print("Scelta non valida per il bicchiere") #stampo un messaggio
    else: #se lo zucchero non è uguale a nessuno dei valori precedenti
        print("Scelta non valida per lo zucchero") #stampo un messaggio
elif bevanda == 2: #SE ABBIAMO SCELTO IL NUMERO 2---------------------------->
    print("Hai scelto il caffè") #stampo un messaggio
    if zucchero == 0: #se lo zucchero è uguale a 0
        print("Hai scelto senza zucchero") #stampo un messaggio
        if bicchiere == 1: #se il bicchiere è uguale a 1
            print("Hai scelto il bicchiere di vetro") #stampo un messaggio
        elif bicchiere == 2: #se il bicchiere è uguale a 2
            print("Hai scelto il bicchiere di plastica") #stampo un messaggio
        elif bicchiere == 3: #se il bicchiere è uguale a
             print("Hai scelto il bicchiere di carta") #stampo un messaggio
        else: #se il bicchiere non è uguale a nessuno dei valori precedenti
            print("Scelta non valida per il bicchiere") #stampo un messaggio
    elif zucchero == 1: #se lo zucchero è uguale a 1
        print("Hai scelto con 1 bustina di zucchero") #stampo un messaggio
        if bicchiere == 1: #se il bicchiere è uguale a 1
            print("Hai scelto il bicchiere di vetro") #stampo un messaggio
        elif bicchiere == 2: #se il bicchiere è uguale a 2
            print("Hai scelto il bicchiere di plastica") #stampo un messaggio
        elif bicchiere == 3: #se il bicchiere è uguale a 3
            print("Hai scelto il bicchiere di carta") #stampo un messaggio
        else: #se il bicchiere non è uguale a nessuno dei valori precedenti
            print("Scelta non valida per il bicchiere") #stampo un messaggio
    elif zucchero == 2: #se lo zucchero è uguale a 2
        print("Hai scelto con 2 bustine di zucchero") #stampo un messaggio
        if bicchiere == 1: #se il bicchiere è uguale a 1
            print("Hai scelto il bicchiere di vetro") #stampo un messaggio
        elif bicchiere == 2: #se il bicchiere è uguale a 2
            print("Hai scelto il bicchiere di plastica") #stampo un messaggio
        elif bicchiere == 3: #se il bicchiere è uguale a 3
            print("Hai scelto il bicchiere di carta") #stampo un messaggio
        else: #se il bicchiere non è uguale a nessuno dei valori precedenti
            print("Scelta non valida per il bicchiere") #stampo un messaggio
    elif zucchero == 3: #se lo zucchero è uguale a 3
        print("Hai scelto con 3 bustine di zucchero") #stampo un messaggio
        if bicchiere == 1: #se il bicchiere è uguale a 1
            print("Hai scelto il bicchiere di vetro") #stampo un messaggio
        elif bicchiere == 2: #se il bicchiere è uguale a 2
            print("Hai scelto il bicchiere di plastica") #stampo un messaggio
        elif bicchiere == 3: #se il bicchiere è uguale a 3
            print("Hai scelto il bicchiere di carta") #stampo un messaggio
        else: #se il bicchiere non è uguale a nessuno dei valori precedenti
            print("Scelta non valida per il bicchiere") #stampo un messaggio
    else: #se lo zucchero non è uguale a nessuno dei valori precedenti
        print("Scelta non valida per lo zucchero") #stampo un messaggio
elif bevanda == 3: #SE ABBIAMO SCELTO IL NUMERO 3---------------------------->
    print("Hai scelto il caffè") #stampo un messaggio
    if zucchero == 0: #se lo zucchero è uguale a 0
        print("Hai scelto senza zucchero") #stampo un messaggio
        if bicchiere == 1: #se il bicchiere è uguale a 1
            print("Hai scelto il bicchiere di vetro") #stampo un messaggio
        elif bicchiere == 2: #se il bicchiere è uguale a 2
            print("Hai scelto il bicchiere di plastica") #stampo un messaggio
        elif bicchiere == 3: #se il bicchiere è uguale a
             print("Hai scelto il bicchiere di carta") #stampo un messaggio
        else: #se il bicchiere non è uguale a nessuno dei valori precedenti
            print("Scelta non valida per il bicchiere") #stampo un messaggio
    elif zucchero == 1: #se lo zucchero è uguale a 1
        print("Hai scelto con 1 bustina di zucchero") #stampo un messaggio
        if bicchiere == 1: #se il bicchiere è uguale a 1
            print("Hai scelto il bicchiere di vetro") #stampo un messaggio
        elif bicchiere == 2: #se il bicchiere è uguale a 2
            print("Hai scelto il bicchiere di plastica") #stampo un messaggio
        elif bicchiere == 3: #se il bicchiere è uguale a 3
            print("Hai scelto il bicchiere di carta") #stampo un messaggio
        else: #se il bicchiere non è uguale a nessuno dei valori precedenti
            print("Scelta non valida per il bicchiere") #stampo un messaggio
    elif zucchero == 2: #se lo zucchero è uguale a 2
        print("Hai scelto con 2 bustine di zucchero") #stampo un messaggio
        if bicchiere == 1: #se il bicchiere è uguale a 1
            print("Hai scelto il bicchiere di vetro") #stampo un messaggio
        elif bicchiere == 2: #se il bicchiere è uguale a 2
            print("Hai scelto il bicchiere di plastica") #stampo un messaggio
        elif bicchiere == 3: #se il bicchiere è uguale a 3
            print("Hai scelto il bicchiere di carta") #stampo un messaggio
        else: #se il bicchiere non è uguale a nessuno dei valori precedenti
            print("Scelta non valida per il bicchiere") #stampo un messaggio
    elif zucchero == 3: #se lo zucchero è uguale a 3
        print("Hai scelto con 3 bustine di zucchero") #stampo un messaggio
        if bicchiere == 1: #se il bicchiere è uguale a 1
            print("Hai scelto il bicchiere di vetro") #stampo un messaggio
        elif bicchiere == 2: #se il bicchiere è uguale a 2
            print("Hai scelto il bicchiere di plastica") #stampo un messaggio
        elif bicchiere == 3: #se il bicchiere è uguale a 3
            print("Hai scelto il bicchiere di carta") #stampo un messaggio
        else: #se il bicchiere non è uguale a nessuno dei valori precedenti
            print("Scelta non valida per il bicchiere") #stampo un messaggio
    else: #se lo zucchero non è uguale a nessuno dei valori precedenti
        print("Scelta non valida per lo zucchero") #stampo un messaggio
        
#ESERCIZIO 2 

#CREAZIONE DI MENU CRUD BASILARE

crud = int(input("Che azione vuoi fare? 1. aggiungi / 2. modifica / 3. elimina: ")) #prendo in input una scelta
num = [1,2,3,5,6,7,8,9] #creo una lista di numeri

if crud == 1: #SE ABBIAMO SCELTO IL NUMERO 1 - AGGIUNGI---------------------------->
    print("Hai scelto di aggiungere un elemento")
    elemento = int(input("Che elemento vuoi aggiungere? ")) #prendo in input un numero intero
    num.append(elemento) #aggiungo l'elemento alla lista
    print("La lista aggiornata è: ", num) #stampo la lista aggiornata

elif crud == 2: #SE ABBIAMO SCELTO IL NUMERO 2 - MODIFICA---------------------------->
    print("Hai scelto di modificare un elemento")
    elemento = int(input("Che elemento vuoi modificare? ")) #prendo in input un numero intero
    if elemento in num: #se l'elemento è nella lista
        elemento_nuovo = int(input("Che elemento vuoi inserire al suo posto? ")) #prendo in input un numero intero
        indice = num.index(elemento) #prendo l'indice dell'elemento da modificare
        num[indice] = elemento_nuovo #modifico l'elemento
        print("La lista aggiornata è: ", num) #stampo la lista aggiornata
        
    else: #se l'elemento non è nella lista
        print("Elemento non trovato nella lista") #stampo un messaggio

elif crud == 3: #SE ABBIAMO SCELTO IL NUMERO 3 - ELIMINA---------------------------->
    print("Hai scelto di eliminare un elemento")
    elemento = int(input("Che elemento vuoi eliminare? ")) #prendo in input un numero intero
    if elemento in num: #se l'elemento è nella lista
        num.remove(elemento) #elimino l'elemento dalla lista
        print("La lista aggiornata è: ", num) #stampo la lista aggiornata
    else: #se l'elemento non è nella lista
        print("Elemento non trovato nella lista") #stampo un messaggio

else: #se l'azione non è valida
    print("Azione non valida") #stampo un messaggio
    
