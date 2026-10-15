
# ASTRAZIONE E CLASSI ASTRATTE

# 1. ASTRAZIONE

# L'astrazione è uno dei quattro principi della programmazione a oggetti.
# Permette di definire il codice in un punto e utilizzarlo in un altro,
# separando la definizione delle operazioni dal loro utilizzo.

# Più precisamente, permette di mostrare COSA deve fare un oggetto,
# nascondendo i dettagli di COME viene eseguita l'operazione.

# In Python possiamo realizzare l'astrazione attraverso le classi astratte.


# 2. CLASSI ASTRATTE

# Una classe astratta è una classe che definisce una struttura comune
# che le classi figlie devono seguire.

# CARATTERISTICHE PRINCIPALI:

# - Non può essere istanziata se contiene metodi astratti non implementati.
# - Può contenere attributi, costruttori e metodi normali.
# - Può contenere metodi astratti che le classi figlie devono implementare.
# - Le classi figlie possono essere istanziate se implementano tutti
#   i metodi astratti ereditati.

# ATTENZIONE:
# Ereditare da ABC non basta per rendere una classe non istanziabile.
# Deve essere presente almeno un metodo astratto non implementato.


# 3. MODULO ABC E DECORATORE @abstractmethod

# La libreria standard di Python contiene il modulo abc,
# che fornisce i meccanismi per definire le classi astratte.

# ABC -> classe base da cui ereditiamo per creare una classe astratta.
# @abstractmethod -> decoratore per dichiarare un metodo astratto.

# Il modulo abc contiene ABC e abstractmethod.
# Il modulo collections.abc contiene invece classi base astratte
# già definite per oggetti come liste, sequenze e altre collezioni.


from abc import ABC, abstractmethod #importiamo la classe ABC e il decoratore


# 4. CREAZIONE DI UNA CLASSE ASTRATTA

class Pippo_Astratto(ABC): #creiamo una classe che eredita da ABC

    @abstractmethod #indichiamo che il metodo è astratto
    def saluta(self): #definiamo il metodo che i figli dovranno implementare
        pass #non definiamo ancora il comportamento del metodo


# CLASSE FIGLIA

class Pippo(Pippo_Astratto): #ereditiamo dalla classe astratta

    def saluta(self): #implementiamo il metodo astratto del padre
        print("Ciao, sono Pippo!") #definiamo il comportamento del metodo


# CREAZIONE OGGETTO

# oggetto = Pippo_Astratto() #ERRORE: non possiamo istanziare la classe astratta

oggetto = Pippo() #creiamo un'istanza della classe figlia
oggetto.saluta() #richiamiamo il metodo implementato e stampiamo il messaggio


# 5. OBBLIGO DI IMPLEMENTARE I METODI ASTRATTI

# Quando una classe figlia eredita un metodo astratto,
# deve implementarlo per poter creare oggetti della classe.

# Implementare significa definire concretamente il comportamento
# del metodo dichiarato nella classe astratta.

# Se il figlio non implementa tutti i metodi astratti,
# rimane una classe astratta e non può essere istanziato.

# @abstractmethod va scritto sopra il metodo da rendere astratto.
# pass indica semplicemente che non eseguiamo alcuna istruzione.

# Un metodo normale della classe padre, invece, può essere
# utilizzato direttamente dai figli senza essere riscritto.


# 6. ESEMPIO PRATICO - SISTEMA DI PAGAMENTI

# Creiamo una classe astratta MetodoPagamento che stabilisce
# che ogni metodo di pagamento deve poter effettuare un pagamento.

# Le classi figlie definiranno COME effettuare il pagamento.


# CLASSE ASTRATTA

class MetodoPagamento(ABC): #classe astratta che eredita da ABC

    @abstractmethod #rendiamo obbligatoria l'implementazione del metodo
    def effettua_pagamento(self, importo): #metodo comune ai pagamenti
        pass #il comportamento verrà definito dalle classi figlie

    def messaggio(self): #metodo normale, non astratto
        print("Operazione di pagamento") #può essere ereditato senza modifiche


# CLASSE FIGLIA CARTA DI CREDITO

class CartaDiCredito(MetodoPagamento): #ereditiamo dalla classe astratta

    def effettua_pagamento(self, importo): #implementiamo il metodo obbligatorio
        print(f"Pagamento con carta di {importo} euro")


# CLASSE FIGLIA PAYPAL

class Paypal(MetodoPagamento): #ereditiamo dalla classe astratta

    def effettua_pagamento(self, importo): #implementiamo il metodo obbligatorio
        print(f"Pagamento con PayPal di {importo} euro")


# CREAZIONE DEGLI OGGETTI

carta = CartaDiCredito() #creiamo un oggetto della classe figlia
paypal = Paypal() #creiamo un altro oggetto della classe figlia

carta.messaggio() #richiamiamo il metodo normale ereditato
carta.effettua_pagamento(50) #pagamento con carta di 50 euro

paypal.messaggio() #richiamiamo lo stesso metodo ereditato
paypal.effettua_pagamento(30) #pagamento con PayPal di 30 euro


# 7. COLLEGAMENTO CON EREDITARIETA' E POLIMORFISMO

# EREDITARIETA':
# CartaDiCredito e Paypal ereditano dalla classe MetodoPagamento.

# ASTRAZIONE:
# La classe astratta stabilisce quali operazioni devono essere disponibili.

# OVERRIDING:
# Le classi figlie ridefiniscono effettua_pagamento().

# POLIMORFISMO:
# Possiamo chiamare lo stesso metodo su oggetti diversi
# ottenendo comportamenti differenti.


# ESEMPIO DI POLIMORFISMO

pagamenti = [carta, paypal] #creiamo una lista contenente due oggetti diversi

for pagamento in pagamenti: #scorriamo gli oggetti della lista
    pagamento.effettua_pagamento(100) #ogni oggetto esegue la propria versione del metodo


# 8. DIFFERENZA TRA CLASSE NORMALE E CLASSE ASTRATTA

# CLASSE NORMALE:
# Possiamo creare direttamente oggetti della classe.
# I figli possono ereditare e sovrascrivere i metodi.

# CLASSE ASTRATTA:
# Definisce una struttura comune e può imporre metodi obbligatori.
# Non possiamo istanziarla se ha metodi astratti non implementati.
# I figli devono implementare tutti i metodi astratti per essere istanziabili.

# IMPORTANTE:
# Non tutti i metodi di una classe astratta devono essere astratti.
# Possiamo avere sia metodi normali sia metodi con @abstractmethod.

# super() può essere utilizzato anche nelle classi astratte
# per richiamare il costruttore o altri metodi ereditati.
