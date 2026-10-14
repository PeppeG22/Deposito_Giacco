
# ESERCIZIO - SISTEMA DI GESTIONE PAGAMENTI

# Il polimorfismo permette di richiamare lo stesso metodo
# su oggetti di classi diverse, ottenendo comportamenti differenti.
# L'overriding permette alle classi figlie di sovrascrivere
# un metodo già presente nella classe padre.


# CLASSE METODO PAGAMENTO

class MetodoPagamento: #creiamo la classe padre

    def effettua_pagamento(self, importo): #metodo che sarà ridefinito dalle classi figlie
        pass #non inseriamo istruzioni nella classe padre


# CLASSE CARTA DI CREDITO

class CartaDiCredito(MetodoPagamento): #ereditiamo dalla classe MetodoPagamento

    def effettua_pagamento(self, importo): #sovrascriviamo il metodo del padre
        print(f"Hai effettuato un pagamento con carta di {importo} euro")


# CLASSE PAYPAL

class Paypal(MetodoPagamento): #ereditiamo dalla classe MetodoPagamento

    def effettua_pagamento(self, importo): #sovrascriviamo il metodo del padre
        print(f"Hai effettuato un pagamento con PayPal di {importo} euro")


# CLASSE BONIFICO BANCARIO

class BonificoBancario(MetodoPagamento): #ereditiamo dalla classe MetodoPagamento

    def effettua_pagamento(self, importo): #sovrascriviamo il metodo del padre
        print(f"Hai effettuato un pagamento con bonifico bancario di {importo} euro")


# CLASSE GESTORE PAGAMENTI

class GestorePagamenti:

    def __init__(self, metodo): #costruttore che riceve un oggetto di pagamento
        
        self.metodo = metodo #salviamo l'oggetto ricevuto come attributo

    def process(self, importo): #metodo per elaborare il pagamento
        
        self.metodo.effettua_pagamento(importo) #richiamiamo il metodo dell'oggetto scelto


# FUNZIONE PER SCEGLIERE IL METODO DI PAGAMENTO

def scegli_metodo(): #funzione che permette di scegliere il metodo

    while True: #ripetiamo la scelta finché non è valida

        print("\n--- METODI DI PAGAMENTO ---\n")
        print("1. Carta di credito")
        print("2. PayPal")
        print("3. Bonifico bancario")

        scelta = input("\nScegli un metodo di pagamento: ") #prendiamo la scelta

        match scelta: #controlliamo il metodo selezionato

            case "1": #pagamento con carta
                
                return GestorePagamenti(CartaDiCredito()) #creiamo e restituiamo il gestore con carta

            case "2": #pagamento con PayPal
                
                return GestorePagamenti(Paypal()) #creiamo e restituiamo il gestore con PayPal

            case "3": #pagamento con bonifico
                
                return GestorePagamenti(BonificoBancario()) #creiamo e restituiamo il gestore con bonifico

            case _: #scelta non prevista
                
                print("Metodo di pagamento non valido!")


# INSERIMENTO METODO INIZIALE

print("\nScegli il metodo di pagamento iniziale")

gestore = scegli_metodo() #richiamiamo la funzione e salviamo il gestore restituito


# MENU PRINCIPALE

while True: #creiamo un menu ripetibile

    print("\n--- GESTIONE PAGAMENTI ---\n")
    print("1. Effettua pagamento")
    print("2. Cambia metodo di pagamento")
    print("0. Esci")

    scelta = input("\nScegli un'operazione: ") #prendiamo la scelta dell'utente

    match scelta: #gestiamo le operazioni

        case "1": #effettuiamo un pagamento

            importo = float(input("Inserisci l'importo da pagare: ")) #chiediamo l'importo

            if importo <= 0: #controlliamo che l'importo sia positivo
                print("Importo non valido")

            else:
                gestore.process(importo) #richiamiamo il pagamento attraverso il gestore

        case "2": #modifichiamo il metodo di pagamento
            gestore = scegli_metodo() #scegliamo un nuovo metodo e aggiorniamo il gestore

        case "0": #usciamo dal programma
            print("Qui concludiamo")
            break #interrompiamo il ciclo while

        case _: #scelta non valida
            print("Scelta non valida!")
