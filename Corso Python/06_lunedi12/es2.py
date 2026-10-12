
#ESERCIZIO 3 

class ContoCorrente:
    def __init__(self, saldo=0):  #costruttore della classe ContoCorrente
        if saldo >= 0:  #controlliamo che il saldo iniziale sia positivo o uguale a 0
            self.saldo = saldo  #inizializziamo il saldo del conto
        else:
            self.saldo = 0  #se il saldo è negativo lo impostiamo a 0

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
                self.saldo -= prelievo  #sottraiamo il prelievo dal saldo
                print(f'Hai prelevato {prelievo}€')
        else:
            print('Non puoi prelevare un importo minore o uguale a 0€!')

    def stampa_saldo(self):  #metodo per stampare il saldo attuale
        print(f'Il saldo attuale del tuo conto è {self.saldo}€')


#CREAZIONE DEL CONTO CORRENTE

saldo_base = int(input('Quanti soldi vuoi nel tuo conto? '))  #chiediamo il saldo iniziale

conto1 = ContoCorrente(saldo_base)  #creiamo un conto con il saldo scelto dall'utente

conto1.stampa_saldo()  #stampiamo il saldo iniziale


#MENU PRINCIPALE

while True:  #creiamo un ciclo ripetibile per effettuare più operazioni

    print('\n------ GESTIONE CONTO CORRENTE ------')
    print('1. Deposita denaro')
    print('2. Preleva denaro')
    print('3. Visualizza saldo')
    print('0. Esci')

    scelta = input('\nScegli un operazione: ')  #chiediamo all'utente quale operazione eseguire

    match scelta:  #controlliamo la scelta dell'utente

        case '1':  #caso in cui vogliamo depositare
            dep1 = int(input('Quanto vuoi depositare? '))  #chiediamo l'importo del deposito
            conto1.deposito(dep1)  #richiamiamo il metodo deposito

        case '2':  #caso in cui vogliamo prelevare
            prel1 = int(input('Quanto vuoi prelevare? '))  #chiediamo l'importo del prelievo
            conto1.prelievo(prel1)  #richiamiamo il metodo prelievo

        case '3':  #caso in cui vogliamo visualizzare il saldo
            conto1.stampa_saldo()  #richiamiamo il metodo per stampare il saldo

        case '0':  #caso in cui vogliamo uscire dal programma
            print('\nGrazie per aver utilizzato il nostro conto corrente!')
            break  #interrompiamo il ciclo while

        case _:  #caso in cui l'utente inserisce una scelta non valida
            print('Scelta non valida! Riprova.')
