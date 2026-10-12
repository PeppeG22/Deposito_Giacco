
# ===================================================================================
#                      LE CLASSI IN PYTHON
# ===================================================================================
# -- Gli oggetto si scrivono sempre con la maiuscola, a differenza delle variabili--
# 1. COS'È UNA CLASSE?
# Una classe è un modello che permette di creare oggetti.
# Ogni oggetto può avere attributi (dati) e metodi (funzioni).
# Si utilizza la parola chiave class per definirla.


# 2. CREAZIONE DI UNA CLASSE

class Persona:

    def __init__(self, nome, eta):
        self.nome = nome  #attributo nome
        self.eta = eta    #attributo età

    def saluta(self):  #metodo della classe
        print(f'Ciao, mi chiamo {self.nome}')


# 3. IL METODO __init__()
# È il costruttore della classe.
# Viene eseguito automaticamente quando creiamo un oggetto.
# Serve per inizializzare gli attributi dell'oggetto.


# 4. LA PAROLA SELF
# self rappresenta l'oggetto su cui stiamo lavorando.
# Permette di accedere agli attributi e ai metodi dell'oggetto.
# Va inserito come primo parametro dei metodi di istanza.


# 5. CREAZIONE DI UN OGGETTO
# Un oggetto è un'istanza di una classe.

p1 = Persona('Mario', 25)  #creiamo un oggetto Persona
p2 = Persona('Luca', 30)   #creiamo un secondo oggetto


# 6. ACCESSO AGLI ATTRIBUTI
# Utilizziamo il punto per accedere ai dati dell'oggetto.

print(p1.nome)  #stampa Mario
print(p1.eta)   #stampa 25


# 7. RICHIAMARE UN METODO
# I metodi sono funzioni definite all'interno della classe.

p1.saluta()  #stampa Ciao, mi chiamo Mario


# 8. MODIFICARE UN ATTRIBUTO
# Possiamo modificare gli attributi dopo aver creato l'oggetto.

p1.eta = 26  #modifichiamo l'età di Mario
print(p1.eta)  #stampa 26


# 9. DIFFERENZA TRA CLASSE E OGGETTO
# Classe = modello generale (Persona)
# Oggetto = elemento concreto creato dalla classe (p1, p2)
# Attributo = caratteristica dell'oggetto (nome, eta)
# Metodo = azione che l'oggetto può eseguire (saluta)


# 10. EREDITARIETÀ
# Una classe può ereditare attributi e metodi da un'altra.
# La classe figlia può aggiungere nuove funzionalità.

class Studente(Persona):

    def studia(self):
        print(f'{self.nome} sta studiando Python')


s1 = Studente('Giuseppe', 26)  #creiamo uno studente
s1.saluta()  #metodo ereditato dalla classe Persona
s1.studia()  #metodo della classe Studente


# ============================================================
# RIEPILOGO
# ============================================================

# class       -> definisce una classe
# __init__    -> inizializza un nuovo oggetto
# self        -> rappresenta l'istanza corrente
# attributi   -> dati associati a un oggetto
# metodi      -> funzioni appartenenti a una classe
# oggetto     -> istanza concreta di una classe
# ereditarietà -> permette di riutilizzare una classe esistente

# NOTA: una classe organizza dati e funzioni in un'unica struttura.
# È uno dei concetti fondamentali della programmazione a oggetti (OOP).


# I METODI POSSONO ESSERE:

# -Di istanza: lavorano sull'oggetto 

# -Di classe: operano sulla classe, vengono definiti attraverso il decoratore
# @classmethod e ricevono come primo parametro cls

# -Statici: funzioni legate alla classe, non operano nè sull'istanza nè sulla classe
# @staticmethos

class Calcolatrice:
    
    @staticmethod #da usare quando vuoi che l'istanza sia indipendente dalla classe
    def somma(a, b):
        
        return a+b
    

risultato = Calcolatrice.somma(5,3)

print(risultato)
    