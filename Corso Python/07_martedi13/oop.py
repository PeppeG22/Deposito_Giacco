'''
Le tre regole fondamentali dell'OOP:

1. Incapsulamento: la capacità di nascondere e proteggere alcuni elementi del codice,
   controllando l'accesso agli attributi e ai metodi di una classe.

2. Ereditarietà: la capacità di generare una classe figlia a partire da una classe padre,
   creando una gerarchia tra le classi e permettendo di riutilizzare attributi e metodi.

3. Polimorfismo: la capacità di un elemento di cambiare forma o comportamento,
   mantenendo la stessa interfaccia per il sistema.


----> ALLA BASE DELL'OOP C'È L'ASTRAZIONE:
      la capacità di rappresentare soltanto le caratteristiche essenziali
      di un elemento, nascondendo i dettagli non necessari.


EREDITARIETÀ:

Una sottoclasse eredita attributi e metodi da un'altra classe, chiamata SUPERCLASSE.

- Superclasse: classe padre da cui ereditiamo.
- Sottoclasse: classe figlia che eredita.

La sottoclasse può utilizzare i metodi della superclasse oppure modificarli.


SUPER():

super() permette di richiamare i metodi della superclasse, in particolare
il costruttore __init__(), per estenderne il comportamento senza riscrivere il codice.

Può essere utilizzato anche per richiamare un metodo della superclasse
che è stato sovrascritto nella sottoclasse.


SOVRASCRITTURA DEI METODI (OVERRIDING):

Una sottoclasse può ridefinire un metodo già presente nella superclasse.

Il metodo viene sovrascritto e può comportarsi in maniera diversa
rispetto a quello della classe padre.


EREDITARIETÀ MULTIPLA:

Una classe può ereditare attributi e metodi da più superclassi contemporaneamente.

Esempio:

class Automobile(Veicolo, DotazioniSpeciali):

In questo caso Automobile eredita da entrambe le classi.


ESEMPIO CON SUPER():

class Automobile(Veicolo):

    def __init__(self, marca, modello, cavalli):
        super().__init__(marca, modello)
        self.cavalli = cavalli

In questo modo richiamiamo il costruttore di Veicolo
e aggiungiamo l'attributo cavalli.

'''


#ESERCIZIO - EREDITARIETÀ MULTIPLA

class Veicolo:

    def __init__(self, marca, modello):
        self.marca = marca  #inizializziamo la marca
        self.modello = modello  #inizializziamo il modello

    def mostra_informazioni(self):  #metodo per mostrare le informazioni del veicolo
        print(f"Veicolo marca {self.marca}, modello {self.modello}")


class DotazioniSpeciali:

    def __init__(self, dotazioni):
        self.dotazioni = dotazioni  #inizializziamo le dotazioni

    def mostra_dotazioni(self):  #metodo per mostrare le dotazioni speciali
        print(f"Dotazioni speciali: {', '.join(self.dotazioni)}")


#creiamo la classe Automobile che eredita da Veicolo e DotazioniSpeciali

class Automobile(Veicolo, DotazioniSpeciali):

    def __init__(self, marca, modello, dotazioni, cavalli):

        Veicolo.__init__(self, marca, modello)  #richiamiamo il costruttore di Veicolo
        DotazioniSpeciali.__init__(self, dotazioni)  #richiamiamo il costruttore di DotazioniSpeciali

        self.cavalli = cavalli  #aggiungiamo l'attributo cavalli

    def mostra_informazioni(self):  #sovrascriviamo il metodo della superclasse
        super().mostra_informazioni()  #richiamiamo il metodo di Veicolo
        print(f'Cavalli: {self.cavalli}')  #stampiamo i cavalli
        self.mostra_dotazioni()  #richiamiamo il metodo ereditato da DotazioniSpeciali


#CREAZIONE DEGLI OGGETTI

auto1 = Automobile('BMW', 'Serie 3', ['Navigatore', 'Sensori di parcheggio'], 190)

auto2 = Automobile('Audi', 'A4', ['Cambio automatico', 'Telecamera posteriore'], 204)

auto3 = Automobile('Mercedes', 'Classe A', ['Fari LED', 'Sedili riscaldati'], 150)


#STAMPA DELLE INFORMAZIONI

print('\nAUTOMOBILE 1')
auto1.mostra_informazioni()

print('\nAUTOMOBILE 2')
auto2.mostra_informazioni()

print('\nAUTOMOBILE 3')
auto3.mostra_informazioni()