import pandas as pd  # importiamo la libreria Pandas
import matplotlib.pyplot as plt  # importiamo Matplotlib per i grafici


# 1. STUDIO CSV

def studio_csv():  # funzione per esplorare il CSV

    print("\n--- STUDIO CSV ---")

    print(df.head())  # visualizziamo le prime 5 righe

    print(df.tail())  # visualizziamo le ultime 5 righe

    df.info()  # visualizziamo le informazioni generali sulle colonne

    print(f"Il dataset contiene {df.shape[0]} prodotti e {df.shape[1]} colonne.")


# 2. PULIZIA CSV

def pulizia_csv(df):  # funzione per controllare e pulire il CSV

    print("\n--- PULIZIA CSV ---")

    print(df.isnull().sum())  # contiamo i valori mancanti per ogni colonna

    print(f"Totale valori mancanti: {df.isnull().sum()}")  # sommiamo tutti i valori mancanti

    print(f"Righe duplicate: {df.duplicated().sum()}")  # contiamo le righe duplicate

    df = df.drop_duplicates()  # eliminiamo eventuali righe duplicate

    df = df.dropna()  # eliminiamo le righe con valori mancanti

    print(df.describe())  # statistiche descrittive dopo la pulizia

    print(f"Dimensioni dopo la pulizia: {df.shape}")  # verifichiamo le dimensioni finali

    df.to_csv(nome_file, index=False)  # salviamo il DataFrame pulito nel CSV

    print("DataFrame pulito correttamente!")

    return df  # restituiamo il DataFrame aggiornato


# 3. AGGIUNTA PRODOTTO

def aggiungi_prodotto(df):  # funzione per aggiungere un prodotto al CSV

    print("\n--- AGGIUNTA PRODOTTO ---")

    id_articolo = input("Inserisci ID Articolo: ")  # inseriamo l'ID
    marca = input("Inserisci Marca: ")  # inseriamo la marca
    categoria = input("Inserisci Categoria: ")  # inseriamo la categoria
    colore = input("Inserisci Colore: ")  # inseriamo il colore
    taglia = input("Inserisci Taglia: ")  # inseriamo la taglia
    prezzo = float(input("Inserisci Prezzo: "))  # inseriamo il prezzo
    vendite = int(input("Inserisci Vendite: "))  # inseriamo le vendite

    with open(nome_file, "a") as file:  # apriamo il CSV in modalità aggiunta

        file.write(f"\n{id_articolo},{marca},{categoria},{colore},{taglia},{prezzo},{vendite}")  # scriviamo tutti i dati del prodotto

    df = pd.read_csv(nome_file)  # ricarichiamo il CSV aggiornato

    print("Prodotto aggiunto correttamente!")

    return df  # restituiamo il DataFrame aggiornato


# 4. ANALISI VENDITE

def analisi_vendite():  # funzione per analizzare le vendite

    print("\n--- ANALISI VENDITE ---")

    vendite = df.sort_values("Vendite", ascending=False)  # ordiniamo i prodotti per vendite decrescenti

    print("\nI 5 prodotti più venduti:")
    print(vendite[["ID_Articolo", "Marca", "Vendite"]].head(5))  # primi 5 prodotti

    print("\nI 5 prodotti meno venduti:")
    print(vendite[["ID_Articolo", "Marca", "Vendite"]].tail(5))  # ultimi 5 prodotti

    pivot_df = df.pivot_table(  # raggruppiamo le vendite per marca
        values="Vendite",  # colonna da analizzare
        index="Marca",  # raggruppiamo per marca
        aggfunc="sum"  # sommiamo le vendite
    )

    print("\nVendite totali per marca:")
    print(pivot_df.sort_values("Vendite", ascending=False))  # ordiniamo le marche per vendite


# 5. GRAFICO VENDITE

def grafico_vendite():  # funzione per visualizzare le vendite migliori

    print("\n--- GRAFICO VENDITE ---")

    top_5 = df.sort_values("Vendite", ascending=False).head(5)  # selezioniamo i 5 prodotti più venduti

    plt.bar(top_5["ID_Articolo"], top_5["Vendite"])  # creiamo il grafico a barre

    plt.title("I 5 prodotti più venduti")  # titolo del grafico
    plt.xlabel("ID Articolo")  # asse X
    plt.ylabel("Numero di vendite")  # asse Y
    plt.xticks(rotation=0)  # manteniamo orizzontali le etichette
    plt.tight_layout()  # sistemiamo gli spazi del grafico

    plt.show()  # visualizziamo il grafico


# CARICAMENTO INIZIALE CSV

nome_file = input("Inserisci il nome del file CSV: ")  # chiediamo il file da caricare

df = pd.read_csv(nome_file)  # carichiamo il file in un DataFrame

print("File caricato correttamente!")  # confermiamo il caricamento


# MENU PRINCIPALE

while True:  # ciclo per rendere il menu ripetibile

    print("\n--- MENU PRINCIPALE ---")
    print("1. Studio del CSV")  # esplorazione dei dati
    print("2. Pulizia del CSV")  # controllo e pulizia dei dati
    print("3. Aggiungi Prodotto")  # inserimento di nuovi prodotti
    print("4. Analisi delle Vendite")  # analisi delle vendite
    print("5. Grafico delle Vendite")  # rappresentazione grafica
    print("6. Cambia File CSV")  # caricamento di un altro file
    print("0. Esci")  # chiusura del programma

    scelta = input("Seleziona un'opzione: ")  # chiediamo la scelta all'utente

    if scelta == "1":  # studio CSV

        studio_csv()  # richiamiamo la funzione

    elif scelta == "2":  # pulizia CSV

        df = pulizia_csv(df)  # puliamo e aggiorniamo il DataFrame

    elif scelta == "3":  # aggiunta prodotto

        df = aggiungi_prodotto(df)  # aggiungiamo il prodotto e aggiorniamo il DataFrame

    elif scelta == "4":  # analisi vendite

        analisi_vendite()  # richiamiamo la funzione

    elif scelta == "5":  # grafico vendite

        grafico_vendite()  # richiamiamo la funzione

    elif scelta == "6":  # cambiamo il file CSV

        nome_file = input("Inserisci il nuovo file CSV: ")  # chiediamo il nuovo file

        df = pd.read_csv(nome_file)  # carichiamo il nuovo DataFrame

        print("Nuovo CSV caricato correttamente!")

    elif scelta == "0":  # uscita dal programma

        print("Programma terminato!")

        break  # interrompiamo il ciclo while

    else:  # scelta non valida

        print("Scelta non valida, riprova!")