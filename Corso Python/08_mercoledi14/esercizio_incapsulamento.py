
# ESERCIZIO - INCAPSULAMENTO CON GETTER E SETTER

# Creiamo una classe ContoBancario con attributi privati

class ContoBancario:

    def __init__(self, titolare, saldo): #costruttore della classe
        
        self.__titolare = titolare #attributo privato del titolare
        self.__saldo = saldo #attributo privato del saldo

    def get_titolare(self): #getter per leggere il titolare
        
        return self.__titolare #restituiamo il nome

    def set_titolare(self, titolare): #setter per modificare il titolare

        if titolare == "": #controlliamo che il nome non sia vuoto
            
            print("Nome del titolare non valido")
            return #interrompiamo il metodo

        else:
            
            self.__titolare = titolare #aggiorniamo il titolare
            print("Titolare modificato correttamente")

    def deposita(self, importo): #metodo per depositare denaro

        if importo <= 0: #controlliamo che l'importo sia positivo
            
            print("Importo non valido")
            return #interrompiamo il metodo

        else:
            
            self.__saldo += importo #aggiungiamo l'importo al saldo
            print("Deposito effettuato")

    def preleva(self, importo): #metodo per prelevare denaro

        if importo <= 0: #controlliamo che l'importo sia positivo
            
            print("Importo non valido")
            return #interrompiamo il metodo

        elif importo > self.__saldo: #controlliamo che il saldo sia sufficiente
            
            print("Saldo insufficiente")
            return #interrompiamo il metodo

        else:
            
            self.__saldo -= importo #sottraiamo l'importo dal saldo
            print("Prelievo effettuato")

    def visualizza_saldo(self): #metodo per leggere il saldo
        
        return self.__saldo #restituiamo il saldo senza modificarlo


# INSERIMENTO DATI

titolare = input("Inserisci il nome del titolare: ") #chiediamo il nome

while titolare == "": #ripetiamo finché il nome è vuoto
    
    print("Nome del titolare non valido")
    titolare = input("Inserisci il nome del titolare: ")

conto = ContoBancario(titolare, 0) #creiamo l'oggetto con saldo iniziale a 0


# MENU PRINCIPALE

while True: #creiamo un menu ripetibile

    print("\n--- CONTO BANCARIO ---\n")
    print("1. Deposita")
    print("2. Preleva")
    print("3. Visualizza saldo")
    print("4. Modifica titolare")
    print("0. Esci")

    scelta = input("\nScegli un'operazione: ") #prendiamo la scelta dell'utente

    match scelta: #gestiamo le operazioni

        case "1": #deposito
            
            importo = float(input("Quanto vuoi depositare? ")) #chiediamo l'importo
            conto.deposita(importo) #richiamiamo il metodo deposita

        case "2": #prelievo
            
            importo = float(input("Quanto vuoi prelevare? ")) #chiediamo l'importo
            conto.preleva(importo) #richiamiamo il metodo preleva

        case "3": #visualizzazione saldo
            
            nome = conto.get_titolare() #otteniamo il nome tramite getter
            saldo = conto.visualizza_saldo() #otteniamo il saldo

            print(f"\nIl saldo di {nome} è: {saldo} €") #stampiamo il risultato

        case "4": #modifica del titolare
            
            nuovo_titolare = input("Inserisci il nuovo titolare: ") #chiediamo il nome
            conto.set_titolare(nuovo_titolare) #richiamiamo il setter

        case "0": #uscita dal programma
            
            print("Qui concludiamo")
            break #interrompiamo il ciclo while

        case _: #scelta non prevista
            print("Scelta non valida!")
