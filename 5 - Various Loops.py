

#ciclo for
for x in range(5):
    print (x)

#ciclo for doppio
list = [[1,'a'],[2,'b'],[3,'c']]
for x, y in list:
    print (x)
    print (y)


#WHILE BREAK CONTINUE
# Prints out 0,1,2,3,4
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)



#LOOPS

#break: to exit a for / while loop
#continue: skip the current block and return to the for / while statement

    # Prints out 0,1,2,3,4
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

        # skips number 5
for x in range(10):
    # Check if x is even
    if x == 5:
        continue
    print(x)


count=0
while count<5:
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))


# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")

foo(1,2,3)


#doppia iterazione....MOLTO STRANA
a =[ ['a', 'b'], ['c', 'd'],[ 'e', 'f'] ]
for x,y in a:
    print(x, y)


#ciclo while :

print('start:')
numero_segreto = 9
while True:
    if numero_segreto == 5:
        print ('hai vinto!')
        break
    if numero_segreto > 5:
        print ("prova un po' di meno!")
    if numero_segreto < 5:
        print ("prova un po' di più!")
    break
