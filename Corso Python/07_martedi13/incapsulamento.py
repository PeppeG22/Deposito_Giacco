'''
INCAPSULAMENTO IN PYTHON

L'incapsulamento è la capacità di mostrare solo ciò che è necessario,
decidendo quali informazioni rendere accessibili dall'esterno e quali mantenere
interne alla classe.

Serve a proteggere gli attributi e controllare come vengono letti e modificati.

Esistono tre tipi di attributi:

1. PUBBLICI: self.nome
   Sono accessibili e modificabili direttamente dall'esterno.

2. PROTETTI: self._nome
   Utilizzano un underscore e, per convenzione, dovrebbero essere utilizzati
   solo all'interno della classe e delle sue sottoclassi.

3. PRIVATI: self.__nome
   Utilizzano due underscore e non sono accessibili direttamente
   dall'esterno con il loro nome originale.

GETTER E SETTER:

GETTER (get): metodo che permette di leggere un attributo privato.
Utilizza generalmente return per restituire il valore.

SETTER (set): metodo che permette di modificare un attributo privato.
Possiamo inserire delle condizioni per controllare il valore prima di modificarlo.

METODI PRIVATI:

Anche i metodi possono essere privati utilizzando due underscore (__).
Sono destinati all'utilizzo interno della classe.

INDENTAZIONE:

L'indentazione definisce i blocchi di codice.
Più un'istruzione è indentata, più si trova all'interno di altri blocchi.
Non indica però il livello di privacy di un attributo.

'''


#ESEMPIO DI INCAPSULAMENTO - ATTRIBUTI PRIVATI, GETTER E SETTER

class Parametri_privati:  #creiamo una classe con un attributo privato

    def __init__(self, nome):  #costruttore della classe
        self.__nome = nome  #creiamo un attributo privato utilizzando due underscore


    #GETTER E SETTER

    def get_nome(self):  #metodo getter per leggere il nome
        return self.__nome  #restituiamo il valore dell'attributo privato


    def set_nome(self, nome_nuovo):  #metodo setter per modificare il nome

        if len(nome_nuovo) == 0:  #controlliamo se il nome inserito è vuoto
            print("Sei un pippo!")  #stampiamo un messaggio se il nome non è valido

        else:  #caso in cui il nome è valido
            self.__nome = nome_nuovo  #modifichiamo l'attributo privato
            self.__metodo_privato()  #richiamiamo il metodo privato della classe


    #METODO PRIVATO

    def __metodo_privato(self):  #creiamo un metodo privato utilizzando due underscore
        print("Sono dentro")  #stampiamo un messaggio quando viene richiamato



#CREAZIONE DELL'OGGETTO

o_pp = Parametri_privati("Mirko")  #creiamo un oggetto della classe

print(o_pp.get_nome())  #utilizziamo il getter per leggere il nome

o_pp.set_nome("Giuseppe")  #utilizziamo il setter per modificare il nome

print(o_pp.get_nome())  #verifichiamo che il nome sia stato modificato

o_pp.set_nome("")  #proviamo a inserire un nome vuoto

print(o_pp.get_nome())  #verifichiamo che il nome sia rimasto invariato


'''
RISULTATO:

Mirko
Sono dentro
Giuseppe
Sei un pippo!
Giuseppe

Il getter permette di leggere __nome senza accedervi direttamente.

Il setter controlla il nuovo valore attraverso len().
Se il nome è vuoto, non viene modificato.
Se il nome è valido, viene aggiornato e viene richiamato il metodo privato.

Il doppio underscore attiva il name mangling: non garantisce una
privacy assoluta, ma evita l'accesso accidentale con il nome originale.
'''