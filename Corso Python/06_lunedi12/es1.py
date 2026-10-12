
#Traccia 1: crea un classe chiamata - punto - con x e y per rappresentare i punti del piano
#           un metodo muovi che prenda in input un valore dx e uno dy e modifichi le coordinate
#           un metodo distanza_da_origine che restituisca la distanza del punto dall'origine (0,0)

#Traccia 2: crea una classe Libro, con 3 attributi titolo autore e pagine
#           un metodo che restituisca una stringa del tipo il libro è stato scritto da e ha pagine


#ESERCIZIO 1 -------->

class Punto:
    def __init__(self, x:int, y:int):  #costruttore della classe Punto
        self.x = x  #assegniamo la coordinata x all'oggetto
        self.y = y  #assegniamo la coordinata y all'oggetto

    def muovi(self, dx:int, dy:int):  #metodo per spostare il punto
        self.x += dx  #aggiungiamo lo spostamento alla coordinata x
        self.y += dy  #aggiungiamo lo spostamento alla coordinata y

    def distanza_da_origine(self):  #metodo per calcolare la distanza dall'origine
        return self.x-0, self.y-0  #formula della distanza dal punto (0,0)


#chiediamo all'utente le coordinate iniziali

x = int(input('Inserisci la coordinata x: '))
y = int(input('Inserisci la coordinata y: '))

p1 = Punto(x, y)  #creiamo un oggetto della classe Punto

print(f'Le coordinate del punto sono: ({p1.x}, {p1.y})')

#chiediamo di quanto spostare il punto
dx = int(input('Inserisci di quanto vuoi spostare la coordinata x: '))
dy = int(input('Inserisci di quanto vuoi spostare la coordinata y: '))

p1.muovi(dx, dy)  #richiamiamo il metodo per modificare le coordinate

print(f'Le coordinate aggiornate sono: ({p1.x}, {p1.y})')

#richiamiamo il metodo per calcolare la distanza dall'origine
print(f"La distanza dall'origine è: {p1.distanza_da_origine}")


#ESERCIZIO 2 ------------>

class Libro:
    def __init__(self, titolo: str, autore: str, pag: int):  #costruttore della classe Libro
        self.titolo = titolo  #assegniamo il titolo all'oggetto
        self.autore = autore  #assegniamo l'autore all'oggetto
        self.pag = pag  #assegniamo il numero di pagine all'oggetto

    def descrizione(self):  #metodo per restituire le informazioni del libro
        return f'Il libro {self.titolo} è stato scritto da {self.autore} ed ha {self.pag} pagine totali.'


#EXTRA - INSERIMENTO DI PIÙ LIBRI CON WHILE

libri = []  #creiamo una lista vuota dove salvare tutti i libri

while True:  #ciclo ripetibile per inserire più libri

    #chiediamo all'utente le informazioni del libro
    titolo = input('\nInserisci il titolo del libro: ')
    autore = input("Inserisci l'autore del libro: ")
    pag = int(input('Inserisci il numero di pagine del libro: '))

    libro1 = Libro(titolo, autore, pag)  #creiamo un oggetto della classe Libro

    libri.append(libro1)  #aggiungiamo l'oggetto alla lista dei libri

    print(libro1.descrizione())  #stampiamo la descrizione del libro inserito

    #chiediamo all'utente se vuole inserire un altro libro
    scelta = input('\nVuoi inserire un altro libro? si/no: ')

    if scelta.lower() != 'si':  #se la risposta è diversa da si
        break  #interrompiamo il ciclo while


#STAMPA FINALE DI TUTTI I LIBRI

print('\n--- ELENCO DEI LIBRI INSERITI ---')

for libro in libri:  #scorriamo tutti gli oggetti presenti nella lista
    print(libro.descrizione())  #richiamiamo il metodo descrizione per ogni libro