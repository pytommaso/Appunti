

N^2 o N^3
(in c++ )si riferisce al nested di più for looops???





#ask ORL
def up_low(s):
    dic = {'upper': 0, 'low': 0}
    for x in s:
        if x.isupper():
            dic['upper'] += 1
        else:
            dic['low'] += 1
    print('No. of Upper case characters :', dic['upper'])
    print('No. of Lower case Characters :', dic['low'])
def up_low(s):
    d={"upper":0, "lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case Characters : ", d["lower"])
up_low('Hello Mr. Rogers, how are you this fine Tuesday?')
# OOOOOOOOO
# OOOOOOOOO
# OOOOOOOOO
#ask ORL
import string
help(string)
def ispangram(str1, alphabet=string.ascii_lowercase):
    a = True
    for letter in alphabet:
        if letter not in str1.lower():
            a = False
    print (a)
ispangram("qick brown fox jumps over the lazy dog")
ma quando mai???
def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())
# OOOOOOOOO
# OOOOOOOOO
# OOOOOOOOO
