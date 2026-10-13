#ESERCIZIO 1 - EREDITARIETÀ (ZOO)

#CLASSE PADRE

class Animale:

    def __init__(self, nome, eta):
        self.nome = nome  #inizializziamo il nome dell'animale
        self.eta = eta  #inizializziamo l'età dell'animale

    def fai_suono(self):  #metodo per emettere un suono generico
        print(f'{self.nome} emette un suono!')


#CLASSE FIGLIA - LEONE

class Leone(Animale):  #ereditiamo dalla classe Animale

    def __init__(self, nome, eta, criniera):
        super().__init__(nome, eta)  #richiamiamo il costruttore della classe padre
        self.criniera = criniera  #aggiungiamo l'attributo criniera

    def fai_suono(self):  #sovrascriviamo il metodo della classe padre
        print(f'{self.nome} ruggisce: ROAR!')

    def caccia(self):  #metodo specifico del leone
        print(f'{self.nome} sta cacciando una preda!')


#CLASSE FIGLIA - GIRAFFA

class Giraffa(Animale):  #ereditiamo dalla classe Animale

    def __init__(self, nome, eta, altezza):
        super().__init__(nome, eta)  #richiamiamo il costruttore della classe padre
        self.altezza = altezza  #aggiungiamo l'attributo altezza

    def fai_suono(self):  #sovrascriviamo il metodo della classe padre
        print(f'{self.nome} emette un verso sommesso!')

    def mangia_foglie(self):  #metodo specifico della giraffa
        print(f'{self.nome} sta mangiando le foglie dagli alberi!')


#CLASSE FIGLIA - PINGUINO

class Pinguino(Animale):  #ereditiamo dalla classe Animale

    def __init__(self, nome, eta, velocita_nuoto):
        super().__init__(nome, eta)  #richiamiamo il costruttore della classe padre
        self.velocita_nuoto = velocita_nuoto  #aggiungiamo la velocità di nuoto

    def fai_suono(self):  #sovrascriviamo il metodo della classe padre
        print(f'{self.nome} emette un richiamo stridulo!')

    def nuota(self):  #metodo specifico del pinguino
        print(f'{self.nome} sta nuotando a {self.velocita_nuoto} km/h!')


#CREAZIONE DEGLI OGGETTI

leone1 = Leone('Simba', 5, True)  #creiamo un leone
giraffa1 = Giraffa('Melman', 8, 5.2)  #creiamo una giraffa
pinguino1 = Pinguino('Rico', 3, 12)  #creiamo un pinguino


#STAMPA DELLE INFORMAZIONI

print('\n--- LEONE ---')
print(f'Nome: {leone1.nome}')
print(f'Età: {leone1.eta}')
print(f'Criniera: {leone1.criniera}')
leone1.fai_suono()  #richiamiamo il metodo sovrascritto
leone1.caccia()  #richiamiamo il metodo specifico


print('\n--- GIRAFFA ---')
print(f'Nome: {giraffa1.nome}')
print(f'Età: {giraffa1.eta}')
print(f'Altezza: {giraffa1.altezza} metri')
giraffa1.fai_suono()  #richiamiamo il metodo sovrascritto
giraffa1.mangia_foglie()  #richiamiamo il metodo specifico


print('\n--- PINGUINO ---')
print(f'Nome: {pinguino1.nome}')
print(f'Età: {pinguino1.eta}')
print(f'Velocità di nuoto: {pinguino1.velocita_nuoto} km/h')
pinguino1.fai_suono()  #richiamiamo il metodo sovrascritto
pinguino1.nuota()  #richiamiamo il metodo specifico


print('\n--- SUONI DEGLI ANIMALI ---')

animali = [leone1, giraffa1, pinguino1]  #creiamo una lista con tutti gli animali

for animale in animali:  #scorriamo gli animali presenti nella lista
    animale.fai_suono()  #ogni animale esegue il proprio metodo
    
    
#ESERCIZIO 2 - EREDITARIETÀ (FABBRICA)


#CLASSE PADRE - PRODOTTO

class Prodotto:

    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        self.quantita = 0  #inizializziamo la quantità del prodotto

    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione


#CLASSE FIGLIA - ELETTRONICA

class Elettronica(Prodotto):

    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.garanzia = garanzia


#CLASSE FIGLIA - ABBIGLIAMENTO

class Abbigliamento(Prodotto):

    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.materiale = materiale


#CLASSE FABBRICA

class Fabbrica:

    def __init__(self):
        self.inventario = []  #creiamo una lista vuota per i prodotti


    def aggiungi_prodotto(self, prodotto, quantita):

        if quantita > 0:  #controlliamo che la quantità sia positiva

            if prodotto not in self.inventario:  #controlliamo se il prodotto non è presente
                self.inventario.append(prodotto)  #aggiungiamo il prodotto alla lista

            prodotto.quantita += quantita  #aumentiamo la quantità disponibile


    def vendi_prodotto(self, prodotto, quantita):

        if prodotto in self.inventario and 0 < quantita <= prodotto.quantita:

            prodotto.quantita -= quantita  #diminuiamo la quantità disponibile

            profitto = prodotto.calcola_profitto() * quantita  #calcoliamo il profitto totale

            print(f'Profitto realizzato: {profitto} euro')  #stampiamo il profitto


    def resi_prodotto(self, prodotto, quantita):

        if quantita > 0:  #controlliamo che la quantità sia positiva

            if prodotto not in self.inventario:
                self.inventario.append(prodotto)  #aggiungiamo il prodotto se non è presente

            prodotto.quantita += quantita  #aumentiamo la quantità restituita


#CREAZIONE DEGLI OGGETTI

prodotto1 = Elettronica('Computer', 500, 800, 24)

prodotto2 = Abbigliamento('Maglietta', 10, 25, 'Cotone')


#CREAZIONE DELLA FABBRICA

fabbrica1 = Fabbrica()


#AGGIUNTA DEI PRODOTTI

fabbrica1.aggiungi_prodotto(prodotto1, 10)

fabbrica1.aggiungi_prodotto(prodotto2, 20)


#VENDITA DEI PRODOTTI

fabbrica1.vendi_prodotto(prodotto1, 2)

fabbrica1.vendi_prodotto(prodotto2, 5)


#RESO DEI PRODOTTI

fabbrica1.resi_prodotto(prodotto1, 1)

fabbrica1.resi_prodotto(prodotto2, 2)