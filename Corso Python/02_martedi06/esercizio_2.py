
#esercizio: creare 2 liste: 1 di numeri , 1 di stringhe. Andiamo a chiedere
#           quale lista si vuole usare e dopo gli facciamo aggiungere o rimuovere
#           alla fine si richiede di stampare la lista.

num = [1,2,3,4,5,6,7,8,9]
words = ['banana','mela','pera','melone','fragola']

scelta = int(input('su quale lista vuoi operare? 1/2 \n')) #L'OPERATORE SCEGLIE SU QUALE LISTA OPERARE

operazione = int(input('come vuoi modificare? 1 - aggiungi / 2 - elimina ')) #L'OPERATORE SCEGLIE CHE OPERAZIONE EFFETTUARE


if scelta == 1: #PRIMO CASO

    print('Hai scelto di operare sui numeri\n')

    if operazione == 1: #PRIMA OPERAZIONE

        elemento = int(input("Che elemento vuoi aggiungere? ")) #VARIABILE IN CUI SALVIAMO L'ELEMENTO DA AGGIUNGERE

        num.append(elemento) #OPERAZIONE DI AGGIUNTA

        print('Lista aggiornata: \n', num, '\n') #STAMPA FINALE AGGIORNATA


    elif operazione == 2: #SECONDA OPERAZIONE

        elemento = int(input("Che elemento vuoi eliminare? ")) #VARIABILE IN CUI SALVIAMO L'ELEMENTO DA ELIMINARE

        if elemento in num: #CONTROLLO SE L'ELEMENTO È PRESENTE NELLA LISTA

            num.remove(elemento) #OPERAZIONE DI ELIMINAZIONE

            print('Lista aggiornata: \n', num, '\n') #STAMPA FINALE AGGIORNATA

        else:

            print('Elemento non presente nella lista!\n') #CASO IN CUI L'ELEMENTO NON ESISTE NELLA LISTA

    else:

        print('Operazione non riconosciuta!\n') #NEL CASO IN CUI NON SI SCELGA UN OPERAZIONE CONSENTITA


elif scelta == 2: #SECONDO CASO

    print('Hai scelto di operare sulle parole\n')

    if operazione == 1: #PRIMA OPERAZIONE

        elemento = input("Che elemento vuoi aggiungere? ") #VARIABILE IN CUI SALVIAMO L'ELEMENTO DA AGGIUNGERE

        words.append(elemento) #OPERAZIONE DI AGGIUNTA

        print('Lista aggiornata: \n', words, '\n') #STAMPA FINALE AGGIORNATA


    elif operazione == 2: #SECONDA OPERAZIONE

        elemento = input("Che elemento vuoi eliminare? ") #VARIABILE IN CUI SALVIAMO L'ELEMENTO DA ELIMINARE

        if elemento in words: #CONTROLLO SE L'ELEMENTO È PRESENTE NELLA LISTA

            words.remove(elemento) #OPERAZIONE DI ELIMINAZIONE

            print('Lista aggiornata: \n', words, '\n') #STAMPA FINALE AGGIORNATA

        else:

            print('Elemento non presente nella lista!\n') #CASO IN CUI L'ELEMENTO NON ESISTE NELLA LISTA

    else:

        print('Operazione non riconosciuta!\n') #NEL CASO IN CUI NON SI SCELGA UN OPERAZIONE CONSENTITA


else:

    print('Scelta non valida!\n') #CASO IN CUI NON SI SCELTA UN CASO TRATTATO IN PRECEDENZA


#------------------------------------------------------------------------------------------------------------

