'''
Cos'è un operazione vettoriale? A cosa serve?

Un'operazione vettoriale è un'operazione che permette di eseguire calcoli su tutti gli elementi di un array, senza dover utilizzare nessun tipo di ciclo.
A differenza delle operazioni universali, quelle vettoriali vanno a lavorare nello specifico sugli elementi  degli array effettuando un operazione. 
Esempio: avendo un vettore arr = [1, 2, 3], un operazione potrebbe essere quella di sommare a tutti gli elementi un numero x, modificandone quindi il valore.
    
    
    
    
Cos'è un MatplotLib? E seaborn? a cosa servono e cosa le distingue?


Matplotlib e Seaborn sono due librerie Python utilizzate per la
visualizzazione dei dati attraverso grafici.
Matplotlib è considerato il padre di Seaborn, ci permette di creare grafici di ogni tipo: a linee, a barre, a disperisione, ecc...
Grazie a questa libreria, in Python, siamo in grado di modificare a piacimento ogni particolare del nostro grafico, come colori, titoli e legende. 
Seaborn è principalmente utilizzata per creare grafici statistici piu complessi ed elaborati.
Entrambi, insieme a Numpy e Pandas, cooperano nell'ambito dell'analisi dati, quindi vanno a rappresentare i dati dopo che sono stati raccolti, puliti e ordinati.
    

Cos'è un NumPY? a cosa serve?

Numpy è una libreria Python utilizzata per eseguire calcoli scientifici, matematici e statistici.
Introduce due strutture nuove in Python, l'array e le Series.
L'array è una struttura dati che contiene una lista di elementi, può essere:
monodimensionale (una dimensione, simile a una lista),
bidimensionale (una matrice, struttura organizzata in riga, colonna)
multidimensionale (quindi a piu di 2 dimensioni)
In NumPy, gli array vengono rappresentati attraverso la struttura dati ndarray.
Introduce una delle operazioni piu importanti dell'analisi dati,
ovvero le operazioni vettoriali. #verranno spiegate nelle domande successive


Cos'è il Pandas? A cosa serve? Spiegalo

Pandas è una libreria Python utilizzata per la pulizia, manipolazione e analisi dei dati.
Permette di organizzare i dati principalmente attraverso
due strutture:

- Series: struttura dati monodimensionale che contiene valori associati a un indice.

- DataFrame: struttura dati bidimensionale, organizzata in righe e colonne, simile a una tabella Excel o SQL.

Pandas serve principalmente a:
- Importare ed esportare dati, ad esempio da file CSV ed Excel.
- Pulire i dati, eliminando o correggendo valori mancanti o errati.
- Modificare, filtrare e ordinare i dati.
- Raggruppare e aggregare i dati.
- Eseguire analisi statistiche, come media, somma e conteggio sfruttando anche NumPy.
- Unire e concatenare più DataFrame.

Pandas si basa anche su NumPy e permette di lavorare con grandi quantità di dati in modo organizzato ed efficiente.


Quali sono le tre categorie che abbiamo visto delle librerie per l'analisi? a cosa servono? 

LIBRERIE PER IL CALCOLO NUMERICO (NumPy):
   Permettono di eseguire operazioni matematiche, statistiche
   e matriciali in modo rapido ed efficiente, utilizzando
   principalmente gli array.

LIBRERIE PER LA MANIPOLAZIONE DEI DATI (Pandas):
   Permettono di gestire, organizzare, pulire, modificare
   e analizzare grandi quantità di dati attraverso
   strutture come Series e DataFrame.

LIBRERIE PER LA VISUALIZZAZIONE DEI DATI (Matplotlib e Seaborn):
   Permettono di rappresentare graficamente i dati
   attraverso grafici a linee, a barre, istogrammi
   e grafici statistici, facilitandone l'interpretazione.
   


Come si gestisce in Python l'I/O?
Quali altre librerie permettono di gestire questa funzionalità?

Input/Output rappresenta l'insieme delle operazioni che permettono a un programma di ricevere dati (input) e restituire(output).
Per la gestione dei file possiamo utilizzare diverse modalità:
- "r": lettura di un file.
- "w": scrittura, creando o sovrascrivendo un file.
- "a": aggiunta di contenuti alla fine di un file.
- "x": creazione di un nuovo file, se non esiste già.
Attraverso read() e write() possiamo leggere e scrivere dati.
Molto importante l'istruzione close() per chiudere un file dopo l'operazione effettuata, in quando potrebbe rimanere aperto
all'infinito, in aiut abbiamo l'istruzione with, attraverso la quale possiamo gestire l'apertura e la chiusura automatica del file.
'''
