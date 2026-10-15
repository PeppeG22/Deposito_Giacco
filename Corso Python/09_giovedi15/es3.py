
from abc import ABC, abstractmethod  # importiamo la classe astratta e il decoratore


# CLASSE ASTRATTA - VEICOLO TRASPORTO

class VeicoloTrasporto(ABC):  # creiamo la classe astratta per il trasporto delle merci

    def __init__(self, targa: str, peso_massimo: int, carico_attuale: int = 0):  # costruttore della classe

        self._targa = targa  # attributo della targa
        self._peso_massimo = peso_massimo  # attributo del peso massimo
        self._carico_attuale = carico_attuale  # attributo del carico attuale

    def __str__(self):  # metodo per rappresentare il veicolo come stringa
        return f'Veicolo con targa {self._targa}'

    def carica(self):  # metodo per aggiungere un carico al veicolo

        peso = int(input("Inserisci il peso da aggiungere: "))  # chiediamo il peso da aggiungere

        if peso > 0:  # controlliamo che il peso sia positivo

            if self._peso_massimo >= peso + self._carico_attuale:  # controlliamo di non superare il peso massimo

                self._carico_attuale += peso  # aggiungiamo il peso al carico attuale

                print(self._carico_attuale)  # stampiamo il nuovo carico

                return  # terminiamo il metodo

            else:
                print("Il peso non può essere aggiunto perchè supera il limite massimo! ")

        else:
            print("Il peso deve essere maggiore di zero! ")

    def scarica(self):  # metodo per scaricare completamente il veicolo

        self._carico_attuale = 0  # azzeriamo il carico attuale
        print(f"Il carico attuale è {self._carico_attuale} ")

    @abstractmethod  # rendiamo obbligatorio il metodo per le classi figlie
    def costo_manutenzione(self):  # metodo astratto per calcolare il costo della manutenzione
        pass  # il metodo sarà implementato dalle classi figlie


# CLASSI CONCRETE


# CLASSE CAMION

class Camion(VeicoloTrasporto):  # ereditiamo dalla classe astratta

    def __init__(self, targa, peso_massimo, carico_attuale=0, numero_assi: int = 0):

        super().__init__(targa, peso_massimo, carico_attuale)  # richiamiamo il costruttore del padre
        self._numero_assi = numero_assi  # attributo del numero di assi

    def costo_manutenzione(self):  # implementiamo il metodo astratto

        tot_cost = 100 * self._numero_assi + self._peso_massimo  # calcoliamo il costo
        print(f"Il costo manutenzione del camion è {tot_cost}€ ")
        return tot_cost  # restituiamo il costo


# CLASSE FURGONE

class Furgone(VeicoloTrasporto):  # ereditiamo dalla classe astratta

    def __init__(self, targa, peso_massimo, carico_attuale=0, alimentazione: str = ""):

        super().__init__(targa, peso_massimo, carico_attuale)  # richiamiamo il costruttore del padre
        self.alimentazione = alimentazione  # attributo dell'alimentazione

    def costo_manutenzione(self):  # implementiamo il metodo astratto

        tot_cost = 0  # inizializziamo il costo

        if self.alimentazione.lower() == "diesel":  # controlliamo se è diesel

            tot_cost = 150  # assegniamo il costo

        elif self.alimentazione.lower() == "elettrico":  # controlliamo se è elettrico

            tot_cost = 288  # assegniamo il costo

        else:
            print("Alimentazione non valida! ")
            return 0  # restituiamo zero per evitare errori nella somma

        print(f"Il costo manutenzione del furgone è {tot_cost}€ ")
        return tot_cost  # restituiamo il costo


# CLASSE MOTOCARRO

class Motocarro(VeicoloTrasporto):  # ereditiamo dalla classe astratta

    def __init__(self, targa, peso_massimo, carico_attuale=0, anni_servizio: int = 0):

        super().__init__(targa, peso_massimo, carico_attuale)  # richiamiamo il costruttore del padre
        self._anni_servizio = anni_servizio  # attributo degli anni di servizio

    def costo_manutenzione(self):  # implementiamo il metodo astratto

        tot_cost = 50 * self._anni_servizio  # calcoliamo il costo
        print(f"Il costo manutenzione del motocarro è {tot_cost}€ ")
        return tot_cost  # restituiamo il costo


# CLASSE GESTORE FLOTTA

class GestoreFlotta:  # classe che gestisce tutti i veicoli

    def __init__(self):  # costruttore della classe

        self.veicoli = []  # creiamo una lista vuota per contenere i veicoli

    def aggiungi_veicolo(self, veicolo):  # metodo per aggiungere un veicolo

        self.veicoli.append(veicolo)  # aggiungiamo il veicolo alla lista
        print('Veicolo aggiunto correttamente! ')

    def rimuovi_veicolo(self, targa):  # metodo per rimuovere un veicolo tramite targa

        for veicolo in self.veicoli:  # scorriamo tutti i veicoli della lista

            if veicolo._targa == targa:  # controlliamo se la targa corrisponde

                self.veicoli.remove(veicolo)  # rimuoviamo il veicolo dalla lista
                print('Veicolo rimosso correttamente!')
                return  # terminiamo il metodo dopo la rimozione

        print('Veicolo non trovato! ')  # stampiamo se non troviamo la targa

    def costo_totale_manutenzione(self):  # metodo per sommare i costi di manutenzione

        tot = 0  # inizializziamo il totale

        for veicolo in self.veicoli:  # scorriamo tutti i veicoli della lista

            tot += veicolo.costo_manutenzione()  # richiamiamo il metodo di ogni veicolo e sommiamo

        return tot  # restituiamo il costo totale

    def stampa_veicoli(self):  # metodo per stampare tutti i veicoli

        for veicolo in self.veicoli:  # scorriamo tutti i veicoli della lista

            if isinstance(veicolo, Camion):  # controlliamo se il veicolo è un camion
                tipo = "Camion"

            elif isinstance(veicolo, Furgone):  # controlliamo se il veicolo è un furgone
                tipo = "Furgone"

            elif isinstance(veicolo, Motocarro):  # controlliamo se il veicolo è un motocarro
                tipo = "Motocarro"

            else:
                tipo = "Veicolo generico"  # caso in cui il tipo non sia riconosciuto

            print(f"Targa: {veicolo._targa}")  # stampiamo la targa
            print(f"Tipo: {tipo}")  # stampiamo il tipo di veicolo
            print(f"Carico attuale: {veicolo._carico_attuale}")  # stampiamo il carico attuale
            print()  # andiamo a capo per separare i veicoli


# PROGRAMMA PRINCIPALE

c1 = Camion('aaa', 100, 2, 6)  # creiamo un camion
c2 = Motocarro('bbb', 200, 3, 9)  # creiamo un motocarro
c3 = Furgone('ccc', 300, 4, 'diesel')  # creiamo un furgone

flotta = GestoreFlotta()  # creiamo un oggetto della classe GestoreFlotta

flotta.aggiungi_veicolo(c1)  # aggiungiamo il camion
flotta.aggiungi_veicolo(c2)  # aggiungiamo il motocarro
flotta.aggiungi_veicolo(c3)  # aggiungiamo il furgone

print('\nELENCO VEICOLI\n')

flotta.stampa_veicoli()  # stampiamo tutti i veicoli presenti nella flotta

print('\nCOSTO MANUTENZIONE\n')

totale = flotta.costo_totale_manutenzione()  # calcoliamo il costo totale
print(f'\nIl costo totale della manutenzione è {totale}€')  # stampiamo il totale

print('\nRIMOZIONE VEICOLO\n')

flotta.rimuovi_veicolo('bbb')  # rimuoviamo il veicolo con targa bbb

print('\nELENCO AGGIORNATO\n')

flotta.stampa_veicoli()  # stampiamo la lista aggiornata
