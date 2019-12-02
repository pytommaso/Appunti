

# generators:
# doesnt return and exit, like functions
# they automatically suspend and resume in the last point
# of value generation



# with giant list in memory
def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result

create_cubes(10)   # ---> gives a list



for x in create_cubes(10):
    print (x)            #here we need the single value at once,
                            # not all the list stored
# soooo

# with yield and no list
def create_cubes(n):
    #result = []
    for x in range(n):
        #result.append(x**3)
        yield x**3
    #return result


for x in create_cubes(10):
    print (x)

print(create_cubes(10)) # no more a list,
                        # instead:
                        # <generator object create_cubes at 0x00C79430>

print(list(create_cubes(10)))
