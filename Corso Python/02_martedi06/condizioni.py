#CONTROLLO DEL FLUSSO 

x = 10 #VARIABILE INTERA

if x > 5: #condizione vera!
    print("x è maggiore di 5") #eseguo l'if solo se la condizione è vera
        #CONDIZIONE 1

elif x == 5: #condizione falsa!
    print("x è uguale a 5") #eseguo l'elif solo se la condizione è vera
        #CONDIZIONE 2

else: #tutte le condizioni false!
    print("x è minore di 5") #eseguo l'else se non esiste una condizione vera
        #CONDIZIONE FINALE, INCLUDE TUTTO CIO' CHE NON ABBIAMO RACCHIUSO IN UN IF


#FACCIAMO UN IF DENTRO UN IF

if x > 5:
    print("x è maggiore di 5")
    if x > 8: #esegue solo se è vera la sua condizione e se è vera la condizione dell'if esterno
        print("x è anche maggiore di 8")
    else:
        print("x non è maggiore di 8")
else: #esegue se le condizioni dell'if esterno sono false
    print("x è minore o uguale a 5")
    
#-------------------------------------------------------------- 
#--------------------------------------------------------------




