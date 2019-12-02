
#funioni GLOBAL - Local

#1
x = 15

def funzione_esempio1():
    x = x + 2    #la x prima dell'uguale non esiste
    return (x)


#2
x = 15

def funzione_esempio():
    y = x           # perchè invece esiste la x dopo l'uguale ?
    y = y + 2       # perchè esiste solo come valore 15, trasferito alla y
    return (y)      #..la y non diventa = x, ma = a 15 !!  ATTENZIONE

print(funzione_esempio())
print(funzione_esempio1())
# alle variabili locali si accede solo da ambito locale!!!
# ciò che arriva al Globale è solo il return

# USA TANTE -IL PIù POSSIBILE- VARIABILI LOCALI:
#   - CHE RENDONO PIù LEGGERO IL PROGRAMMA!!!!!!!
#   - EVITANO I BUG
#   - RENDONO PIù ROBUSTO IL PROGRAMMA
