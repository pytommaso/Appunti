
def gen_fibon(n):

    a = 1
    b = 1
    for i in range(n):
        yield b
        #a = b
        #b = a + b
        a,b = b,a+b

# # ATTENZIONE:
# a = b
# b = a + b
# # E' DIVERSO DA: perchè nel primo l'espressione iniziale
# #variando varia la seconda
# a,b = b,a+b


for n in gen_fibon(10):
    print(n)
