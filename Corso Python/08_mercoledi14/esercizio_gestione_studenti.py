
# ESERCIZIO - SISTEMA DI GESTIONE STUDENTI

# L'incapsulamento permette di controllare l'accesso agli attributi di una classe.
# Il name mangling modifica internamente i nomi degli attributi che iniziano con __.
# L'ereditarietà permette a una classe figlia di utilizzare attributi e metodi della classe padre.


# CLASSE PERSONA

class Persona:

    def __init__(self, nome, eta): #costruttore della classe
        
        self.__nome = nome #attributo privato del nome
        self.__eta = eta #attributo privato dell'età

    def get_nome(self): #getter per leggere il nome
        
        return self.__nome #restituiamo il nome

    def set_nome(self, nome): #setter per modificare il nome

        if nome != "": #controlliamo che il nome non sia vuoto
            
            self.__nome = nome #aggiorniamo il nome
            print("Nome modificato correttamente")

        else:
            
            print("Nome non valido")

    def get_eta(self): #getter per leggere l'età
        
        return self.__eta #restituiamo l'età

    def set_eta(self, eta): #setter per modificare l'età

        if eta < 0: #controlliamo che l'età non sia negativa
            
            print("Età non valida")

        else:
            
            self.__eta = eta #aggiorniamo l'età
            print("Età modificata correttamente")

    def presentazione(self): #metodo per presentare la persona
        
        print(f"Sono {self.__nome} e ho {self.__eta} anni")


# CLASSE STUDENTE

class Studente(Persona):

    def __init__(self, nome, eta, voti): #costruttore della classe figlia
        
        super().__init__(nome, eta) #richiamiamo il costruttore della classe Persona
        self.__voti = voti #attributo privato contenente la lista dei voti

    def calcola_media(self): #metodo per calcolare la media dei voti

        somma = 0 #inizializziamo la somma dei voti

        if len(self.__voti) == 0: #controlliamo se la lista è vuota
            
            return 0 #restituiamo 0 per evitare la divisione per zero

        else:

            for voto in self.__voti: #scorriamo tutti i voti della lista
                
                somma += voto #aggiungiamo ogni voto alla somma

            media = somma / len(self.__voti) #dividiamo la somma per il numero dei voti
            
            return media #restituiamo la media calcolata

    def stampa_studente(self): #metodo per stampare le informazioni dello studente

        print("Studente:", self.get_nome()) #leggiamo il nome tramite getter ereditato
        print("Età:", self.get_eta()) #leggiamo l'età tramite getter ereditato
        print("Media dei voti:", self.calcola_media()) #richiamiamo il metodo per la media


# CLASSE PROFESSORE

class Professore(Persona):

    def __init__(self, nome, eta, materia): #costruttore della classe figlia
        
        super().__init__(nome, eta) #inizializziamo nome ed età tramite la classe padre
        self.__materia = materia #attributo privato della materia insegnata

    def stampa_professore(self): #metodo per stampare le informazioni del professore

        print("Professore:", self.get_nome()) #getter ereditato dalla classe Persona
        print("Età:", self.get_eta()) #getter ereditato dalla classe Persona
        print("Materia insegnata:", self.__materia) #leggiamo l'attributo privato


# CREAZIONE DEGLI OGGETTI

persona1 = Persona("Michele", 32) #creiamo un oggetto della classe Persona

studente1 = Studente("Martina", 25, [21, 23, 28, 24]) #creiamo uno studente con una lista di voti

professore1 = Professore("Esposito", 57, "Inglese") #creiamo un professore con la materia


# STAMPA DEI RISULTATI

print("\nPRESENTAZIONE PERSONA")
persona1.presentazione() #richiamiamo il metodo della classe Persona

print("\nPRESENTAZIONE STUDENTE")
studente1.stampa_studente() #richiamiamo il metodo della classe Studente

print("\nPRESENTAZIONE PROFESSORE")
professore1.stampa_professore() #richiamiamo il metodo della classe Professore
