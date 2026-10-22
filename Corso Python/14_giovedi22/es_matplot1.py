import pandas as pd  # importiamo pandas per creare il DataFrame
import numpy as np  # importiamo numpy per generare le temperature casuali
import matplotlib.pyplot as plt  # importiamo pyplot per creare il grafico

dati = {  # creiamo un dizionario con una sola colonna
    "temperature": np.random.randint(10, 31, size=30)  # generiamo 30 temperature tra 10 e 30 gradi per un mese di 30 giorni
}

df = pd.DataFrame(dati)  # creiamo il DataFrame dal dizionario

massima = df["temperature"].max()  # calcoliamo la temperatura massima
minima = df["temperature"].min()  # calcoliamo la temperatura minima
media = df["temperature"].mean()  # calcoliamo la temperatura media
mediana = df["temperature"].median()  # calcoliamo la mediana delle temperature

print("Temperatura massima:", massima)  # stampiamo la temperatura massima
print("Temperatura minima:", minima)  # stampiamo la temperatura minima
print("Temperatura media:", media)  # stampiamo la temperatura media
print("Mediana delle temperature:", mediana)  # stampiamo la mediana


giorni = np.arange(1, 31)  # creiamo i giorni del mese da 1 a 30

plt.plot(giorni, df["temperature"])  # disegniamo una linea con i giorni sull'asse x e le temperature sull'asse y

plt.title("Temperature giornaliere")  # aggiungiamo il titolo
plt.xlabel("Giorno")  # aggiungiamo il nome dell'asse x
plt.ylabel("Temperatura (°C)")  # aggiungiamo il nome dell'asse y

plt.show()  # mostriamo il grafico