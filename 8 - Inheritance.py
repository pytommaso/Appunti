
class Animal():

    def __init__(self):
        print('ANIMAL CREATED')

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')


class Dog(Animal):

    # INHERIT                       # not necessary!!
    # def __init__(self):
    #     Animal.__init__(self)
    #     print('DOG CREATED')      # just if u want to add something

    # OVER-WRITE
    def who_am_i(self):
        print('I am a dog')

    # CLASS SPECIFIC METHOD
    def abbaiare(self):
        print('Woof!')


an_animal = Animal()
an_animal.eat                   # NOOOO!
an_animal.eat()
an_animal.who_am_i()

print('* '*10)

caterina = Dog()
caterina.eat()
caterina.who_am_i()
caterina.abbaiare()
