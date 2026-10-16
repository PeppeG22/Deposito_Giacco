
# PROGETTO DI GRUPPO - GIUSEPPE - VALENTINA
# Andiamo a creare un sistema che permetta di gestire l'inserimento di ticket di richieste che possono essere gestiti in CRUD (create, read, update, delete)
# Inoltre ci deve essere una classe utente che può inserire e vedere, e una admin che può modificare ed eliminare oltreché risolvere i ticket ovvero chiuderli e salvarli
# in una lista ticket chiusi, è obbligatorio usare le tre regole fondamentali
# Una repository per gruppo. Presentazione 15 min a gruppo.

# CLASSE TICKET

class Ticket:  # classe per gestire un ticket di richiesta

    def __init__(self, id_ticket):  # costruttore della classe
        self.__id_ticket = id_ticket  # attributo privato dell'ID
        self.__stato = "aperto"  # ogni nuovo ticket parte dallo stato aperto
        self.__note = []  # creiamo la lista inizialmente vuota delle note

    def get_id_ticket(self):  # getter dell'ID
        return self.__id_ticket  # restituiamo l'ID

    def get_stato(self):  # getter dello stato
        return self.__stato  # restituiamo lo stato attuale

    def set_stato(self, stato):  # setter per modificare lo stato
        if stato in ["aperto", "in lavorazione", "chiuso"]:  # controlliamo che lo stato sia valido
            self.__stato = stato  # aggiorniamo lo stato
        else:  # se il valore non è consentito
            print("Stato non valido!")  # comunichiamo l'errore

    def get_note(self):  # getter per leggere le note
        return self.__note.copy()  # restituiamo una copia per evitare modifiche dall'esterno

    def set_note(self, note):  # setter per sostituire la lista delle note
        if type(note) == list:  # controlliamo che il valore sia una lista
            self.__note = note.copy()  # salviamo una copia delle note
        else:  # se il valore non è una lista
            print("Le note devono essere una lista!")  # comunichiamo l'errore

    def aggiungi_nota(self, testo):  # metodo per aggiungere una nota
        self.__note.append(testo)  # inseriamo la nota nella lista

    def __str__(self):  # metodo speciale per personalizzare la stampa dell'oggetto
        return f'Il ticket con id {self.get_id_ticket()} è in stato {self.get_stato()}'  # restituiamo ID e stato


# CLASSE UTENTE

class Utente:  # classe per gestire le operazioni dell'utente

    def __init__(self, tickets):  # costruttore della classe utente
        self.tickets = tickets  # utilizziamo la lista dei ticket condivisa

    def read(self):  # metodo per visualizzare i ticket
        for ticket in self.tickets:  # scorriamo tutti i ticket presenti nella lista
            print(ticket.get_id_ticket(), ticket.get_stato())  # stampiamo ID e stato del ticket

    def aggiungi_ticket(self, ticket):  # metodo per inserire un nuovo ticket
        for i in self.tickets:  # scorriamo i ticket già presenti
            if i.get_id_ticket() == ticket.get_id_ticket():  # verifichiamo che l'ID sia univoco nella lista
                print("Esiste già un ticket con questo ID!")  # comunichiamo il duplicato
                return  # evitiamo di aggiungere il ticket due volte

        self.tickets.append(ticket)  # aggiungiamo il ticket alla lista


# CLASSE ADMIN

class Admin(Utente):  # classe amministratore che eredita dalla classe Utente

    def __init__(self, tickets):  # costruttore della classe Admin
        super().__init__(tickets)  # richiamiamo il costruttore della classe padre
        self.ticket_chiusi = []  # creiamo la lista dei ticket chiusi

    def chiudi_ticket(self, id_ticket):  # metodo per chiudere un ticket usando il suo ID
        for ticket in self.tickets:  # scorriamo tutti i ticket
            if ticket.get_id_ticket() == id_ticket:  # cerchiamo quello con l'ID richiesto
                ticket.set_stato("chiuso")  # impostiamo lo stato su chiuso
                self.ticket_chiusi.append(ticket)  # aggiungiamo il ticket alla lista dei chiusi
                self.tickets.remove(ticket)  # rimuoviamo il ticket dalla lista degli attivi
                return  # usciamo dal metodo dopo aver trovato il ticket
        else:  # caso in cui il ciclo termina senza trovare il ticket
            print("Ticket non trovato!")  # messaggio se nessun ID corrisponde

    def elimina_ticket(self, id_ticket):  # metodo per eliminare un ticket usando il suo ID
        for ticket in self.tickets:  # scorriamo tutti i ticket
            if ticket.get_id_ticket() == id_ticket:  # cerchiamo quello con l'ID richiesto
                self.tickets.remove(ticket)  # eliminiamo il ticket dalla lista
                return  # usciamo dal metodo dopo aver trovato il ticket
        else:  # caso in cui il ciclo termina senza trovare il ticket
            print("Ticket non trovato!")  # messaggio se nessun ID corrisponde

    def modifica_stato(self, id_ticket):  # metodo per modificare lo stato del ticket
        
        for ticket in self.tickets:  # scorriamo tutti i ticket
            if ticket.get_id_ticket() == id_ticket:  # cerchiamo quello con l'ID richiesto
                if ticket.get_stato().lower() == 'aperto':  # controlliamo se il ticket è aperto
                    ticket.set_stato('in lavorazione')  # modifichiamo lo stato del ticket
                    return  # usciamo dal metodo dopo la modifica
                else:  # caso in cui il ticket non sia aperto
                    print('Stato non modificabile!')  # comunichiamo che lo stato non può essere modificato
                    return  # interrompiamo il metodo
        else:  # caso in cui il ciclo termina senza trovare il ticket
            print("Ticket non trovato!")  # messaggio se nessun ID corrisponde

    def stampa(self):  # metodo per visualizzare i ticket chiusi
        for i in self.ticket_chiusi:  # scorriamo la lista dei ticket chiusi
            print(i)  # stampiamo il ticket attraverso il metodo __str__


# CREAZIONE DEGLI OGGETTI

tickets = []  # creiamo la lista condivisa dei ticket

utente = Utente(tickets)  # creiamo l'oggetto utente
admin = Admin(tickets)  # creiamo l'oggetto amministratore


# MENU PRINCIPALE

while True:  # menu ripetibile

    print("\n------------MENU------------")  # stampiamo il titolo del menu
    print("BENVENUTO NELL'INTERFACCIA TICKET!")  # messaggio iniziale
    print("1. Aggiungi ticket")  # operazione per creare un ticket
    print("2. Elimina ticket")  # operazione per eliminare un ticket
    print("3. Chiudi ticket")  # operazione per chiudere un ticket
    print("4. Modifica stato")  # operazione per modificare lo stato
    print("5. Leggi ticket")  # operazione per leggere i ticket
    print("6. Stampa ticket chiusi")  # operazione per visualizzare i ticket chiusi
    print("0. Esci")  # operazione per uscire dal programma

    scelta = int(input("Scegli un'operazione: "))  # prendiamo la scelta dell'utente

    if scelta == 0:  # caso in cui usciamo dal menu
        print("Arrivederci!")  # messaggio di uscita
        break  # interrompiamo il ciclo

    elif scelta == 1:  # aggiungiamo un nuovo ticket
        nuovo_id = int(input("Inserisci il nuovo id: "))  # chiediamo l'ID del nuovo ticket
        ticket = Ticket(nuovo_id)  # creiamo un oggetto Ticket
        utente.aggiungi_ticket(ticket)  # inseriamo il ticket nella lista

    elif scelta == 2:  # eliminiamo un ticket
        nuovo_id = int(input("Inserisci l'id che vuoi eliminare: "))  # chiediamo l'ID del ticket
        admin.elimina_ticket(nuovo_id)  # richiamiamo il metodo elimina

    elif scelta == 3:  # chiudiamo un ticket
        nuovo_id = int(input("Inserisci l'id che vuoi chiudere: "))  # chiediamo l'ID del ticket
        admin.chiudi_ticket(nuovo_id)  # richiamiamo il metodo chiudi

    elif scelta == 4:  # modifichiamo lo stato di un ticket
        nuovo_id = int(input("Inserisci l'id di cui vuoi modificare lo stato: "))  # chiediamo l'ID del ticket
        admin.modifica_stato(nuovo_id)  # richiamiamo il metodo modifica

    elif scelta == 5:  # visualizziamo i ticket attivi
        utente.read()  # richiamiamo il metodo read

    elif scelta == 6:  # visualizziamo i ticket chiusi
        admin.stampa()  # richiamiamo il metodo stampa

    else:  # caso in cui viene inserita una scelta non prevista
        print("Nessuna scelta valida!")  # comunichiamo l'errore
