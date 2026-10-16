'''
DOMANDA 4:
Una classe è un modello che permette di creare degli oggetti ed è uno dei concetti fondamentali della programmazione OOP.
Ogni oggetto creato a partire da una classe è detto "istanza" e possiede gli attributi e i metodi definiti dalla classe.
Per definire una classe si utilizza la parola chiave class, seguita dal nome della classe che, per convenzione,
si scrive con la lettera iniziale maiuscola.
Ogni classe può possedere attributi e metodi. Gli attributi di istanza vengono generalmente definiti
nel costruttore __init__(), mentre i metodi definiscono le operazioni che gli oggetti possono eseguire.
Ogni oggetto possiede i propri attributi di istanza e può utilizzare i metodi della classe.
Self rappresenta l'istanza su cui stiamo lavorando e viene specificato sia nel costruttore
sia nei metodi di istanza della classe.
Permette di accedere agli attributi e ai metodi dell'oggetto e va inserito come primo parametro
dei metodi di istanza.

'''
'''
DOMANDA 5 : Cos'è l'ereditarietà? Come funziona? Spiegala.

L'ereditarietà è uno dei pilastri della programmazione OOP e permette a una classe di ereditare
attributi e metodi da un'altra classe. La classe da cui ereditiamo è chiamata superclasse (classe padre), mentre quella che eredita
è detta sottoclasse (classe figlia). La sottoclasse può utilizzare gli attributi e i metodi
della superclasse, aggiungere nuove funzionalità oppure modificare quelle già esistenti. 
Per definire l'ereditarietà si inserisce il nome della superclasse tra parentesi dopo
il nome della sottoclasse. Attraverso super() possiamo richiamare i metodi della classe padre,
in particolare il costruttore __init__(), per estenderne il comportamento senza riscrivere il codice.
Una sottoclasse può anche ridefinire un metodo già presente nella superclasse attraverso
l'overriding, modificandone il comportamento. Esiste l'ereditarietà multipla, che permette a una classe di ereditare attributi
e metodi da più superclassi contemporaneamente.
'''

'''
DOMANDA 10: Cos'è l'incapsulamento? Come funziona? Spiegalo.

L'incapsulamento è uno dei pilastri della programmazione OOP e consiste nell'organizzare
attributi e metodi di una classe, controllando l'accesso ai dati interni dell'oggetto.
Permette di decidere quali informazioni far vedere all'esterno e quali gestire attraverso
metodi specifici.
In Python distinguiamo tre livelli di visibilità degli attributi:
- Pubblico (self.nome): l'attributo è accessibile e modificabile direttamente dall'esterno.
- Protetto (self._nome): l'attributo è destinato all'utilizzo interno della classe, ma rimane accessibile dall'esterno.
- Privato (self.__nome): il doppio underscore rende meno immediato l'accesso all'attributo dall'esterno.
Per gestire gli attributi possiamo utilizzare i metodi getter e setter.
Il getter permette di leggere il valore di un attributo, mentre il setter consente
di modificarlo.
È importante ricordare che in Python gli attributi privati non sono completamente
inaccessibili, ma l'incapsulamento serve soprattutto a 'proteggerli' dall'esterno.

'''

'''
DOMANDA 11: Cos'è il polimorfismo? Come funziona? Spiegalo.

Il polimorfismo è la capacità degli oggetti di classi diverse di utilizzare lo stesso metodo, ma con comportamenti differenti.
Il polimorfismo consente quindi di richiamare un metodo con lo stesso nome su oggetti
diversi, ottenendo risultati differenti in base alla classe a cui appartiene l'oggetto.
Può essere realizzato attraverso l'ereditarietà e la sovrascrittura dei metodi (overriding). Una sottoclasse può infatti ridefinire
un metodo già presente nella superclasse, modificandone il comportamento.
Il polimorfismo può essere utilizzato anche senza ereditarietà, quando classi
diverse possiedono metodi con lo stesso nome per esempio.
In questo modo possiamo utilizzare oggetti differenti attraverso gli stessi
metodi, rendendo il codice riutilizzabile e semplice da gestire.


DOMANDA 13: Cosa sono le funzioni? Perché incarnano passivamente il concetto di astrazione?
Cos'è l'astrazione nella programmazione?

Le funzioni sono blocchi di codice riutilizzabili che permettono di eseguire
determinate operazioni. Vengono definite attraverso la parola chiave def,
possono ricevere dei parametri e restituire un risultato attraverso return.
Permettono di evitare la ripetizione del codice.
Le funzioni incarnano passivamente il concetto di astrazione perché permettono
di separare il codice di definizione da quello di richiamo. Possiamo infatti
definire una funzione in un punto del programma ed eseguirla in un altro,
senza dover conoscere ogni volta i dettagli del suo funzionamento.
L'astrazione è uno dei pilastri della programmazione OOP è la possibilità intrinseca di nascondere
i dettagli di un blocco, mostrando soltanto le funzionalità necessarie
per utilizzare un determinato elemento.
In Python l'astrazione può essere realizzata attraverso le classi astratte,
definite utilizzando ABC e il decoratore @abstractmethod.

'''

'''
DOMANDA 15 : Cos'è il controllo di flusso? Quali famiglie ne fanno parte?
Spiega gli elementi di queste famiglie teoricamente.

Il controllo di flusso è un meccanismo della programmazione che permette di gestire
l'ordine di esecuzione delle istruzioni attraverso condizioni e cicli.
In Python distinguiamo principalmente due famiglie: condizioni e cicli(o iterazioni).
Le strutture condizionali permettono di eseguire determinate istruzioni in base
a una condizione. Utilizziamo if per verificare una condizione, elif per aggiungere
ulteriori condizioni ed else quando nessuna delle precedenti è vera.
Possiamo inoltre utilizzare match/case per gestire diversi casi.
Le strutture iterative permettono invece di ripetere un blocco di codice.
Il ciclo for permette di scorrere gli elementi di una sequenza, mentre il ciclo
while ripete le istruzioni finché una condizione rimane vera.
All'interno dei cicli possiamo utilizzare break per interrompere il ciclo
e continue per passare all'iterazione successiva.
Esiste inoltre pass, che non esegue alcuna operazione e viene utilizzato
come segnaposto all'interno di un blocco di codice.
'''

