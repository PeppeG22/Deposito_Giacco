#ESERCIZIO 5 - CONVERTITORE

class Convertitore:

    @staticmethod  #definiamo un metodo statico
    def euro_in_dollari(euro:float=0):  #riceviamo l'importo in euro
        
        dollaro = euro * 1.08  #convertiamo gli euro in dollari
        return dollaro  #restituiamo il risultato

    @staticmethod  #definiamo un metodo statico
    def km_in_miglia(km:float=0):  #riceviamo la distanza in km
        
        miglia = km * 0.621371  #convertiamo i km in miglia
        return miglia  #restituiamo il risultato


#CONVERSIONE EURO IN DOLLARI

euro = float(input('Inserisci quanti euro vuoi convertire: '))  #chiediamo l'importo all'utente

dollari = Convertitore.euro_in_dollari(euro)  #richiamiamo il metodo direttamente dalla classe

print(f'{euro} euro corrispondono a {dollari} dollari')  #stampiamo il risultato


#CONVERSIONE KM IN MIGLIA

km = float(input('\nInserisci quanti km vuoi convertire: '))  #chiediamo la distanza all'utente

miglia = Convertitore.km_in_miglia(km)  #richiamiamo il metodo direttamente dalla classe

print(f'{km} km corrispondono a {miglia} miglia')  #stampiamo il risultato


#ESERCIZIO 2 - ANIMALI

class Animale:

    numero_animali: int = 0  #inizializziamo il contatore degli animali

    def __init__(self, nome, specie):  #costruttore della classe
        self.nome = nome  #assegniamo il nome dell'animale
        self.specie = specie  #assegniamo la specie dell'animale

        Animale.numero_animali += 1  #incrementiamo il contatore ogni volta che creiamo un animale

    @classmethod  #definiamo un metodo di classe
    def quanti_animali(cls):  #cls rappresenta la classe Animale
        return f'Ci sono {cls.numero_animali} animali!'  #restituiamo il numero totale degli animali


#CREAZIONE DEGLI OGGETTI

Animale1 = Animale('Tigre', 'Gialla')  #creiamo il primo animale
Animale2 = Animale('Panda', 'Fucsia')  #creiamo il secondo animale
Animale3 = Animale('Talpa', 'Benedetta')  #creiamo il terzo animale

print(Animale.quanti_animali())  #richiamiamo il metodo direttamente dalla classe