'''TRACCIA: chiedere all'utente di inserire un numero
            dobbiamo stampare un conto alla rovescia
            da quel numero fino a 0, alla fine chiedere 
            se vuole ripetere oppure no.'''
            
while True:   #ripete finche l'utente lo richiede        
           
    count = int(input('Inserisci numero per far partire il conto alla rovescia! '))

    for i in range(count, -1, -1): #parte dal numero inserito e va fino a -1 (escluso), quindi 0
        print(i) #stampa i ad ogni iterazione 
        
    scelta = input("Vuoi ripetere? si/no ") #ƒacciamo scegliere all'utente se vuole continuare

    if scelta.lower() == "no":
        break

#ESERCIZIO 2 + EXTRA


'''Traccia: chiedi all'utente di inserire un numero se è pari o primo
            lo salva e stampa, si ferma tutto quando ha 5 numeri'''
            
num_pari = []  #inizializziamo le due liste
num_primi = []
num_dispari = []

while True:  #facciamo un ciclo che controlla la lunghezza delle liste

    num = int(input('Inserisci il numero che vuoi inserire nelle liste '))

    if num % 2 == 0:  #se il resto della divisione per 2 è zero
        num_pari.append(num)  #viene inserito all'interno della list

    elif num % 2 != 0:  #se il resto non è 0 allora è dispari
        num_dispari.append(num)


    divisori = 0  #formula numeri primi

    for i in range(1, num + 1):
        if num % i == 0:
            divisori += 1

    if divisori == 2:
        num_primi.append(num)


    if len(num_pari) == 5:
        print(num_pari)

    if len(num_dispari) == 5:
        print(num_dispari)

    if len(num_primi) == 5:
        print(num_primi)

    if len(num_pari) == 5 or len(num_dispari) == 5 or len(num_primi) == 5: #se almeno una lista arriva a 5 si ferma il ciclo
        break

    else:
        print('Aggiungi fino ad arrivare a 5 numeri \n ')