
'''
ESERCIZIO - GESTIONE DEI FILE IN PYTHON

Creare un sistema che permetta di gestire le principali operazioni
di input/output sui file, utilizzando le funzioni studiate.

Il sistema deve permettere all'utente di:

1. CREARE UN FILE

2. MODIFICARE UN FILE
   
3. LEGGERE UN FILE
   
4. SVUOTARE UN FILE
 
EXTRA:
Permettere all'utente di scegliere autonomamente il nome del file
su cui effettuare le operazioni.
'''


# PUNTO 1 - CREAZIONE DI UN FILE + EXTRA

def crea_file():  #funzione per creare un nuovo file

    nuovo_nome = input('Inserisci il nome del file che vuoi creare: ')  #chiediamo all'utente il nome del file

    file = open(nuovo_nome + '.txt', 'x')  #creiamo il file in modalità x, aggiungendo l'estensione txt
    file.close()  #chiudiamo il file dopo averlo creato

    print('File creato correttamente!')  #confermiamo la creazione del file


# PUNTO 2 - MODIFICA DI UN FILE

def modifica_file():  #funzione per modificare il contenuto di un file

    nome_file = input('Inserisci il nome del file che vuoi modificare: ')  #chiediamo il nome del file da modificare

    with open(nome_file + '.txt', 'a') as file:  #apriamo il file in modalità aggiunta utilizzando with

        nuova_riga = input('Inserisci quello che vuoi aggiungere: ')  #chiediamo all'utente il nuovo contenuto
        file.write('\n' + nuova_riga)  #aggiungiamo il contenuto andando a capo senza cancellare il precedente

    print('File modificato!')  #confermiamo la modifica del file


# PUNTO 3 - LETTURA DI UN FILE

def leggi_file():  #funzione per leggere il contenuto di un file

    nome_file = input('Inserisci il nome del file che vuoi leggere: ')  #chiediamo il nome del file

    with open(nome_file + '.txt', 'r') as file:  #apriamo il file in modalità lettura utilizzando with

        contenuto = file.read()  #leggiamo tutto il contenuto del file
        print(contenuto)  #stampiamo il contenuto letto


# PUNTO 4 - SVUOTAMENTO DI UN FILE

def svuota_file():  #funzione per svuotare il contenuto di un file

    nome_file = input('Inserisci il nome del file che vuoi modificare: ')  #chiediamo il nome del file da svuotare

    with open(nome_file + '.txt', 'w') as file:  #apriamo il file in modalità scrittura utilizzando with

        file.write('')  #scriviamo una stringa vuota nel file

        print('File svuotato correttamente! ')  #confermiamo lo svuotamento del file


# MENU PRINCIPALE - GESTIONE DEI FILE

while True:  #creiamo un menu ripetibile attraverso un ciclo while

    print('\n--- GESTIONE DEI FILE ---')  #stampiamo il titolo del menu
    print('1. Creare un file')  #prima operazione disponibile
    print('2. Modificare un file')  #seconda operazione disponibile
    print('3. Leggere un file')  #terza operazione disponibile
    print('4. Svuotare un file')  #quarta operazione disponibile
    print('0. Esci')  #opzione per uscire dal programma

    scelta = int(input('\nScegli un operazione: '))  #chiediamo all'utente quale operazione eseguire

    match scelta:  #controlliamo la scelta effettuata dall'utente

        case 1:  #caso in cui l'utente vuole creare un nuovo file
            crea_file()  #richiamiamo la funzione per creare il file

        case 2:  #caso in cui l'utente vuole modificare un file
            modifica_file()  #richiamiamo la funzione per modificare il file

        case 3:  #caso in cui l'utente vuole leggere un file
            leggi_file()  #richiamiamo la funzione per leggere il file

        case 4:  #caso in cui l'utente vuole svuotare un file
            svuota_file()  #richiamiamo la funzione per svuotare il file

        case 0:  #caso in cui l'utente vuole uscire dal programma
            print('Chiusura del programma...')  #stampiamo il messaggio di chiusura
            break  #interrompiamo il ciclo while e terminiamo il programma

        case _:  #caso in cui l'utente inserisce una scelta non presente nel menu
            print('Scelta non valida, riprova!')  #segnaliamo la scelta non valida
