'''
ESERCIZI

Estendere una classe base UnitaMilitare per creare diverse unità specializzate,
ciascuna con compiti e metodi specifici.
Inoltre, implementare una classe ControlloMilitare che eredita da tutte le altre
classi per gestire e tenere traccia delle diverse unità, utilizzando i metodi speciali.
1. Classe UnitaMilitare:

   Attributi:
   - nome (stringa): nome dell'unità.
   - numero_soldati (intero): numero di soldati nell'unità.

   Metodi:
   - muovi(): stampa un messaggio sul movimento dell'unità.
   - attacca(): stampa un messaggio sull'attacco.
   - ritira(): gestisce il ritiro strategico.
2. Classi Derivate:

   Fanteria:
   - costruisci_trincea(): costruisce difese temporanee.

   Artiglieria:
   - calibra_artiglieria(): calibra i pezzi di artiglieria per la precisione.

   Cavalleria:
   - esplora_terreno(): esplora l'area per raccogliere informazioni sul nemico.

   SupportoLogistico:
   - rifornisci_unita(): gestisce il rifornimento e la manutenzione.

   Ricognizione:
   - conduci_ricognizione(): conduce missioni di sorveglianza.
3. Classe ControlloMilitare:

   Eredita da tutte le classi precedenti.

   Attributi aggiuntivi:
   - unita_registrate: lista per tenere traccia delle unità create.

   Metodi:
   - registra_unita(unita): aggiunge un'unità al registro.
   - mostra_unita(): elenca tutte le unità registrate.
   - dettagli_unita(nome): mostra i dettagli specifici di un'unità.
4. EXTRA:

   Utilizzare i seguenti metodi speciali:

   - __repr__()
   - __getattribute__()
   - __eq__()

'''
#CLASSE PADRE - UNITAMILITARE

class UnitaMilitare:  #creiamo la classe padre da cui erediteranno tutte le altre unità

    def __init__(self, nome, numero_soldati):  #costruttore della classe con i due attributi
        
        self.nome = nome  #assegniamo il nome all'oggetto
        self.__numero_soldati = numero_soldati  #salviamo il numero dei soldati come attributo privato


    def attacca(self):  #metodo per effettuare un attacco
        
        print(f"L'unità {self.nome} sta attaccando! ")  #stampiamo il messaggio di attacco


    def muovi(self):  #metodo per effettuare un movimento
        
        print(f"L'unità {self.nome} si sta muovendo! ")  #stampiamo il messaggio di movimento


    def ritira(self):  #metodo per effettuare una ritirata
        
        print(f"L'unità {self.nome} si sta ritirando strategicamente! ")  #stampiamo il messaggio di ritirata


    def __repr__(self):  #metodo speciale per rappresentare l'oggetto tramite una stringa
        
        return f"Un'unità {self.nome} con numero di soldati riservato."  #restituiamo le informazioni dell'unità senza mostrare i soldati


    def __eq__(self, altro):  #metodo speciale per confrontare due oggetti
        
        return self.nome == altro.nome and self.__numero_soldati == altro.__numero_soldati  #controlliamo che nome e numero dei soldati siano uguali


    def __getattribute__(self, attributo):  #metodo speciale per controllare l'accesso agli attributi

        if attributo == "numero_soldati":  #controlliamo se viene richiesto il numero dei soldati
            
            return "Informazione riservata!"  #nascondiamo l'informazione richiesta

        return object.__getattribute__(self, attributo)  #restituiamo normalmente tutti gli altri attributi



#CLASSI FIGLIE 

class Fanteria(UnitaMilitare):  #creiamo la classe Fanteria che eredita da UnitaMilitare

    def costruisci_trincea(self):  #metodo specifico della fanteria
        
        print(f"L'unità {self.nome} costruisce difese temporanee! ")  #stampiamo il messaggio della costruzione



class Artiglieria(UnitaMilitare):  #creiamo la classe Artiglieria che eredita da UnitaMilitare

    def calibra_artiglieria(self):  #metodo specifico dell'artiglieria
        
        print(f"L'unità {self.nome} calibra i pezzi di artiglieria per la precisione! ")  #stampiamo il messaggio della calibrazione



class Cavalleria(UnitaMilitare):  #creiamo la classe Cavalleria che eredita da UnitaMilitare

    def esplora_terreno(self):  #metodo specifico della cavalleria
        
        print(f"L'unità {self.nome} esplora l'area per raccogliere informazioni sul nemico! ")  #stampiamo il messaggio dell'esplorazione



class SupportoLogistico(UnitaMilitare):  #creiamo la classe SupportoLogistico che eredita da UnitaMilitare

    def rifornisci_unita(self):  #metodo specifico del supporto logistico
        
        print(f"L'unità {self.nome} sta effettuando il rifornimento e la manutenzione! ")  #stampiamo il messaggio del rifornimento



class Ricognizione(UnitaMilitare):  #creiamo la classe Ricognizione che eredita da UnitaMilitare

    def conduci_ricognizione(self):  #metodo specifico della ricognizione
        
        print(f"L'unità {self.nome} sta conducendo una missione di sorveglianza! ")  #stampiamo il messaggio della ricognizione



#CLASSE CONTROLLO MILITARE 

class ControlloMilitare(Fanteria, Artiglieria, Cavalleria, SupportoLogistico, Ricognizione):  #creiamo una classe che eredita da tutte le classi figlie

    def __init__(self, nome, numero_soldati):  #costruttore della classe ControlloMilitare
        
        super().__init__(nome, numero_soldati)  #richiamiamo il costruttore ereditato dalla classe padre
        self.unita_registrate = []  #creiamo una lista vuota per registrare le unità militari


    def registra_unita(self, unita):  #metodo per registrare una nuova unità militare

        if unita in self.unita_registrate:  #controlliamo se l'unità è già presente nella lista tramite __eq__
            
            print("Unità già registrata!")  #stampiamo un messaggio se l'unità esiste già

        else:  #caso in cui l'unità non è presente nella lista
            
            self.unita_registrate.append(unita)  #aggiungiamo l'oggetto alla lista delle unità registrate


    def mostra_unita(self):  #metodo per visualizzare tutte le unità registrate

        print("Ci sono le seguenti unità: ")  #stampiamo un messaggio introduttivo

        for unita in self.unita_registrate:  #scorriamo tutti gli oggetti presenti nella lista
            
            print(unita)  #stampiamo ogni oggetto utilizzando automaticamente __repr__


    def dettagli_unita(self, nome: str):  #metodo per cercare un'unità tramite il nome

        for unita in self.unita_registrate:  #scorriamo tutte le unità presenti nella lista

            if unita.nome == nome:  #controlliamo se il nome dell'unità corrisponde a quello cercato
                
                print(unita)  #stampiamo l'unità trovata tramite __repr__
                return  #terminiamo il metodo quando troviamo una corrispondenza

        print("Nessuna corrispondenza trovata! ")  #se terminiamo il ciclo senza trovare l'unità stampiamo il messaggio



#MENU PRINCIPALE

controllo = ControlloMilitare("Comando Militare", 0)  #creiamo l'oggetto che gestirà tutte le unità militari


while True:  #creiamo un menu ripetibile

    print("\n--- CONTROLLO MILITARE ---\n")  #stampiamo il titolo del menu
    print("1. Registra una nuova unità")  #prima operazione disponibile
    print("2. Mostra tutte le unità")  #seconda operazione disponibile
    print("3. Cerca un'unità")  #terza operazione disponibile
    print("0. Esci")  #opzione per uscire dal programma

    scelta = int(input("\nScegli un'operazione: "))  #prendiamo la scelta dell'utente


    match scelta:  #controlliamo quale operazione ha scelto l'utente

        case 1:  #caso in cui vogliamo registrare una nuova unità

            print("\n--- TIPOLOGIA UNITÀ ---\n")  #stampiamo il titolo del secondo menu
            print("1. Fanteria")  #prima tipologia di unità
            print("2. Artiglieria")  #seconda tipologia di unità
            print("3. Cavalleria")  #terza tipologia di unità
            print("4. Supporto Logistico")  #quarta tipologia di unità
            print("5. Ricognizione")  #quinta tipologia di unità

            tipo = int(input("\nScegli il tipo di unità: "))  #prendiamo la tipologia scelta dall'utente

            if tipo < 1 or tipo > 5:  #controlliamo se la scelta non è compresa tra 1 e 5
                
                print("Scelta non valida!")  #stampiamo un messaggio se la scelta non è valida
                continue  #torniamo all'inizio del menu principale

            nome = input("Inserisci il nome dell'unità: ")  #chiediamo il nome della nuova unità
            numero_soldati = int(input("Inserisci il numero dei soldati: "))  #chiediamo il numero dei soldati


            match tipo:  #controlliamo quale tipologia di unità dobbiamo creare

                case 1:  #caso in cui viene scelta la fanteria
                    
                    unita = Fanteria(nome, numero_soldati)  #creiamo un oggetto della classe Fanteria

                case 2:  #caso in cui viene scelta l'artiglieria
                    
                    unita = Artiglieria(nome, numero_soldati)  #creiamo un oggetto della classe Artiglieria

                case 3:  #caso in cui viene scelta la cavalleria
                    
                    unita = Cavalleria(nome, numero_soldati)  #creiamo un oggetto della classe Cavalleria

                case 4:  #caso in cui viene scelto il supporto logistico
                    
                    unita = SupportoLogistico(nome, numero_soldati)  #creiamo un oggetto della classe SupportoLogistico

                case 5:  #caso in cui viene scelta la ricognizione
                    
                    unita = Ricognizione(nome, numero_soldati)  #creiamo un oggetto della classe Ricognizione


            controllo.registra_unita(unita)  #richiamiamo il metodo per registrare l'oggetto nella lista


        case 2:  #caso in cui vogliamo visualizzare tutte le unità registrate

            controllo.mostra_unita()  #richiamiamo il metodo per stampare tutte le unità


        case 3:  #caso in cui vogliamo cercare una specifica unità

            nome = input("Inserisci il nome dell'unità da cercare: ")  #chiediamo il nome dell'unità da cercare

            controllo.dettagli_unita(nome)  #richiamiamo il metodo per cercare e stampare l'unità


        case 0:  #caso in cui vogliamo uscire dal programma

            print("Uscita dal programma.")  #stampiamo il messaggio di uscita
            break  #interrompiamo il ciclo while e terminiamo il programma


        case _:  #caso in cui viene inserita una scelta non prevista

            print("Scelta non valida!")  #stampiamo il messaggio di errore