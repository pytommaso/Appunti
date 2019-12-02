
def simple_gen():
    for x in range(3):
        yield x


for n in simple_gen():
    print(n)


g = simple_gen()

print(g)
print(next(g))
print('-  -   -')
print(next(g))
print('-  -   -')
print(next(g))
print('-  -   -')
print(next(g))    # NO MORE !!!



# ITER trasforma ad es. una str
# in un iterator su cui posso fare next()
iter(collection, sentinel=None)
