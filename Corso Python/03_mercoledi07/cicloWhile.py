#Lezione: Ciclo While --->

#ESEMPIO 1 

conteggio = 0 #Variabile iniziale

while conteggio < 5: #''FINCHE'' è minore di 5
    print(conteggio)
    conteggio += 1 #Aumenta ad ogni ciclo il conteggio
    
    
#ESEMPIO 2 --->    ciclo booleano 


controllore = True

while controllore: # Finchè il controllore è vero
    
    print('ciao')
    
    scelta = input('scrivi - end - per uscire')
    
    if scelta.lower()== 'end': 
        
        controllore = False #Lambia la variabile, rompe il ciclo
        
        
#CICLO FOR --->

#ESEMPIO 1 
numeri = [1,2,3,4,5] #Lista di partenza
 
for numero in numeri: #Itera tutti gli elementi della lista
    print(numero)   #Li stampa uno per uno    
    
limite = 5

#ESEMPIO 2 
for numero in limite:
    print(numero) 
    
    
#RANGE ---> 

#ESEMPIO 1 

for i in range(2, 8): #START - STOP - STEP 
    
    print(i)
    
