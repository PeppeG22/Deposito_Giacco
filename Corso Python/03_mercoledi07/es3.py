


while True:  #EXTRA

    print('Scegli quale esercizio eseguire:') #creazione menu'
    print('1 - Somma numeri')
    print('2 - Stampa parola lettera per lettera')
    print('3 - Crea lista con range')
    print('0 - Esci')

    scelta = int(input('Inserisci la tua scelta: ')) #raccoglie la scelta del menu'


    #es 1

    if scelta == 1:

        sum = 0 #inseriamo tutti i valori inseriti dall'utente

        while True:

            num = int(input('Inserisci il numero che vuoi sommare ')) #raccogliamo il valore dell'utente

            sum += num #sommiamo il nuovo numero inserito con quello nella variabile sum

            if num == 0: #blocchiamo il ciclo quando viene inserito 0

                print(sum)

                break


    #----------------------------------------------------------------------------------------


    #es2

    elif scelta == 2:

        testo = input('Inserisci una parola ') #raccolta la parola inserita da utente

        for i in testo: #prendiamo ogni lettera dal testo

            print(i) #stampiamo ogni lettera che raccoglie


    #----------------------------------------------------------------------------------------


    #es3

    elif scelta == 3:

        numeri = [] #inizializziamo la lista iniziale

        scelta1 = int(input('Scegli il numero massimo della tua lista: ')) #sarà il nostro stop

        scelta2 = int(input('Scegli lo step della tua lista: ')) #sarà il nostro step

        numeri = list(range(0, scelta1, scelta2)) #START - STOP - STEP

        print(numeri)


    #----------------------------------------------------------------------------------------


    elif scelta == 0:   #terminiamo il while iniziale, usciamo dal menu'

        print('Programma terminato')

        break


    else:

        print('Scelta non valida') #nel caso in cui non si scelga un numero