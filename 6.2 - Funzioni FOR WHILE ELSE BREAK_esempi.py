

# switch tra 2 while in parallelo

def summer_69(arr):
    total = 0
    adding = True
    for num in arr:
        while adding:
            if num != 6:
                total += num
                break
            else:
                adding = False
        while not adding:
            if num != 9:
                break
            else:
                adding = True
                break
    return total

print(summer_69([5,6,1,9,5,6,1,9,5]))


# = = = = = = = = OUT OF THE BOX !!!!!!!!!!!!!! = = = = = = = =

# CREA UNA MATRICE E LA CONSUMA NELLA SCANSIONE

def spy_game(nums):

    code = [0, 0, 7, 'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)

    return len(code) == 1

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))


# = = = = = = = = OUT OF THE BOX !!!!!!!!!!!!!! = = = = = = = =

# COMPARA CIASCUN VALORE CON UNA LISTA DINAMIZZATA DALLO SCRIPT STESSO


# Write a Python function that takes a list and returns
# a new list with unique elements of the first list

def unique_list(lst):
    x = []
    for a in lst:
        if a not in x:
            x.append(a)
    print (x)


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

# particolare struttura for-(break)-else
    # for:
        # if:
        # break
    # else:

def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3,x,2):  # test all odd factors up to x-1
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    print(len(primes))

count_primes(10)


# ragiona sulla differenza di
# dove è posizionato il break
for y in range(5):
    print (y)
    if y == 3:
        pass
        break

for y in range(5):
    print (y)
    if y == 3:
        pass
    break


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
