
#--LA STRINGA E' IMMUTABILE-------------

oggetto = 'ciao'
print(oggetto, '                  ', id(oggetto))

oggetto = 'figa'

print(oggetto, '                  ', id(oggetto))


cucu = 'ciao'
print(cucu, '                  ', id(cucu))



# 'is' operator
'''Unlike the double equals operator "==",
the "is" operator does not match the values of the variables,
but the instances themselves. '''
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False
