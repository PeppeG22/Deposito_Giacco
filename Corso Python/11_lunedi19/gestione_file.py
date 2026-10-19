
'''
GESTIONE DEI FILE IN PYTHON

La gestione dei file in Python permette di leggere, scrivere e modificare
il contenuto dei file attraverso operazioni di input/output (I/O).

La funzione principale è open(), che accetta due parametri:

1. Nome del file o percorso -> indica il file su cui lavorare.
2. Modalità di apertura -> indica l'operazione da eseguire sul file.

MODALITÀ PRINCIPALI:

'r' -> lettura: apre un file esistente, se non esiste genera un errore.
'w' -> scrittura: crea il file se non esiste, altrimenti cancella il contenuto precedente e lo sovrascrive.
'a' -> aggiunta: aggiunge contenuto alla fine del file senza cancellare quello esistente.
'x' -> creazione: crea un nuovo file, ma genera un errore se esiste già.

MODALITÀ COMBINATE (DA UTILIZZARE CON ATTENZIONE):

'r+' -> permette di leggere e scrivere un file esistente senza cancellarlo automaticamente.
'w+' -> permette di leggere e scrivere, ma cancella subito il contenuto precedente.

Queste modalità richiedono attenzione perché possiamo modificare
o perdere accidentalmente i dati del file.
'''


# ESEMPIO 1 - APERTURA E LETTURA DI UN FILE

file = open('file_prova.txt', 'r')  #apriamo il file in modalità lettura
contenuto = file.read()  #leggiamo tutto il contenuto del file
print(contenuto)  #stampiamo il contenuto letto
file.close()  #chiudiamo il file dopo averlo utilizzato


'''
DIFFERENZA TRA READ(), READLINE() E READLINES()

read() -> legge tutto il contenuto del file e restituisce una stringa.

readline() -> legge una sola riga alla volta e restituisce una stringa.
Richiamandolo nuovamente, passa alla riga successiva.

readlines() -> legge tutte le righe e le restituisce in una lista.

Possiamo utilizzare un ciclo for per scorrere tutte le righe
di un file e, attraverso una condizione, individuare quella desiderata.
'''


# ESEMPIO 2 - LETTURA DI UNA RIGA ALLA VOLTA

file = open('file_prova.txt', 'r')  #apriamo il file in lettura
riga1 = file.readline()  #leggiamo la prima riga
riga2 = file.readline()  #leggiamo la seconda riga
print(riga1)  #stampiamo la prima riga
print(riga2)  #stampiamo la seconda riga
file.close()  #chiudiamo il file


# ESEMPIO 3 - LETTURA DELLE RIGHE CON UN CICLO FOR

file = open('file_prova.txt', 'r')  #apriamo il file in lettura
contatore = 0  #creiamo un contatore per le righe

for riga in file:  #scorriamo tutte le righe presenti nel file
    contatore += 1  #incrementiamo il contatore a ogni riga

    if contatore == 3:  #controlliamo se siamo arrivati alla terza riga
        print(riga)  #stampiamo solamente la terza riga

file.close()  #chiudiamo il file


'''
SCRITTURA DEI FILE - WRITE()

Il metodo write() permette di scrivere del testo all'interno di un file.

Utilizzando la modalità 'w':
- Se il file non esiste, viene creato automaticamente.
- Se il file esiste, il contenuto precedente viene cancellato.

Utilizzando invece la modalità 'a', il nuovo testo viene aggiunto
alla fine del file senza cancellare quello precedente.

Il metodo write() non aggiunge automaticamente una nuova riga:
possiamo utilizzare \n per andare a capo.
'''


# ESEMPIO 4 - SCRITTURA DI UN FILE

file = open('file_prova.txt', 'w')  #apriamo il file in scrittura
file.write('Ciao, sto imparando Python!\n')  #scriviamo una prima riga
file.write('Questa è la seconda riga.')  #scriviamo una seconda riga
file.close()  #chiudiamo il file salvando le modifiche


# ESEMPIO 5 - AGGIUNTA DI TESTO A UN FILE

file = open('file_prova.txt', 'a')  #apriamo il file in modalità aggiunta
file.write('\nQuesta è una nuova riga.')  #aggiungiamo il testo senza cancellare il precedente
file.close()  #chiudiamo il file


'''
IL COMANDO WITH

Il comando with permette di aprire e utilizzare un file
senza dover richiamare manualmente il metodo close().

Quando terminiamo il blocco di codice indentato,
Python chiude automaticamente il file, anche in caso di errore.

È il metodo consigliato per gestire i file in Python.
'''


# ESEMPIO 6 - UTILIZZO DI WITH IN LETTURA

with open('file_prova.txt', 'r') as file:  #apriamo il file utilizzando with
    contenuto = file.read()  #leggiamo tutto il contenuto
    print(contenuto)  #stampiamo il contenuto del file

#il file viene chiuso automaticamente al termine del blocco


# ESEMPIO 7 - UTILIZZO DI WITH IN SCRITTURA

with open('file_prova.txt', 'a') as file:  #apriamo il file in modalità aggiunta
    file.write('\nSto utilizzando il comando with!')  #aggiungiamo una nuova riga

#il file viene chiuso automaticamente senza utilizzare close()


'''
RICORDA:

- open() -> apre un file.
- read() -> legge tutto il contenuto.
- readline() -> legge una riga alla volta.
- readlines() -> restituisce una lista di righe.
- write() -> scrive del testo.
- close() -> chiude il file.
- with -> gestisce automaticamente la chiusura.

ATTENZIONE:
La modalità 'w' cancella il contenuto precedente del file.
La modalità 'a' permette invece di conservarlo e aggiungere nuovo testo.

Se indichiamo solamente il nome del file, Python lo cerca
nella cartella di lavoro corrente.
Possiamo anche specificare il percorso completo del file.
'''
