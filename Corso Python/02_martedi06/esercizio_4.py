# ES 4

list = []

#inseriamo i nostri dati nella lista

list.append(input('Inserisci il tuo nome '))
list.append(int(input('Inserisci la tua età ')))
list.append(input('Inserisci il sesso     m/f '))

premium = input('Sei un utente premium?     si/no ')

if premium.lower() == 'si': #inseriamo un bool nella lista come da traccia, in base alla richiesta dell'utente 

    list.append(True)

else:

    list.append(False)

#Dati completi


#Creiamo un form di modifica tramite match

print(list, '\n')

scelta = input('Digita il nome del campo da modificare  \n  nome / eta / sesso / premium  \n Digita elimina per eliminare un campo \n digita reset per riscrivere tutto \n') #l'utente sceglie il dato da modificare 

match scelta.lower():

    case 'nome':  #abbiamo scelto il nome 

        list[0] = input('Inserisci un nuovo nome ') #sostituzione valore
        
        print(list, '\n') #stampiamo la lista aggiornata

    case 'eta':

        list[1] = int(input('Inserisci la nuova età ')) #sostituzione valore
        
        print(list, '\n') #stampiamo la lista aggiornata

    case 'sesso':

        list[2] = input('Inserisci il tuo sesso    m/f ') #sostituzione valore
        
        print(list, '\n') #stampiamo la lista aggiornata

    case 'premium':

        if list[3] == True:  #essendo solo due le casistiche la modifica è immediata

            list[3] = False

        else:

            list[3] = True
            
        print(list, '\n') #stampiamo la lista aggiornata
        
    case 'elimina':

        scelta_elimina = input('Quale campo vuoi eliminare? nome / eta / sesso / premium' ) #scegliamo il campo da rimuovere

        match scelta_elimina.lower():

            case 'nome':

                list.pop(0)
                
                print(list, '\n') #stampiamo la lista aggiornata

            case 'eta':

                list.pop(1)
                
                print(list, '\n') #stampiamo la lista aggiornata

            case 'sesso':

                list.pop(2)
                
                print(list, '\n') #stampiamo la lista aggiornata

            case 'premium':

                list.pop(3)
                
                print(list, '\n') #stampiamo la lista aggiornata

            case _:

                print('Campo non valido!\n')
                
                print(list, '\n') #stampiamo la lista aggiornata

    
    case 'reset':
        
        list.clear() #eliminiamo tutti i dati dalla lista 
        
        list.append(input('Inserisci il tuo nome ')) #raccogliamo con gli stessi metodi i dati che vogliamo 
        list.append(int(input('Inserisci la tua età ')))
        list.append(input('Inserisci il sesso     m/f '))

        premium = input('Sei un utente premium?     si/no ')

        if premium.lower() == 'si':

            list.append(True)

        else:

            list.append(False)
        
        print(list, '\n') #stampiamo la lista aggiornata
    
    case _: #nel caso in cui non si scelga di moficare nulla 

        print('Non vuoi modificare nessun dato!\n')
        
        print(list, '\n') #stampiamo la lista aggiornata
        

#EXTRA: andare a gestire la possibilità di non solo modificare ma anache creare una seconda lista da zero o rimuovere dalla prima

