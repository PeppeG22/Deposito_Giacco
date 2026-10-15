
# ESERCIZIO - GESTIONE IMPIEGATI DI UN'AZIENDA

# Utilizziamo una classe astratta 
# Le classi figlie dovranno implementare il metodo calcola_stipendio()

from abc import ABC, abstractmethod #importiamo la classe astratta e il decoratore


# CLASSE ASTRATTA - IMPIEGATO

class Impiegato(ABC): #creiamo la classe astratta

    def __init__(self, nome, cognome, stipendio_base): #costruttore della classe
        
        self.nome = nome #attributo del nome
        self.cognome = cognome #attributo del cognome
        self.stipendio_base = stipendio_base #attributo dello stipendio base

    @abstractmethod #rendiamo obbligatorio il metodo
    def calcola_stipendio(self): #metodo astratto per calcolare lo stipendio
        pass #il metodo sarà implementato dalle classi figlie


# CLASSE FIGLIA - IMPIEGATO FISSO

class ImpiegatoFisso(Impiegato): #ereditiamo dalla classe astratta Impiegato

    def calcola_stipendio(self): #implementiamo il metodo astratto del padre
        return self.stipendio_base #restituiamo lo stipendio senza modifiche


# CLASSE FIGLIA - IMPIEGATO A PROVVIGIONE

class ImpiegatoAProvvigione(Impiegato): #ereditiamo dalla classe astratta Impiegato

    def __init__(self, nome, cognome, stipendio_base, vendite): #costruttore della classe figlia
        super().__init__(nome, cognome, stipendio_base) #richiamiamo il costruttore del padre
        self.vendite = vendite #aggiungiamo l'attributo delle vendite

    def calcola_stipendio(self): #implementiamo il metodo astratto
        
        bonus = self.vendite * 10 / 100 #calcoliamo il bonus del 10% sulle vendite
        totale = self.stipendio_base + bonus #sommiamo il bonus allo stipendio base
        return totale #restituiamo lo stipendio mensile calcolato


# FUNZIONE PER STAMPARE GLI IMPIEGATI

def stampa_impiegati(impiegati): #funzione che riceve una lista di impiegati

    for i in impiegati: #scorriamo tutti gli oggetti presenti nella lista
        print(f"Nome: {i.nome}") #stampiamo il nome
        print(f"Cognome: {i.cognome}") #stampiamo il cognome
        print(f"Stipendio base: {i.stipendio_base} €") #stampiamo lo stipendio base
        print(f"Stipendio mensile: {i.calcola_stipendio()} €") #richiamiamo il metodo della classe figlia


# CREAZIONE DEGLI OGGETTI

impiegato1 = ImpiegatoFisso("Mario", "Rossi", 1800) #creiamo un impiegato con stipendio fisso

impiegato2 = ImpiegatoAProvvigione("Luca", "Bianchi", 1500, 5000) #creiamo un impiegato con 5000 euro di vendite

impiegato3 = ImpiegatoAProvvigione("Anna", "Verdi", 1600, 3000) #creiamo un secondo impiegato a provvigione


# CREAZIONE LISTA IMPIEGATI

impiegati = [] #creiamo una lista vuota per contenere gli oggetti

impiegati.append(impiegato1) #aggiungiamo il primo impiegato
impiegati.append(impiegato2) #aggiungiamo il secondo impiegato
impiegati.append(impiegato3) #aggiungiamo il terzo impiegato


# STAMPA DEI RISULTATI

stampa_impiegati(impiegati) #richiamiamo la funzione che stampa tutti gli impiegati
