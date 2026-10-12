
#ESERCIZIO 4 - GARAGE

class Garage:
    
    def __init__(self, capienza:int=0):
        
        self.capienza = capienza  #impostiamo il numero massimo di auto
        self.auto_presenti = []  #creiamo una lista vuota per le targhe

    def park(self, targa):  #metodo per parcheggiare un'auto

        targa = targa.upper()  #trasformiamo la targa in maiuscolo

        if not self.controllo_targa(targa):  #controlliamo se la targa non è valida
            
            print('Formato targa non valido!')
            return  #interrompiamo il metodo

        if targa in self.auto_presenti:  #controlliamo se la targa è già presente
            
            print('La tua macchina è già parcheggiata!')

        elif len(self.auto_presenti) < self.capienza:  #controlliamo se ci sono posti liberi
            
            self.auto_presenti.append(targa)  #aggiungiamo la targa alla lista
            print('Auto parcheggiata correttamente!')

        else:  #caso in cui il garage è pieno
            print('Garage pieno!')

    def rimuovi_auto(self, targa):  #metodo per rimuovere un'auto dal garage

        targa = targa.upper()  #trasformiamo la targa in maiuscolo

        if targa in self.auto_presenti:  #controlliamo se la targa è presente
            
            self.auto_presenti.remove(targa)  #rimuoviamo la targa dalla lista
            print('Auto rimossa correttamente!')
        
        else:
            print('La tua macchina non è parcheggiata!')

    
    def posti_liberi(self):  #metodo per calcolare i posti liberi
        
        posti = self.capienza - len(self.auto_presenti)  #calcoliamo i posti disponibili

        print(f'Rimangono {posti} posti liberi!')

        return posti  #restituiamo il numero dei posti disponibili

    def controllo_targa(self, targa):  #metodo per controllare il formato della targa

        targa = targa.upper()  #trasformiamo la targa in maiuscolo

        if len(targa) == 7 and targa[:2].isalpha() and targa[2:5].isdigit() and targa[5:].isalpha():
            
            return True  #la targa rispetta il formato richiesto
        else:
            return False  #la targa non rispetta il formato richiesto


#CREAZIONE DEL GARAGE

parcheggio = Garage(10)  #creiamo un garage con 10 posti disponibili


#MENU 

while True:  #creiamo un ciclo ripetibile per effettuare più operazioni

    print('\n------ PARCHEGGIO ------')
    print('1. Parcheggia la macchina')
    print('2. Rimuovi la tua macchina')
    print('3. Parcheggi rimanenti')
    print('4. Lista auto parcheggiate')
    print('0. Esci')

    scelta = input('\nScegli un operazione: ')  #chiediamo all'utente quale operazione eseguire

    match scelta:  #controlliamo la scelta dell'utente

        case '1':  #caso in cui vogliamo parcheggiare un'auto

            targa = input('Inserisci la targa della tua macchina: ')  #chiediamo la targa

            parcheggio.park(targa)  #richiamiamo il metodo per parcheggiare

        case '2':  #caso in cui vogliamo rimuovere un'auto

            targa = input('Inserisci la targa della macchina da rimuovere: ')  #chiediamo la targa

            parcheggio.rimuovi_auto(targa)  #richiamiamo il metodo per rimuovere l'auto

        case '3':  #caso in cui vogliamo visualizzare i parcheggi rimanenti

            parcheggio.posti_liberi()  #richiamiamo il metodo per contare i posti liberi

        case '4':  #caso in cui vogliamo visualizzare le auto parcheggiate

            if len(parcheggio.auto_presenti) == 0:  #controlliamo se il garage è vuoto
                print('Non ci sono auto parcheggiate!')

            else:
                for targa in parcheggio.auto_presenti:  #scorriamo tutte le targhe presenti
                    print(targa)  #stampiamo ogni targa

        case '0':  #caso in cui vogliamo uscire dal programma

            print('\nGrazie per aver utilizzato il nostro parcheggio!')
            break  #interrompiamo il ciclo while

        case _:  #caso in cui l'utente inserisce una scelta non valida

            print('Scelta non valida! Riprova.')
