import pandas as pd  # importiamo pandas per creare i DataFrame

# 1. DATAFRAME ISCRITTI

dati_iscritti = {  # creiamo 11 righe con un duplicato e un valore mancante
    "Nome": [
        "Anna", "Luca", "Marco", "Giulia", "Sara",
        "Paolo", "Elena", "Davide", "Laura", "Mario", "Anna"
    ],  # nomi degli iscritti
    "Eta": [
        25, 30, None, 22, 35,
        40, 28, 33, 26, 45, 25
    ],  # inseriamo un'età mancante
    "Citta": [
        "Roma", "Milano", "Napoli", "Roma", "Milano",
        "Napoli", "Roma", "Milano", "Napoli", "Roma", "Roma"
    ],  # città degli iscritti
    "Tipo_Abbonamento": [
        "Base", "Premium", "Family", "Base", "Premium",
        "Family", "Premium", "Base", "Family", "Base", "Base"
    ]  # la prima e l'ultima riga sono completamente duplicate
}

df_iscritti = pd.DataFrame(dati_iscritti)  # creiamo il DataFrame degli iscritti

# 2. DATAFRAME PRESENZE

dati_presenze = {  # creiamo 15 righe con 3 date e 3 città
    "Data": [
        "2026-10-01", "2026-10-01", "2026-10-01",
        "2026-10-01", "2026-10-01",
        "2026-10-02", "2026-10-02", "2026-10-02",
        "2026-10-02", "2026-10-02",
        "2026-10-03", "2026-10-03", "2026-10-03",
        "2026-10-03", "2026-10-03"
    ],  # date delle lezioni
    "Corso": [
        "Yoga", "Crossfit", "Nuoto", "Pilates", "Yoga",
        "Yoga", "Crossfit", "Nuoto", "Pilates", "Yoga",
        "Yoga", "Crossfit", "Nuoto", "Pilates", "Yoga"
    ],  # corsi del centro sportivo
    "Citta": [
        "Roma", "Milano", "Napoli", "Roma", "Milano",
        "Roma", "Milano", "Napoli", "Roma", "Milano",
        "Roma", "Milano", "Napoli", "Roma", "Milano"
    ],  # città in cui si svolgono le lezioni
    "Partecipanti": [
        15, 20, 12, 18, 10,
        17, 22, 14, 16, 13,
        19, 24, 15, 20, 12
    ]  # numero di partecipanti a ogni lezione
}

df_presenze = pd.DataFrame(dati_presenze)  # creiamo il DataFrame delle presenze

# 3. DATAFRAME COSTI ABBONAMENTO

dati_costi = {  # creiamo il dizionario dei costi degli abbonamenti
    "Tipo_Abbonamento": ["Base", "Premium", "Family"],  # tipi di abbonamento
    "Costo_Mensile": [30, 50, 70]  # costi mensili in euro
}

df_costi_abbonamento = pd.DataFrame(dati_costi)  # creiamo il DataFrame dei costi