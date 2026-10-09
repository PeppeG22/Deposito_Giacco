#modulo su cui creare le funzioni da richiamare in altri moduli


def somma(n1, n2):
    risultato = n1 + n2 #sommiamo i due numeri
    return risultato #restituiamo il risultato


def moltiplicazione(n1, n2):
    risultato = n1 * n2 #moltiplichiamo i due numeri
    return risultato #restituiamo il risultato


def sottrazione(n1, n2):
    risultato = n1 - n2 #sottraiamo i due numeri
    return risultato #restituiamo il risultato


def divisione(n1, n2):
    if n2 != 0: #controlliamo che il divisore sia diverso da 0
        risultato = n1 / n2 #dividiamo i due numeri
        return risultato #restituiamo il risultato

    else:
        print('Non puoi fare la divisione per 0! ')
        return None #restituiamo None se la divisione non è possibile