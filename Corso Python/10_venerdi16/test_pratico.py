
# CLASSE BASE - ELETTRODOMESTICO

class Elettrodomestico:  # creiamo la classe padre degli elettrodomestici

    def __init__(self, marca, modello, anno_acquisto, guasto):  # costruttore della classe
        self.__marca = marca  # attributo privato della marca
        self.__modello = modello  # attributo privato del modello
        self.__anno_acquisto = None  # inizializziamo l'anno, che controlleremo con il setter
        self.set_anno_acquisto(anno_acquisto)  # richiamiamo il setter per verificare l'anno
        self.__guasto = guasto  # attributo privato del guasto

    def get_marca(self):  # getter per leggere la marca
        return self.__marca  # restituiamo la marca

    def set_marca(self, marca):  # setter per modificare la marca
        self.__marca = marca  # aggiorniamo la marca

    def get_modello(self):  # getter per leggere il modello
        return self.__modello  # restituiamo il modello

    def set_modello(self, modello):  # setter per modificare il modello
        self.__modello = modello  # aggiorniamo il modello

    def get_anno_acquisto(self):  # getter per leggere l'anno di acquisto
        return self.__anno_acquisto  # restituiamo l'anno

    def set_anno_acquisto(self, anno_acquisto):  # setter per modificare l'anno
        if type(anno_acquisto) == int and 1950 <= anno_acquisto <= 2026:  # controlliamo l'anno
            self.__anno_acquisto = anno_acquisto  # salviamo l'anno se è valido
        else:  # caso in cui l'anno non sia valido
            raise ValueError("Anno di acquisto non valido!")  # blocchiamo l'inserimento non valido

    def get_guasto(self):  # getter per leggere il guasto
        return self.__guasto  # restituiamo il guasto

    def set_guasto(self, guasto):  # setter per modificare il guasto
        self.__guasto = guasto  # aggiorniamo il guasto

    def descrizione(self):  # metodo richiesto per descrivere l'elettrodomestico
        return f"Marca: {self.__marca}, Modello: {self.__modello}, Anno: {self.__anno_acquisto}, Guasto: {self.__guasto}"  # restituiamo la descrizione

    def __str__(self):  # metodo speciale usato quando stampiamo l'oggetto
        return self.descrizione()  # richiamiamo la descrizione senza riscriverla

    def stima_costo_base(self):  # metodo con il costo base generico
        return 50  # restituiamo il costo base della diagnosi


# CLASSE FIGLIA - LAVATRICE

class Lavatrice(Elettrodomestico):  # ereditiamo attributi e metodi da Elettrodomestico

    def __init__(self, marca, modello, anno_acquisto, guasto, capacita_kg, giri_centrifuga):  # costruttore
        super().__init__(marca, modello, anno_acquisto, guasto)  # richiamiamo il costruttore della classe padre
        self.__capacita_kg = capacita_kg  # attributo privato della capacità
        self.__giri_centrifuga = giri_centrifuga  # attributo privato dei giri

    def get_capacita_kg(self):  # getter della capacità
        return self.__capacita_kg  # restituiamo la capacità

    def set_capacita_kg(self, capacita_kg):  # setter della capacità
        self.__capacita_kg = capacita_kg  # aggiorniamo la capacità

    def get_giri_centrifuga(self):  # getter dei giri della centrifuga
        return self.__giri_centrifuga  # restituiamo i giri

    def set_giri_centrifuga(self, giri_centrifuga):  # setter dei giri della centrifuga
        self.__giri_centrifuga = giri_centrifuga  # aggiorniamo i giri

    def stima_costo_base(self):  # sovrascriviamo il metodo della classe padre (overriding)
        costo_base = super().stima_costo_base()  # partiamo dal costo generico di 50 euro
        if self.__capacita_kg > 7:  # controlliamo se la lavatrice ha capacità elevata
            costo_base += 20  # aggiungiamo 20 euro al costo base
        return costo_base  # restituiamo il costo finale


# CLASSE FIGLIA - FRIGORIFERO

class Frigorifero(Elettrodomestico):  # ereditiamo dalla classe Elettrodomestico

    def __init__(self, marca, modello, anno_acquisto, guasto, litri, ha_freezer):  # costruttore
        super().__init__(marca, modello, anno_acquisto, guasto)  # inizializziamo gli attributi della classe padre
        self.__litri = litri  # attributo privato dei litri
        self.__ha_freezer = ha_freezer  # attributo privato booleano del freezer

    def get_litri(self):  # getter dei litri
        return self.__litri  # restituiamo i litri

    def set_litri(self, litri):  # setter dei litri
        self.__litri = litri  # aggiorniamo i litri

    def get_ha_freezer(self):  # getter per verificare la presenza del freezer
        return self.__ha_freezer  # restituiamo True o False

    def set_ha_freezer(self, ha_freezer):  # setter del freezer
        self.__ha_freezer = ha_freezer  # aggiorniamo il valore

    def stima_costo_base(self):  # sovrascriviamo il metodo per il frigorifero
        costo_base = super().stima_costo_base()  # prendiamo il costo generico della classe padre
        if self.__ha_freezer:  # controlliamo se il frigorifero ha il freezer
            costo_base += 30  # aggiungiamo 30 euro
        if self.__litri > 200:  # controlliamo se la capacità supera 200 litri
            costo_base += 20  # aggiungiamo altri 20 euro
        return costo_base  # restituiamo il costo finale


# CLASSE FIGLIA - FORNO

class Forno(Elettrodomestico):  # ereditiamo dalla classe Elettrodomestico

    def __init__(self, marca, modello, anno_acquisto, guasto, tipo_alimentazione, ha_ventilato):  # costruttore
        super().__init__(marca, modello, anno_acquisto, guasto)  # richiamiamo il costruttore del padre
        self.__tipo_alimentazione = tipo_alimentazione  # attributo privato del tipo di alimentazione
        self.__ha_ventilato = ha_ventilato  # attributo privato che indica se il forno è ventilato

    def get_tipo_alimentazione(self):  # getter del tipo di alimentazione
        return self.__tipo_alimentazione  # restituiamo il tipo

    def set_tipo_alimentazione(self, tipo_alimentazione):  # setter del tipo di alimentazione
        self.__tipo_alimentazione = tipo_alimentazione  # aggiorniamo il tipo

    def get_ha_ventilato(self):  # getter della funzione ventilata
        return self.__ha_ventilato  # restituiamo True o False

    def set_ha_ventilato(self, ha_ventilato):  # setter della funzione ventilata
        self.__ha_ventilato = ha_ventilato  # aggiorniamo il valore

    def stima_costo_base(self):  # sovrascriviamo il metodo per il forno
        costo_base = super().stima_costo_base()  # partiamo dal costo della classe padre
        if self.__tipo_alimentazione == "gas":  # controlliamo se il forno è a gas
            costo_base += 20  # aggiungiamo 20 euro
        if self.__ha_ventilato:  # controlliamo se il forno è ventilato
            costo_base += 15  # aggiungiamo 15 euro
        return costo_base  # restituiamo il costo finale


# CLASSE - TICKET RIPARAZIONE

class TicketRiparazione:  # classe per gestire il ticket di un elettrodomestico

    def __init__(self, id_ticket, elettrodomestico):  # costruttore della classe
        self.__id_ticket = id_ticket  # attributo privato dell'ID
        self.__elettrodomestico = elettrodomestico  # memorizziamo l'oggetto da riparare
        self.__stato = "aperto"  # ogni nuovo ticket parte dallo stato aperto
        self.__note = []  # creiamo la lista inizialmente vuota delle note

    def get_id_ticket(self):  # getter dell'ID
        return self.__id_ticket  # restituiamo l'ID

    def get_elettrodomestico(self):  # getter dell'elettrodomestico
        return self.__elettrodomestico  # restituiamo l'oggetto associato al ticket

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

    def calcola_preventivo(self, *voci_extra):  # metodo variadico che accetta più importi
        costo_base = self.__elettrodomestico.stima_costo_base()  # richiamiamo il metodo dell'oggetto (polimorfismo)
        totale = costo_base + sum(voci_extra)  # sommiamo al costo base tutte le voci extra
        return totale  # restituiamo il preventivo finale


# CLASSE - OFFICINA

class Officina:  # classe che gestisce tutti i ticket dell'officina

    def __init__(self, nome):  # costruttore dell'officina
        self.nome = nome  # attributo del nome dell'officina
        self.tickets = []  # lista in cui memorizziamo i ticket

    def aggiungi_ticket(self, ticket):  # metodo per inserire un nuovo ticket
        if not isinstance(ticket, TicketRiparazione):  # verifichiamo che l'oggetto sia un ticket
            print("Oggetto non valido: inserisci un ticket!")  # comunichiamo l'errore
            return  # interrompiamo il metodo
        for presente in self.tickets:  # scorriamo i ticket già presenti
            if presente.get_id_ticket() == ticket.get_id_ticket():  # verifichiamo che l'ID sia univoco
                print("Esiste già un ticket con questo ID!")  # comunichiamo il duplicato
                return  # evitiamo di aggiungere il ticket due volte
        self.tickets.append(ticket)  # aggiungiamo il ticket alla lista

    def chiudi_ticket(self, id_ticket):  # metodo per chiudere un ticket usando il suo ID
        for ticket in self.tickets:  # scorriamo tutti i ticket
            if ticket.get_id_ticket() == id_ticket:  # cerchiamo quello con l'ID richiesto
                ticket.set_stato("chiuso")  # impostiamo lo stato su chiuso
                return  # usciamo dal metodo dopo aver trovato il ticket
        else:
            print("Ticket non trovato!")  # messaggio se nessun ID corrisponde

    def stampa_ticket_aperti(self):  # metodo per stampare i ticket non ancora chiusi
        for ticket in self.tickets:  # scorriamo la lista dei ticket
            if ticket.get_stato() != "chiuso":  # controlliamo che il ticket non sia chiuso
                elettrodomestico = ticket.get_elettrodomestico()  # recuperiamo l'oggetto associato
                if type(elettrodomestico) == Lavatrice:  # controlliamo se è una lavatrice
                    tipo = "Lavatrice"  # assegniamo il tipo lavatrice
                elif type(elettrodomestico) == Frigorifero:  # controlliamo se è un frigorifero
                    tipo = "Frigorifero"  # assegniamo il tipo frigorifero
                elif type(elettrodomestico) == Forno:  # controlliamo se è un forno
                    tipo = "Forno"  # assegniamo il tipo forno
                else:  # se è un altro elettrodomestico
                    tipo = "Elettrodomestico"  # assegniamo il tipo generico
                print(f"ID Ticket: {ticket.get_id_ticket()}, Tipo: {tipo}, Stato: {ticket.get_stato()}")  # stampiamo i dati

    def totale_preventivi(self):  # metodo che somma i preventivi di tutti i ticket
        tot_cost = 0  # inizializziamo il totale a zero
        for ticket in self.tickets:  # scorriamo la lista dei ticket
            tot_cost += ticket.calcola_preventivo()  # aggiungiamo il preventivo base di ogni ticket
        return tot_cost  # restituiamo il totale

    def statistiche_per_tipo(self):  # metodo per contare i ticket secondo il tipo di elettrodomestico
        lavatrici = 0  # contatore dei ticket delle lavatrici
        frigoriferi = 0  # contatore dei ticket dei frigoriferi
        forni = 0  # contatore dei ticket dei forni
        for ticket in self.tickets:  # scorriamo tutti i ticket
            elettrodomestico = ticket.get_elettrodomestico()  # recuperiamo l'elettrodomestico associato
            if type(elettrodomestico) == Lavatrice:  # controlliamo se è una lavatrice
                lavatrici += 1  # aumentiamo il contatore delle lavatrici
            elif type(elettrodomestico) == Frigorifero:  # controlliamo se è un frigorifero
                frigoriferi += 1  # aumentiamo il contatore dei frigoriferi
            elif type(elettrodomestico) == Forno:  # controlliamo se è un forno
                forni += 1  # aumentiamo il contatore dei forni
        print(f"Numero di ticket per lavatrici: {lavatrici}")  # stampiamo il primo risultato
        print(f"Numero di ticket per frigoriferi: {frigoriferi}")  # stampiamo il secondo risultato
        print(f"Numero di ticket per forni: {forni}")  # stampiamo il terzo risultato


# UTILIZZIAMO IL PROGRAMMA

officina = Officina("Officina elettrodomestici")  # creiamo un oggetto Officina

lavatrice = Lavatrice("Bosch", "Serie 6", 2022, "Non centrifuga", 8, 1200)  # creiamo una lavatrice
frigorifero = Frigorifero("Samsung", "Cool", 2023, "Non raffredda", 300, True)  # creiamo un frigorifero
forno = Forno("Smeg", "Classic", 2021, "Non scalda", "gas", True)  # creiamo un forno

ticket1 = TicketRiparazione(1, lavatrice)  # associamo la lavatrice al ticket 1
ticket2 = TicketRiparazione(2, frigorifero)  # associamo il frigorifero al ticket 2
ticket3 = TicketRiparazione(3, forno)  # associamo il forno al ticket 3

ticket1.aggiungi_nota("Controllare il motore")  # aggiungiamo una nota al primo ticket
ticket1.set_stato("in lavorazione")  # modifichiamo lo stato del primo ticket

officina.aggiungi_ticket(ticket1)  # inseriamo il primo ticket nell'officina
officina.aggiungi_ticket(ticket2)  # inseriamo il secondo ticket nell'officina
officina.aggiungi_ticket(ticket3)  # inseriamo il terzo ticket nell'officina

print("\nELETTRODOMESTICI")  # stampiamo un titolo
print(lavatrice)  # richiamiamo automaticamente il metodo __str__()
print(frigorifero)  # stampiamo la descrizione del frigorifero
print(forno)  # stampiamo la descrizione del forno

print("\nPREVENTIVI")  # stampiamo il titolo dei preventivi
print("Ticket 1 con voci extra:", ticket1.calcola_preventivo(15, 10), "euro")  # esempio di metodo variadico
print("Ticket 2:", ticket2.calcola_preventivo(), "euro")  # preventivo senza costi extra
print("Ticket 3:", ticket3.calcola_preventivo(), "euro")  # altro preventivo

print("\nTOTALE PREVENTIVI BASE:", officina.totale_preventivi(), "euro")  # sommiamo i costi base dei ticket

print("\nTICKET NON CHIUSI")  # stampiamo un titolo
officina.stampa_ticket_aperti()  # stampiamo i ticket aperti o in lavorazione

officina.chiudi_ticket(2)  # chiudiamo il secondo ticket
print("\nTICKET NON CHIUSI DOPO LA CHIUSURA DEL TICKET 2")  # stampiamo un nuovo titolo
officina.stampa_ticket_aperti()  # controlliamo che il ticket 2 non venga più mostrato

print("\nSTATISTICHE PER TIPO")  # stampiamo un titolo
officina.statistiche_per_tipo()  # contiamo i ticket in base alla classe degli elettrodomestici
