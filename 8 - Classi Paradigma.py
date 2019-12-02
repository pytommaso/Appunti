
class Dog():

    numero_zampe = 'quattro'  # attribute for any instance

    def __init__(self, argument, name, macchie):

        self.attribute = argument
        self.attribute2 = argument**2
        self.name = name
        # Expected boolean True/False
        self.macchie = macchie
        self.fullname = name + ' Rognoni'

    def abbaiare(self):      # Methods: Operation/Actions
        print('Woof! My name is {}, I have {} zampe, or {} class-zampe'
              .format(self.name, self.numero_zampe, Dog.numero_zampe))

    def abbaiare2(self, number):
        print('{} gives: the number can be {} or {}'
              .format(self.name, self.attribute, self.attribute2))


# *****************
my_dog = Dog(argument=5, name='Caterina', macchie=False)

print(type(my_dog))

print(my_dog.attribute)
print(my_dog.attribute2)
print(my_dog.name)
print(my_dog.macchie)
print(my_dog.fullname)

print(my_dog.numero_zampe)
my_dog.numero_zampe = 'cinque' # variabile di classe diventa dell'istanza
print(my_dog.numero_zampe)

my_dog.abbaiare()
my_dog.abbaiare2(7)

print (Dog.__dict__)
print (my_dog.__dict__)
