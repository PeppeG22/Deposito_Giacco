
# ESERCIZIO - GESTIONE PRODUZIONE DI UNA FABBRICA

# come EXTRA ho aggiunto un metodo per incrementare il numero di pezzi 


# CLASSE PADRE

class Prodotto:

    def __init__(self, nome: str, pezzi: int = 0): #costruttore della classe
        
        self.nome = nome #nome del prodotto
        self.__pezzi = 0 #attributo privato della quantità
        self.set_pezzi(pezzi) #impostiamo la quantità tramite setter

    def get_pezzi(self): #getter per leggere il numero dei pezzi
        return self.__pezzi #restituiamo la quantità

    def set_pezzi(self, pezzi): #setter per modificare il numero dei pezzi

        if pezzi >= 0: #controlliamo che la quantità non sia negativa
            
            self.__pezzi = pezzi #aggiorniamo l'attributo privato
            return True #modifica effettuata correttamente

        else:
            return False #quantità non valida

    def __str__(self): #metodo speciale per stampare l'oggetto
        return f'Ci sono {self.get_pezzi()} pezzi del prodotto {self.nome}!'


# CLASSE FIGLIA

class ProdottoFabbricato(Prodotto): #ereditiamo dalla classe Prodotto

    def __init__(self, nome, pezzi): #costruttore della classe figlia
        
        super().__init__(nome, pezzi) #richiamiamo il costruttore del padre

    def modifica_quantita(self, nuova_quantita): #metodo per modificare la quantità
        return self.set_pezzi(nuova_quantita) #utilizziamo il setter ereditato

    def aggiungi_pezzi(self, quantita): #metodo extra per aumentare la produzione

        if quantita > 0: #controlliamo che la quantità sia positiva
            
            totale = self.get_pezzi() + quantita #sommiamo i nuovi pezzi a quelli esistenti
            self.set_pezzi(totale) #aggiorniamo la quantità tramite setter
            return True #operazione riuscita

        else:
            return False #quantità non valida


# CLASSE FABBRICA

class Fabbrica:

    def __init__(self): #costruttore della fabbrica
        self.prodotti = [] #lista che conterrà gli oggetti prodotti

    def aggiungi_prodotto(self): #metodo per aggiungere un prodotto

        nome = input('Inserisci il nome del prodotto: ') #chiediamo il nome
        pezzi = int(input('Inserisci quanti pezzi vuoi produrre: ')) #chiediamo la quantità

        if nome == "" or pezzi < 0: #controlliamo che i dati siano validi
            print('Dati del prodotto non validi!')
            return #interrompiamo il metodo

        for i in self.prodotti: #scorriamo gli oggetti già presenti
            if i.nome == nome: #controlliamo se il prodotto esiste già
                print('Prodotto già presente nella fabbrica!')
                return #evitiamo di inserire prodotti duplicati

        prodotto = ProdottoFabbricato(nome, pezzi) #creiamo l'oggetto della classe figlia
        self.prodotti.append(prodotto) #aggiungiamo l'oggetto alla lista
        print(f'Prodotto {nome} aggiunto con successo!')

    def stampa_prodotti(self): #metodo per visualizzare la produzione

        if len(self.prodotti) == 0: #controlliamo se la lista è vuota
            print('Non ci sono prodotti nella lista!')

        else:
            for prodotto in self.prodotti: #scorriamo gli oggetti della lista
                print(prodotto) #stampiamo l'oggetto tramite __str__

    def cerca_prodotto(self): #metodo per cercare un prodotto

        prodotto = input('Inserisci il prodotto da cercare: ') #chiediamo il nome

        for i in self.prodotti: #scorriamo tutti gli oggetti della lista
            if i.nome == prodotto: #confrontiamo il nome del prodotto
                print(f'Il prodotto {i.nome} è stato già fabbricato con {i.get_pezzi()} pezzi!')
                return #interrompiamo la ricerca

        else:
            print('Il prodotto non è ancora stato fabbricato!')

    def modifica(self): #metodo per modificare la quantità

        cerca = input('Quale prodotto vuoi modificare? ') #chiediamo il nome
        nuova_quantita = int(input('Inserisci la nuova quantità del prodotto: ')) #nuova quantità

        if nuova_quantita >= 0: #controlliamo che la quantità sia valida

            for i in self.prodotti: #scorriamo gli oggetti della lista
                if i.nome == cerca: #controlliamo se il nome corrisponde
                    i.modifica_quantita(nuova_quantita) #richiamiamo il metodo della classe figlia
                    print(f'Prodotto {cerca} modificato con successo!')
                    return #interrompiamo il metodo

            else:
                print(f'Prodotto {cerca} non trovato!')

        else:
            print('Quantità sbagliata!')

    def rimuovi(self): #metodo per eliminare un prodotto

        cerca = input('Quale prodotto vuoi eliminare? ') #chiediamo il nome

        for i in self.prodotti: #scorriamo tutti gli oggetti della lista
            
            if i.nome == cerca: #controlliamo se il nome corrisponde
                self.prodotti.remove(i) #eliminiamo l'oggetto dalla lista
                print(f'Prodotto {cerca} eliminato con successo!')
                return #interrompiamo il metodo

        else:
            print(f'Prodotto {cerca} non trovato!')

    def pezzi_totali(self): #metodo per calcolare il totale dei pezzi

        totale = 0 #inizializziamo la variabile per la somma

        for i in self.prodotti: #scorriamo tutti gli oggetti
            totale += i.get_pezzi() #sommiamo i pezzi tramite getter

        print(f'I pezzi totali prodotti sono: {totale}') #stampiamo il totale

    def aumenta_produzione(self): #metodo extra per aumentare la produzione

        cerca = input('Quale prodotto vuoi produrre nuovamente? ') #chiediamo il nome
        quantita = int(input('Quanti pezzi vuoi aggiungere? ')) #chiediamo i nuovi pezzi

        if quantita <= 0: #controlliamo che la quantità sia positiva
            print('Quantità non valida!')
            return #interrompiamo il metodo

        for i in self.prodotti: #scorriamo tutti gli oggetti
            
            if i.nome == cerca: #cerchiamo il prodotto selezionato
                i.aggiungi_pezzi(quantita) #richiamiamo il metodo della classe figlia
                print(f'Aggiunti {quantita} pezzi al prodotto {cerca}!')
                print(f'La nuova quantità è: {i.get_pezzi()}') #leggiamo il totale con getter
                return #interrompiamo il metodo

        else:
            print(f'Prodotto {cerca} non trovato!')


# CREAZIONE OGGETTO FABBRICA

fabbrica = Fabbrica() #creiamo l'oggetto che gestirà tutti i prodotti


# MENU PRINCIPALE

while True: #creiamo un menu ripetibile

    print("\n--- GESTIONE PRODUZIONE FABBRICA ---\n")
    print("1. Aggiungi prodotto")
    print("2. Visualizza produzione")
    print("3. Cerca prodotto")
    print("4. Modifica quantità")
    print("5. Rimuovi prodotto")
    print("6. Calcola totale pezzi prodotti")
    print("7. Aumenta produzione") #extra
    print("8. Esci")

    scelta = input("\nScegli un'operazione: ") #prendiamo la scelta dell'utente

    match scelta: #gestiamo le operazioni

        case "1": #aggiungiamo un prodotto
            fabbrica.aggiungi_prodotto() #richiamiamo il metodo

        case "2": #visualizziamo la produzione
            fabbrica.stampa_prodotti() #richiamiamo il metodo

        case "3": #cerchiamo un prodotto
            fabbrica.cerca_prodotto() #richiamiamo il metodo

        case "4": #modifichiamo la quantità
            fabbrica.modifica() #richiamiamo il metodo

        case "5": #rimuoviamo un prodotto
            fabbrica.rimuovi() #richiamiamo il metodo

        case "6": #calcoliamo il totale dei pezzi prodotti
            fabbrica.pezzi_totali() #richiamiamo il metodo

        case "7": #aumentiamo la produzione
            fabbrica.aumenta_produzione() #richiamiamo il nuovo metodo

        case "8": #usciamo dal programma
            print("Qui concludiamo")
            break #interrompiamo il ciclo while

        case _: #scelta non prevista
            print("Scelta non valida!")
