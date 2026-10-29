
# ==========================================================
# LEZIONE 29 OTTOBRE - ALBERI DI DECISIONE
# ==========================================================

# Gli alberi di decisione (Decision Tree) sono algoritmi
# di Machine Learning supervisionato.

# Possono essere utilizzati sia per problemi di classificazione
# sia per problemi di regressione.

# DecisionTreeClassifier:
# Viene utilizzato per prevedere una classe o categoria.

# DecisionTreeRegressor:
# Viene utilizzato per prevedere un valore numerico continuo.

# Un albero di decisione funziona attraverso una sequenza
# di domande sulle caratteristiche (feature) del dataset.

# Ogni domanda permette di dividere le osservazioni
# in gruppi sempre più omogenei.

# L'obiettivo è separare il meglio possibile le classi
# per arrivare a una previsione finale.


# ==========================================================
# 1. STRUTTURA DI UN ALBERO DI DECISIONE
# ==========================================================

# Un albero di decisione è composto da:

# NODO RADICE (ROOT):
# È il primo nodo dell'albero.
# Contiene la prima domanda utilizzata per dividere i dati.
# Tutte le osservazioni inizialmente passano da questo nodo.

# NODI INTERNI:
# Sono i nodi intermedi dell'albero.
# Contengono altre domande sulle caratteristiche.
# Ogni domanda permette di dividere ulteriormente i dati.

# RAMI:
# Rappresentano le possibili risposte alle domande.
# Per esempio, se una condizione è vera seguiamo un ramo,
# mentre se è falsa seguiamo l'altro.

# FOGLIE (LEAVES):
# Sono i nodi terminali dell'albero.
# Non contengono ulteriori divisioni.
# Restituiscono la previsione finale del modello.

# PROFONDITÀ (DEPTH):
# Indica il numero massimo di divisioni lungo
# il percorso dalla radice a una foglia.

# Ogni nodo interno contiene una condizione.
# Se la condizione è vera, seguiamo un ramo.
# Se è falsa, seguiamo l'altro.

# ESEMPIO:

# Prima domanda:
# Età <= 30?

# Se VERO:
# Seguiamo il ramo sinistro.

# Se FALSO:
# Seguiamo il ramo destro.

# Il procedimento continua fino a raggiungere una foglia.


# ==========================================================
# 2. COME FUNZIONA UN ALBERO DI DECISIONE
# ==========================================================

# Il modello analizza le caratteristiche disponibili.

# Per ogni caratteristica cerca una soglia
# che permetta di separare il meglio possibile le classi.

# Ogni divisione prende il nome di SPLIT.

# Il modello sceglie lo split che produce
# la maggiore riduzione dell'impurità.

# Questo procedimento viene ripetuto nei nodi successivi.

# L'obiettivo è ottenere gruppi il più possibile puri,
# cioè composti prevalentemente da osservazioni
# appartenenti alla stessa classe.

# ESEMPIO:

# Abbiamo 10 vini:
# 5 vini appartenenti alla classe 0.
# 5 vini appartenenti alla classe 1.

# Il gruppo iniziale contiene entrambe le classi.
# Quindi presenta una certa impurità.

# L'albero potrebbe trovare una caratteristica
# che permette di dividere i vini in due gruppi:

# Gruppo A: 5 vini della classe 0.
# Gruppo B: 5 vini della classe 1.

# I due gruppi ottenuti sono completamente puri.

# Nella realtà non sempre è possibile ottenere
# gruppi perfettamente separati.


# ==========================================================
# 3. IMPURITÀ DI UN NODO
# ==========================================================

# L'impurità misura quanto sono mescolate
# le diverse classi all'interno di un nodo.

# Un nodo è PURO quando tutte le osservazioni
# appartengono alla stessa classe.

# Un nodo è IMPURO quando contiene osservazioni
# appartenenti a classi differenti.

# ESEMPIO:

# 10 vini della stessa classe:
# Il nodo è completamente puro.

# 5 vini della classe 0 e 5 della classe 1:
# Il nodo è molto impuro.

# Per misurare l'impurità possiamo utilizzare:
# 1. Indice di Gini.
# 2. Entropia.

# Entrambi permettono al Decision Tree di scegliere
# le divisioni migliori durante l'addestramento.


# ==========================================================
# 4. INDICE DI GINI
# ==========================================================

# L'indice di Gini misura quanto sono mescolate
# le classi all'interno di un nodo.

# GINI = 0:
# Tutte le osservazioni appartengono alla stessa classe.
# Il nodo è completamente puro.

# GINI = 0.5:
# Nel caso di due classi, rappresenta l'impurità massima.
# Si verifica quando il nodo contiene il 50% di una classe
# e il 50% dell'altra.

# ESEMPIO:

# 10 vini della classe 0:
# Gini = 0.

# 5 vini della classe 0 e 5 della classe 1:
# Gini = 0.5.

# 8 vini della classe 0 e 2 della classe 1:
# Gini = 0.32.

# FORMULA:
# Gini = 1 - somma delle probabilità delle classi al quadrato.

# ATTENZIONE:
# Nei problemi con più di due classi,
# il valore massimo di Gini può essere superiore a 0.5.

# L'albero cerca divisioni che riducano
# il più possibile l'impurità di Gini.

# Nel DecisionTreeClassifier il criterio Gini
# è quello utilizzato per impostazione predefinita.


# ==========================================================
# 5. ENTROPIA
# ==========================================================

# L'entropia misura il livello di incertezza
# sulla classe a cui appartiene un'osservazione.

# ENTROPIA = 0:
# Tutte le osservazioni appartengono alla stessa classe.
# Non abbiamo incertezza sulla classe.

# ENTROPIA ALTA:
# Le classi sono molto mescolate.
# È più difficile prevedere correttamente la classe.

# ESEMPIO:

# 10 vini della classe 0:
# Entropia = 0.

# 5 vini della classe 0 e 5 della classe 1:
# Entropia = 1.

# 8 vini della classe 0 e 2 della classe 1:
# Entropia = circa 0.72.

# FORMULA:
# Entropia = - somma di p * log2(p)
# Dove p rappresenta la proporzione di ogni classe.

# Il valore massimo dipende dal numero di classi.

# L'albero cerca divisioni che riducano
# l'entropia dei gruppi ottenuti.


# ==========================================================
# 6. DIFFERENZA TRA GINI ED ENTROPIA
# ==========================================================

# GINI:
# Misura quanto sono mescolate le classi.
# Utilizza i quadrati delle probabilità.
# È generalmente più veloce da calcolare.

# ENTROPIA:
# Misura quanto è incerta l'appartenenza a una classe.
# Utilizza i logaritmi delle probabilità.
# È generalmente leggermente più complessa da calcolare.

# ENTRAMBI:
# Servono a valutare la qualità delle divisioni.
# Cercano di produrre gruppi più puri.
# Possono portare a costruire alberi differenti.

# ATTENZIONE:
# Non possiamo confrontare direttamente i valori
# numerici di Gini ed Entropia perché hanno scale diverse.

# Non esiste un criterio sempre migliore dell'altro.
# Le prestazioni dipendono dal dataset.


# ==========================================================
# 7. IPERPARAMETRI PRINCIPALI
# ==========================================================

# Gli iperparametri sono valori che impostiamo
# prima di addestrare il modello.

# criterion:
# Indica il criterio utilizzato per misurare
# la qualità delle divisioni.

# criterion="gini":
# Utilizza l'indice di Gini.

# criterion="entropy":
# Utilizza l'entropia.

# max_depth:
# Indica la profondità massima dell'albero.

# max_depth=2:
# L'albero può effettuare al massimo due livelli
# di divisione a partire dalla radice.

# min_samples_split:
# Indica il numero minimo di osservazioni necessarie
# per poter dividere ulteriormente un nodo.

# min_samples_leaf:
# Indica il numero minimo di osservazioni
# che devono rimanere in ogni foglia.

# random_state:
# Permette di rendere riproducibili
# le scelte casuali dell'algoritmo.

# ATTENZIONE:
# Un albero con profondità molto elevata
# può adattarsi eccessivamente ai dati di training.

# Un albero troppo poco profondo
# potrebbe invece essere troppo semplice.


# ==========================================================
# 8. OVERFITTING E UNDERFITTING NEGLI ALBERI
# ==========================================================

# OVERFITTING:
# Si verifica quando l'albero diventa troppo complesso.
# Riesce a classificare molto bene i dati di training,
# ma può commettere più errori sui dati nuovi.

# Un albero molto profondo può creare numerose divisioni
# e imparare anche il rumore presente nel dataset.

# Questo comportamento è associato ad alta varianza.

# UNDERFITTING:
# Si verifica quando l'albero è troppo semplice.
# Non riesce a individuare le relazioni importanti
# presenti nelle caratteristiche del dataset.

# Questo comportamento è associato ad alto bias.

# Per controllare la complessità possiamo utilizzare:
# max_depth.
# min_samples_split.
# min_samples_leaf.

# L'obiettivo è trovare un equilibrio
# tra accuratezza e capacità di generalizzazione.


# ==========================================================
# 9. COME ADDESTRARE UN DECISION TREE
# ==========================================================

from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split

# Carichiamo il dataset dei vini
dataset = load_wine()

# Separiamo le caratteristiche dalle etichette
X = dataset.data
y = dataset.target

# Dividiamo i dati in 75% training e 25% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,
    random_state=0
)

# Creiamo il modello utilizzando Gini
modello = DecisionTreeClassifier(
    criterion="gini",
    max_depth=2,
    random_state=0
)

# Addestriamo il modello
modello.fit(X_train, y_train)

# Effettuiamo le previsioni
y_pred = modello.predict(X_test)

# Calcoliamo l'accuracy sui dati di training
accuracy_train = modello.score(X_train, y_train)

# Calcoliamo l'accuracy sui dati di test
accuracy_test = modello.score(X_test, y_test)

# Stampiamo i risultati
print("Accuracy training:", round(accuracy_train, 4))
print("Accuracy test:", round(accuracy_test, 4))

# Estraiamo le regole dell'albero
regole = export_text(
    modello,
    feature_names=list(dataset.feature_names)
)

# Stampiamo le regole
print("\nREGOLE DELL'ALBERO")
print(regole)


# ==========================================================
# 10. METODI PRINCIPALI DEL DECISION TREE
# ==========================================================

# DecisionTreeClassifier():
# Crea un modello di classificazione ad albero decisionale.

# fit(X_train, y_train):
# Addestra il modello sui dati di training.

# predict(X_test):
# Effettua le previsioni sui dati nuovi.

# score(X_test, y_test):
# Calcola l'accuracy del classificatore.

# export_text():
# Permette di visualizzare le regole dell'albero
# sotto forma di testo.

# feature_names:
# Permette di visualizzare i nomi delle caratteristiche
# invece di utilizzare soltanto i loro indici.


# ==========================================================
# 11. RIEPILOGO FINALE
# ==========================================================

# DECISION TREE:
# Algoritmo che effettua previsioni attraverso
# una sequenza di domande sulle caratteristiche.

# NODO RADICE:
# Prima domanda dell'albero.

# NODI INTERNI:
# Domande successive che dividono ulteriormente i dati.

# RAMI:
# Percorsi seguiti in base alle risposte.

# FOGLIE:
# Nodi terminali che restituiscono la previsione.

# PROFONDITÀ:
# Numero di livelli di divisione lungo un percorso.

# SPLIT:
# Divisione dei dati in gruppi differenti.

# IMPURITÀ:
# Misura quanto sono mescolate le classi.

# GINI:
# Misura l'impurità delle classi.

# ENTROPIA:
# Misura l'incertezza sull'appartenenza a una classe.

# MAX_DEPTH:
# Controlla la profondità massima dell'albero.

# OVERFITTING:
# Modello troppo complesso, rischio di alta varianza.

# UNDERFITTING:
# Modello troppo semplice, rischio di alto bias.

# OBIETTIVO:
# Costruire un albero che separi correttamente le classi
# e riesca a generalizzare anche sui dati nuovi.
