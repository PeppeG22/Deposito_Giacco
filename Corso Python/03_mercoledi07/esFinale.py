'''ESERCIZIO COMPLETO
   Cicli, range e condizioni'''

#Chiedere all'utente di inserire un numero intero positivo n


n = int(input('Inserisci un numero intero positivo: '))


#1. Utilizzare un ciclo while per garantire che l'utente inserisca
#un numero positivo


while n <= 0:

    print('Il numero deve essere positivo')

    n = int(input('Inserisci un numero intero positivo: '))


#--------------------------------------------------------------------


#2. Utilizzare un ciclo for con range per calcolare e stampare
#la somma dei numeri pari da 1 a n


sommaPari = 0


for i in range(1, n + 1):

    if i % 2 == 0:  #controlliamo se il numero è pari

        sommaPari += i  #aggiungiamo il numero alla somma


print('La somma dei numeri pari da 1 a', n, 'è:', sommaPari)


#--------------------------------------------------------------------


#3. Utilizzare un ciclo for per stampare tutti i numeri dispari
#da 1 a n


print('I numeri dispari da 1 a', n, 'sono:')


for i in range(1, n + 1):

    if i % 2 != 0:  #se il resto della divisione per 2 è diverso da 0

        print(i)


#--------------------------------------------------------------------


#4. Determinare se n è un numero primo
#Un numero primo è divisibile solo per 1 e per se stesso


primo = True  #inizialmente consideriamo il numero primo


if n == 1:

    primo = False  #1 non è un numero primo

else:

    for i in range(2, n):

        if n % i == 0:  #se n è divisibile per un altro numero

            primo = False

            break  #abbiamo trovato un divisore quindi possiamo fermarci


if primo == True:

    print(n, 'è un numero primo')

else:

    print(n, 'non è un numero primo')