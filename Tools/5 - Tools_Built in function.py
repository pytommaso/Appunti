
# builtinfunction

__import__()     help()       min()           tuple()
abs()            id()         next()          type()
ascii()          input()      open()          zip()
bool()           int()        print()
dict()           iter()       range()
dir()            len()        reversed()
enumerate()      list()       set()
float()          map()        str()
format()         max()        sum()

sort() VS sorted() # ???
# getattr()


#Ciascuna variabile in Python è un oggetto,
#e quindi ogni oggetto supporta le seguenti funzioni:
help(object) # - Mostra informazioni circa l'uso dell'oggetto
dir(object)  # - Mostra la struttura interna dell'oggetto - Tutti i metodi e tutti i membri

            # list comprehention
movies_with_G = [title for title in movies if title.startwith('g') ]

movies_before_2000 = [title for (title, year) in  movies if year in title < 2000 ]


            # with open
with open("file_name", "file2_name") as f:
