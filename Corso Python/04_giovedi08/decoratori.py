# GENERATORI:

# Sono una speciale tipologia di funzioni, permettono di creare un ciclo dentro una funzione
# - yield - è un return dinamico

# DECORATORI

# Sono una funzione che va a modificare il comportamento di altre funzioni
# senza cambiare direttamente il codice, solitamente usate per aggiungere
# si riconoscono tramite: @ - 'wrapper'

# esempio


def decoratore(funzione):  # riceve una funzione come parametro

    def wrapper():  # crea una funzione interna
        print("Prima dell'esecuzione della funzione")

        funzione()  # esegue la funzione originale

        print("Dopo l'esecuzione della funzione")

        return wrapper  # restituisce la funzione interna


@decoratore  # applica il decoratore alla funzione saluta
def saluta():
    print("Ciao!")


saluta()  # richiama la funzione decorata
