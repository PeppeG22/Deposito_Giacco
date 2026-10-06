#CREAZIONE DI LISTE --->

numeri = [1, 2, 3, 4, 5]
nome = ["Alice", "Bob", "Charlie"]
misto = [1, "due", True, 4.5]


#STAMPIAMO UN ELEMENTE --->

print(numeri[0])  # Stampa il primo elemento della lista numeri


#SOSTITUZIONE DI UN ELEMENTO --->

numeri[2] = 10  # Sostituisce il terzo elemento della lista numeri con 10

print(numeri[2])  # Stampa il terzo elemento della lista numeri


#METODI DELLE LISTE --->

print(len(numeri))  # Stampa la lunghezza della lista    

numeri.append(6)  # Aggiunge l'elemento 6 alla fine della lista numeri  

numeri.remove(4)  # Rimuove l'elemento 4 dalla lista numeri 

numeri.sort()  # Ordina la lista numeri in ordine crescente

numeri.insert(2, 7)  # Inserisce l'elemento 7 alla posizione 2 della lista numeri

