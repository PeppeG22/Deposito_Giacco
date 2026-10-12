
#ESERCIZIO 3 - CONTO CORRENTE

class ContoCorrente:
    def __init__(self, saldo=0):  #costruttore della classe ContoCorrente
        self.saldo = saldo  #inizializziamo il saldo del conto

    def deposito(self, deposito:int):  #metodo per depositare denaro
        
        if deposito <= 0:  #controlliamo che l'importo sia positivo
            print('Non puoi depositare un importo minore o uguale a 0€!')
        else:
            self.saldo += deposito  #aggiungiamo il deposito al saldo
            print(f'Hai depositato {deposito}€')

    def prelievo(self, prelievo:int):  #metodo per prelevare denaro
        
        if prelievo > 0:  #controlliamo che l'importo sia positivo
            
            if prelievo > self.saldo:  #controlliamo se il saldo è sufficiente
                print('Saldo non sufficiente!')
            
            else:
                print(f'Hai prelevato {prelievo}€')
                self.saldo -= prelievo  #sottraiamo il prelievo dal saldo
        else:
            print('Non puoi prelevare un importo minore o uguale a 0€!')

    def stampa_saldo(self):  #metodo per stampare il saldo attuale
        print(f'Il saldo attuale del tuo conto è {self.saldo}€')


#CREAZIONE DEL CONTO CORRENTE

saldo_base = int(input('Quanti soldi vuoi nel tuo conto? ')) #inizializziamo il conto

conto1 = ContoCorrente(saldo_base)  #creiamo un conto con saldo iniziale gia impostato

conto1.stampa_saldo()  #stampiamo il saldo iniziale

#DEPOSITO

dep1 = int(input('Quanto vuoi depositare? ')) #chiediamo quanto vuole depositare

conto1.deposito(dep1)  #depositiamo sul conto

#PRELIEVO

prel1 = int(input('Quanto vuoi prelevare? ')) #chiediamo quanto vuole prelevare

conto1.prelievo(prel1)  #preleviamo dal conto

conto1.stampa_saldo()  #stampiamo il saldo finale
