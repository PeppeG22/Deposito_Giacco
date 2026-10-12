
# ============================================================
#               METODI SPECIALI IN PYTHON
# ============================================================

# I metodi speciali sono metodi che iniziano e finiscono con __
# Vengono chiamati anche DUNDER METHODS (double underscore).
# Permettono di definire il comportamento degli oggetti.
# Python li richiama automaticamente in determinate operazioni.


# 1. METODO __str__()
# Serve per rappresentare un oggetto sotto forma di stringa.
# Viene richiamato automaticamente quando utilizziamo print().
# Deve restituire una stringa tramite return.

class Persona:
    def __init__(self, nome, eta):
        self.nome = nome  #inizializziamo il nome
        self.eta = eta  #inizializziamo l'età

    def __str__(self):  #metodo per rappresentare l'oggetto
        return f'{self.nome} ha {self.eta} anni'


p1 = Persona('Mario', 25)  #creiamo un oggetto Persona
print(p1)  #stampa Mario ha 25 anni

# Senza __str__, print(p1) mostrerebbe una rappresentazione
# predefinita dell'oggetto, invece delle sue informazioni.


# 2. METODO __len__()
# Serve per definire la lunghezza di un oggetto.
# Viene richiamato automaticamente attraverso len().
# Deve restituire un numero intero maggiore o uguale a 0.

class Biblioteca:
    def __init__(self):
        self.libri = []  #creiamo una lista vuota di libri

    def aggiungi(self, libro):  #metodo per aggiungere un libro
        self.libri.append(libro)  #aggiungiamo il libro alla lista

    def __len__(self):  #metodo per contare i libri
        return len(self.libri)  #restituiamo il numero di libri


b1 = Biblioteca()  #creiamo un oggetto Biblioteca

b1.aggiungi('Harry Potter')  #aggiungiamo un libro
b1.aggiungi('Il Signore degli Anelli')  #aggiungiamo un altro libro

print(len(b1))  #stampa 2

# Python richiama automaticamente b1.__len__()
# quando scriviamo len(b1).


# 3. METODO __call__()
# Permette di utilizzare un oggetto come se fosse una funzione.
# Viene richiamato quando scriviamo oggetto().
# Può ricevere dei parametri e restituire un risultato.

class Moltiplicatore:
    def __init__(self, numero):
        self.numero = numero  #inizializziamo il moltiplicatore

    def __call__(self, valore):  #rendiamo l'oggetto richiamabile
        return self.numero * valore  #restituiamo il prodotto


m1 = Moltiplicatore(3)  #creiamo un oggetto che moltiplica per 3

print(m1(5))  #stampa 15
print(m1(10))  #stampa 30

# Normalmente richiamiamo un metodo con oggetto.metodo().
# Con __call__ possiamo richiamare direttamente oggetto().
# In questo caso m1(5) equivale a m1.__call__(5).


# ============================================================
#                 ALTRI METODI SPECIALI
# ============================================================

# __init__()  -> inizializza un oggetto quando viene creato.
# __repr__()  -> restituisce una rappresentazione tecnica dell'oggetto.
# __eq__()    -> definisce il confronto tra oggetti con ==.
# __lt__()    -> definisce il confronto tra oggetti con <.
# __gt__()    -> definisce il confronto tra oggetti con >.
# __add__()   -> definisce il comportamento dell'operatore +.
# __sub__()   -> definisce il comportamento dell'operatore -.
# __getitem__() -> permette di accedere agli elementi con [indice].
# __setitem__() -> permette di modificare elementi con [indice].
# __contains__() -> definisce il comportamento dell'operatore in.


# ============================================================
#                       RIEPILOGO
# ============================================================

# __str__  -> print(oggetto)  -> restituisce una stringa.
# __len__  -> len(oggetto)    -> restituisce la lunghezza.
# __call__ -> oggetto()       -> esegue l'oggetto come funzione.

# I metodi speciali si definiscono all'interno delle classi.
# Il loro primo parametro è normalmente self.
# Python li richiama automaticamente quando necessario.
