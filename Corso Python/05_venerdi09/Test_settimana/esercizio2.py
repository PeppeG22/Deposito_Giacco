'''Esercizio: Andare a creare un sistema ripetibile che obblighi l'utente a inserire nome e codice,
               poi l'utente può accedere ad un secondo pezzo del menu, solo se ha inserito i dati nella fase prima e dopo un login (codice == codice e nome == nome)
               questa seconda parte deve permettere di visionare due operazioni, somme e sottrazioni
               e salvare ogni risultato di ogni operazione, entrambi i menu ripetibili (menu: registrazione // login --> dentro login: le due operazioni e visualizza risultati)'''


nome_utente = '' #salviamo i dati per il log-in 
codice = ''
risultati = [] #creiamo una lista per salvare i risultati nell'ultimo menu'


#FUNZIONE REGISTRAZIONE

def registrazione(): #da richiamare quando voglio far registrare l'utente
    
    print('\n Inserisci i tuoi dati: ')
    nome_utente = input('Inserisci nome utente: ')
    codice = int(input('Inserisci il codice con cui accederai al tuo account: '))

    return nome_utente, codice #restituiamo e salviamo i dati inseriti


#FUNZIONE LOGIN

def login(): #richiamare dopo la registrazione 
    
    print('\n Inserisci i tuoi dati: ')
    nome = input('Inserisci nome utente: ')
    password = int(input('Inserisci il codice con cui accederai al tuo account: '))

    if nome == nome_utente and password == codice: #controlliamo se i dati coincidono
        print('Login effettuato! ')
        return True #lo facciamo entrare nel secondo menu'

    else:
        print('Dati non corretti! ')
        return False #facciamo ripetere il ciclo e richiediamo i dati 


#FUNZIONE SOMMA

def somma():
    num1 = int(input('Inserisci il primo numero: ')) #chiediamo i dati all'utente
    num2 = int(input('Inserisci il secondo numero: '))

    risultato = num1 + num2 #sommiamo i numeri

    print('Il risultato della somma è:', risultato) #stampiamo il risultato 

    return risultato #restituiamo il risultato


#FUNZIONE SOTTRAZIONE

def sottrazione():
    num1 = int(input('Inserisci il primo numero: ')) #chiediamo i dati all'utente
    num2 = int(input('Inserisci il secondo numero: '))

    risultato = num1 - num2 #sottraiamo i numeri

    print('Il risultato della sottrazione è:', risultato) #stampiamo il risultato 

    return risultato #restituiamo il risultato


#MENU PRINCIPALE

while True:

    print('\n MENU PRINCIPALE') #creazione del menu' con login e registrazione
    print('1. Registrazione')
    print('2. Login')
    print('3. Esci')

    scelta = input('\n Scegli un operazione: ')

    match scelta: #raccoglie la richiesta in base al menu' 

        case '1': #se abbiamo scelto registrazione
            
            nome_utente, codice = registrazione() #salviamo i dati restituiti
            risultati.clear() #svuotiamo i risultati della registrazione precedente
            print('\n Registrazione effettuata! Ora puoi fare il login.')

        case '2': #se abbiamo scelto login

            if nome_utente == '': #controlliamo se l'utente è registrato
                print('Devi prima registrarti! ')

            else:

                flag = True #creiamo una variabile per ripetere il login

                while flag:
                    flag = not login() #ripetiamo il login finché non è corretto

                print('\n Ora puoi accedere al secondo menu!') #secondo menu' per le successive funzionalità dopo il login 


                #SECONDO MENU

                while True:

                    print('\n  MENU OPERAZIONI')
                    print('1. Somma')
                    print('2. Sottrazione')
                    print('3. Visualizza risultati')
                    print('4. Esci')

                    operazione = input('\n Scegli un operazione: ')

                    match operazione:

                        case '1':
                            
                            risultato = somma() #richiamiamo la funzione somma
                            risultati.append(('Somma', risultato)) #salviamo il risultato

                        case '2':
                            risultato = sottrazione() #richiamiamo la funzione sottrazione
                            risultati.append(('Sottrazione', risultato)) #salviamo il risultato

                        case '3':

                            if len(risultati) == 0: #controlliamo se ci sono risultati
                                print('\n Non ci sono risultati salvati!')

                            else:
                                print('\n STORICO RISULTATI ')

                                for risultato in risultati: #scorriamo la lista
                                    print(risultato[0], ':', risultato[1])

                        case '4':
                            print('\n Uscita dal menu operazioni!')
                            break #torniamo al menu principale

                        case _:
                            print('Operazione non valida!')

        case '3':
            print('\n Programma terminato!')
            break #terminiamo il programma

        case _:
            print('Scelta non valida!')