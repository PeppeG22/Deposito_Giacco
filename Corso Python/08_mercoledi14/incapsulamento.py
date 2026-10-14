
# PROGRAMMAZIONE A OGGETTI - INCAPSULAMENTO


# 1. INCAPSULAMENTO

# L'incapsulamento consiste nell'organizzare attributi e metodi
# di una classe, controllando l'accesso ai dati interni dell'oggetto.
# Permette di decidere quali informazioni esporre all'esterno
# e quali gestire attraverso metodi specifici.

# Ad esempio, in un conto bancario il saldo non dovrebbe essere
# modificato liberamente, ma attraverso metodi come:
# deposita() -> aggiunge denaro controllando che l'importo sia valido.
# preleva() -> sottrae denaro verificando che il saldo sia sufficiente.

# In questo modo possiamo mantenere coerenti i dati dell'oggetto.

# IMPORTANTE:
# In Python un attributo privato non è completamente inaccessibile.
# L'incapsulamento serve soprattutto a evitare modifiche accidentali.


# 2. VISIBILITA' DEGLI ATTRIBUTI

# In Python distinguiamo tre livelli di accesso agli attributi.

# PUBBLICO -> self.nome
# È accessibile e modificabile direttamente dall'esterno.
# Si utilizza attraverso oggetto.nome.

# PROTETTO -> self._nome
# Il singolo underscore indica che l'attributo è destinato
# principalmente all'utilizzo interno della classe.
# Rimane accessibile dall'esterno: è una convenzione.

# PRIVATO -> self.__nome
# Il doppio underscore iniziale attiva il name mangling,
# rendendo meno immediato l'accesso dall'esterno.

# ATTENZIONE:
# __nome__ con due underscore iniziali e finali
# identifica normalmente un metodo speciale, come __init__.


# ESEMPIO:

class Persona:

    def __init__(self, nome, eta, codice):
        self.nome = nome             #attributo pubblico
        self._eta = eta              #attributo protetto per convenzione
        self.__codice = codice       #attributo privato con name mangling


persona = Persona("Mario", 20, 1234)  #creiamo un'istanza della classe

print(persona.nome)                 #Mario, accesso pubblico
print(persona._eta)                 #20, accesso possibile ma sconsigliato

# print(persona.__codice)           #AttributeError, nome non accessibile così


# 3. NAME MANGLING

# Il name mangling è un meccanismo di Python che modifica
# internamente il nome di un attributo preceduto da __.

# Ad esempio, nella classe Esempio:
# self.__valore diventa internamente _Esempio__valore.

# Il dato rimane accessibile tecnicamente,
# ma viene ridotto il rischio di modificarlo accidentalmente.


# ESEMPIO:

class Esempio:

    def __init__(self):
        self.__valore = 10           #creiamo un attributo privato

    def get_valore(self):            #metodo pubblico per leggere il valore
        return self.__valore         #possiamo accedere al dato dall'interno


oggetto = Esempio()                  #creiamo un'istanza

print(oggetto.get_valore())          #10, accesso tramite metodo pubblico

# print(oggetto.__valore)            #AttributeError

print(oggetto._Esempio__valore)      #10, accesso possibile tramite nome trasformato

# È preferibile utilizzare get_valore() invece del nome trasformato.
# Il name mangling non garantisce una protezione assoluta.

# Se Padre e Figlia definiscono entrambi __valore,
# Python genera due nomi differenti per evitare conflitti.
# I metodi ereditati dal padre possono comunque accedere
# ai suoi attributi privati.


# 4. GETTER E SETTER

# Getter e setter sono metodi che permettono di leggere
# e modificare gli attributi di un oggetto in modo controllato.

# GETTER:
# Permette di ottenere il valore di un attributo.
# Generalmente viene chiamato get_nomeAttributo().

# SETTER:
# Permette di modificare il valore di un attributo,
# effettuando eventuali controlli prima dell'assegnazione.
# Generalmente viene chiamato set_nomeAttributo().

# get_ e set_ sono convenzioni, non parole chiave di Python.


# ESEMPIO:

class Persona:

    def __init__(self, nome, eta):
        self.nome = nome             #attributo pubblico
        self.__eta = eta             #attributo privato

    def get_eta(self):               #getter per leggere l'età
        return self.__eta            #restituiamo il valore tramite return

    def set_eta(self, nuova_eta):    #setter che riceve la nuova età

        if nuova_eta < 0:            #controlliamo che il valore sia valido
            print("Età non valida")
            return                   #interrompiamo il metodo senza modificare l'età

        self.__eta = nuova_eta       #aggiorniamo il valore se è valido


persona = Persona("Mario", 20)       #creiamo una persona di 20 anni

print(persona.get_eta())            #20, leggiamo l'età tramite getter

persona.set_eta(25)                 #modifichiamo l'età tramite setter
print(persona.get_eta())            #25, stampiamo il nuovo valore

persona.set_eta(-5)                 #Età non valida, il controllo blocca la modifica
print(persona.get_eta())            #25, il valore rimane invariato

# Il getter restituisce un dato con return.
# Il setter modifica il dato soltanto se supera i controlli.
# Non è obbligatorio creare un setter per ogni attributo.


# 5. INCAPSULAMENTO CON DEPOSITO E PRELIEVO

# Un attributo può essere leggibile tramite getter,
# ma modificabile soltanto attraverso operazioni specifiche.

# In questo esempio proteggiamo il saldo di un conto bancario
# e permettiamo di modificarlo soltanto tramite deposita() e preleva().


# ESEMPIO:

class Conto:

    def __init__(self, saldo):
        self.__saldo = saldo         #creiamo il saldo privato

    def get_saldo(self):             #getter per leggere il saldo
        return self.__saldo

    def deposita(self, importo):     #metodo per aggiungere denaro

        if importo <= 0:             #l'importo deve essere positivo
            print("Importo non valido")
            return                   #interrompiamo il deposito

        self.__saldo += importo      #aggiungiamo l'importo al saldo

    def preleva(self, importo):      #metodo per prelevare denaro

        if importo <= 0 or importo > self.__saldo:  #controlliamo l'importo e il saldo
            print("Prelievo non consentito")
            return                   #blocchiamo il prelievo non valido

        self.__saldo -= importo      #sottraiamo l'importo dal saldo


conto = Conto(100)                   #creiamo un conto con 100 euro

conto.deposita(50)                   #aggiungiamo 50 euro, saldo 150
conto.preleva(30)                    #preleviamo 30 euro, saldo 120

print(conto.get_saldo())             #120, leggiamo il saldo con il getter

# Non creiamo set_saldo() perché vogliamo modificare il saldo
# soltanto attraverso i metodi che eseguono i controlli.


# 6. ATTRIBUTI DI CLASSE E ATTRIBUTI DI ISTANZA

# ATTRIBUTO DI CLASSE:
# Viene definito direttamente all'interno della classe,
# ma fuori dai metodi, e può essere condiviso da tutte le istanze.

# ATTRIBUTO DI ISTANZA:
# Viene generalmente definito tramite self dentro __init__.
# Ogni oggetto possiede il proprio valore.


# ESEMPIO:

class Studente:

    scuola = "Istituto Python"       #attributo di classe condiviso

    def __init__(self, nome):
        self.nome = nome             #attributo di istanza
        self.voti = []               #creiamo una lista distinta per ogni studente


s1 = Studente("Mario")               #creiamo il primo studente
s2 = Studente("Luca")                #creiamo il secondo studente

print(s1.scuola)                     #Istituto Python
print(s2.scuola)                     #Istituto Python, stesso attributo di classe

s1.voti.append(30)                   #aggiungiamo un voto soltanto a Mario

print(s1.voti)                       #[30]
print(s2.voti)                       #[], la lista di Luca è indipendente

# ATTENZIONE:
# Se definiamo una lista direttamente nella classe,
# questa può essere condivisa tra più istanze.

# PARAMETRI PREDEFINITI:
# Possiamo assegnare un valore predefinito a un parametro.

# Esempio: def __init__(self, nome="Non indicato"):
# Se non inseriamo il nome, Python utilizza il valore predefinito.


# 7. VARIABILI GLOBALI, LOCALI E NONLOCAL

# VARIABILE GLOBALE:
# È definita fuori dalle funzioni, a livello del modulo.

# VARIABILE LOCALE:
# È definita dentro una funzione e appartiene al suo ambito.

# NONLOCAL:
# Permette a una funzione interna di modificare
# una variabile della funzione esterna.

# GLOBAL:
# Permette di assegnare a una variabile globale
# dall'interno di una funzione.


# ESEMPIO:

numero = 10                          #variabile globale

def funzione_esterna():

    numero = 5                       #variabile locale della funzione esterna

    def funzione_interna():

        nonlocal numero              #utilizziamo la variabile della funzione esterna
        numero = 3                   #modifichiamo il valore da 5 a 3
        print(numero)                #3

    funzione_interna()               #eseguiamo la funzione interna
    print(numero)                    #3, il valore locale è stato modificato


print(numero)                        #10, leggiamo la variabile globale
funzione_esterna()                   #eseguiamo la funzione esterna
print(numero)                        #10, la variabile globale non è cambiata

# global si riferisce alla variabile globale del modulo.
# nonlocal si riferisce a una variabile di una funzione esterna.


# 8. GLOBAL E RETURN

# global e return hanno due funzionamenti differenti.

# global permette di assegnare a una variabile globale
# direttamente dall'interno di una funzione.

# return restituisce un risultato al punto che ha chiamato
# la funzione, senza modificare automaticamente la variabile esterna.


# ESEMPIO CON RETURN:

def aggiungi_punto(punti):
    return punti + 1                 #restituiamo il valore aumentato di 1


punteggio = 0                        #valore iniziale
punteggio = aggiungi_punto(punteggio) #assegniamo il risultato restituito
print(punteggio)                     #1


# ESEMPIO CON GLOBAL:

punteggio = 0                        #variabile globale

def aggiungi_punto_globale():

    global punteggio                 #indichiamo che vogliamo modificare la globale
    punteggio += 1                   #aumentiamo direttamente il valore


aggiungi_punto_globale()             #eseguiamo la funzione
print(punteggio)                     #1, la variabile globale è stata modificata

# Generalmente è preferibile passare i dati come parametri
# e restituire il risultato utilizzando return.


# 9. DECORATORI - @property

# @property è un decoratore che permette di definire un getter
# e accedere al valore come se fosse un normale attributo.

# @nome_property.setter permette di definire il setter,
# controllando le modifiche effettuate sul valore.

# In questo modo non dobbiamo chiamare esplicitamente
# metodi come get_eta() e set_eta().


# ESEMPIO:

class Persona:

    def __init__(self, eta):
        self.__eta = eta             #creiamo un attributo privato

    @property                       #decoratore che definisce il getter
    def eta(self):
        return self.__eta            #restituiamo l'attributo privato

    @eta.setter                     #decoratore che definisce il setter
    def eta(self, nuova_eta):        #riceviamo il nuovo valore

        if nuova_eta < 0:            #controlliamo che l'età sia valida
            print("Età non valida")
            return                   #blocchiamo la modifica

        self.__eta = nuova_eta       #aggiorniamo il valore privato


persona = Persona(20)                #creiamo una persona di 20 anni

print(persona.eta)                   #20, richiama il getter senza parentesi

persona.eta = 25                     #richiama automaticamente il setter
print(persona.eta)                   #25, leggiamo il nuovo valore

persona.eta = -5                     #Età non valida, il setter blocca la modifica
print(persona.eta)                   #25, il valore rimane invariato

# Con @property utilizziamo persona.eta invece di persona.get_eta().
# Con @eta.setter utilizziamo persona.eta = 25 invece di set_eta(25).
# Se definiamo soltanto @property, senza setter,
# non possiamo assegnare un nuovo valore attraverso la proprietà.
