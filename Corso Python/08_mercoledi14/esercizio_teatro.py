
# ESERCIZIO - SISTEMA DI GESTIONE POSTI TEATRO

# Utilizziamo l'incapsulamento per proteggere gli attributi dei posti.
# Utilizziamo l'ereditarietà per creare PostoStandard dalla classe Posto.
# Ogni posto avrà un numero, una fila e uno stato di occupazione.


# CLASSE POSTO

class Posto: #creiamo la classe padre

    def __init__(self, numero, fila): #costruttore della classe
        
        self.__numeroPosti = numero #attributo privato del numero
        self.__fila = fila #attributo privato della fila
        self.__occupato = False #inizialmente il posto è libero

    def get_numero(self): #getter per leggere il numero
        
        return self.__numeroPosti

    def get_fila(self): #getter per leggere la fila
        
        return self.__fila

    def get_occupato(self): #getter per verificare se il posto è occupato
        
        return self.__occupato

    def prenota(self): #metodo per prenotare il posto

        if self.__occupato == False: #controlliamo se il posto è libero
            
            self.__occupato = True #modifichiamo lo stato del posto
            print("Posto prenotato correttamente")

        else:
            print("Posto già occupato")

    def libera(self): #metodo per liberare il posto

        if self.__occupato == True: #controlliamo se il posto è occupato
            
            self.__occupato = False #rendiamo nuovamente disponibile il posto
            print("Posto liberato correttamente")

        else:
            print("Il posto è già libero")

    def get_risultati(self): #metodo per stampare le informazioni del posto
        
        print(f"Fila: {self.__fila} - Posto: {self.__numeroPosti} - Occupato: {self.__occupato}")


# CLASSE POSTO STANDARD

class PostoStandard(Posto): #classe figlia che eredita da Posto

    def __init__(self, numero, fila, costo=11.50): #costruttore con costo predefinito
        
        super().__init__(numero, fila) #richiamiamo il costruttore del padre
        self.__costo = costo #attributo privato del costo

    def get_costo(self): #getter per leggere il costo
        return self.__costo


# CLASSE TEATRO

class Teatro:

    def __init__(self): #costruttore della classe
        
        self.__posto = [] #creiamo una lista privata per contenere i posti

    def aggiungi_posto(self): #metodo per aggiungere un posto

        numero = int(input("Inserisci il numero del posto: ")) #chiediamo il numero
        fila = int(input("Inserisci la fila del posto: ")) #chiediamo la fila

        for posto in self.__posto: #scorriamo i posti già inseriti

            if posto.get_numero() == numero and posto.get_fila() == fila: #controlliamo i duplicati
                print("Posto già presente nel teatro")
                return #interrompiamo il metodo

        posto_inserito = PostoStandard(numero, fila) #creiamo un nuovo oggetto
        self.__posto.append(posto_inserito) #aggiungiamo l'oggetto alla lista
        print("Posto aggiunto correttamente")

    def prenota_posto(self): #metodo per prenotare un posto

        numero = int(input("Inserisci il numero del posto: ")) #chiediamo il numero
        fila = int(input("Inserisci la fila del posto: ")) #chiediamo la fila

        for posto in self.__posto: #cerchiamo il posto nella lista

            if posto.get_numero() == numero and posto.get_fila() == fila: #verifichiamo numero e fila
                posto.prenota() #richiamiamo il metodo prenota dell'oggetto
                return #terminiamo la ricerca

        print("Posto non presente nel teatro") #nessun posto trovato

    def libera_posto(self): #metodo per liberare un posto

        numero = int(input("Inserisci il numero del posto: ")) #chiediamo il numero
        fila = int(input("Inserisci la fila del posto: ")) #chiediamo la fila

        for posto in self.__posto: #cerchiamo il posto nella lista

            if posto.get_numero() == numero and posto.get_fila() == fila: #controlliamo il posto
                posto.libera() #richiamiamo il metodo libera dell'oggetto
                return #terminiamo la ricerca

        print("Posto non presente nel teatro")

    def stampa_posti_occupati(self): #metodo per stampare i posti occupati

        trovati = False #variabile per verificare se esistono posti occupati

        for posto in self.__posto: #scorriamo tutti i posti

            if posto.get_occupato() == True: #controlliamo se il posto è occupato
                posto.get_risultati() #stampiamo le informazioni del posto
                trovati = True #abbiamo trovato almeno un posto occupato

        if trovati == False: #nessun posto occupato
            print("Non ci sono posti occupati")

    def stampa_tutti_posti(self): #metodo per visualizzare tutti i posti

        if len(self.__posto) == 0: #controlliamo se la lista è vuota
            print("Non ci sono posti nel teatro")
            return

        for posto in self.__posto: #scorriamo tutti gli oggetti
            posto.get_risultati() #stampiamo le informazioni
            print("Costo:", posto.get_costo(), "€") #stampiamo il costo del posto


# CREAZIONE DELL'OGGETTO TEATRO

teatro = Teatro() #creiamo il teatro con una lista inizialmente vuota

# MENU PRINCIPALE

while True: #creiamo un menu ripetibile

    print("\n--- GESTIONE TEATRO ---\n")
    print("1. Aggiungi posto")
    print("2. Prenota posto")
    print("3. Libera posto")
    print("4. Visualizza posti occupati")
    print("5. Visualizza tutti i posti")
    print("0. Esci")

    scelta = input("\nScegli un'operazione: ") #prendiamo la scelta dell'utente

    match scelta: #gestiamo le operazioni

        case "1": #aggiungiamo un nuovo posto
            
            teatro.aggiungi_posto() #richiamiamo il metodo della classe Teatro

        case "2": #prenotiamo un posto
            
            teatro.prenota_posto() #richiamiamo il metodo di prenotazione

        case "3": #liberiamo un posto
            
            teatro.libera_posto() #richiamiamo il metodo per liberare

        case "4": #visualizziamo i posti occupati
           
            teatro.stampa_posti_occupati() #stampiamo soltanto i posti prenotati

        case "5": #visualizziamo tutti i posti
            
            teatro.stampa_tutti_posti() #stampiamo tutti gli oggetti nella lista

        case "0": #usciamo dal programma
            
            print("Qui concludiamo")
            break #interrompiamo il ciclo while

        case _: #scelta non prevista
            print("Scelta non valida!")
