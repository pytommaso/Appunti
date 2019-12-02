
#STRUTTURA

try:                                     # executed like normal code
    # try block
    print(4/0)

except ZeroDivisionError:                # (optional)
    print('target error block')
except Exception as e:                   # alternative to except:
    print('e = ', e, ' block')
except:                                  # alternative to except Exception as
    print('generic error block')         # (must be at the end of exceptions)

else:                                    # (optional)
    # execute if NO exception
    print('else block')

finally:                                 # (optional)
    # execute in any case
    print('finally block')


#RAISE: decide to generate error at any time, ('printing some text')
x = 10
if x > 5:
    raise ZeroDivisionError('W a r N!')  # create an exception with warnings

#ASSERT PORTA AD UN ERRORE SE...
assert (1 in [2,3,4]), 'è Falso, se Vero non davo errore'



    |
    |
    V
# = = = E S E M P I = = = = = = = = = = = = = = = = = = = = =

def ask():
    while True:
        try:
            n = int(input('Input an integer: '))
        except:
            print('An error occurred! Please try again!')
        else:
            break
    print('your number squared is: ', n**2)

ask()


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

try:
    x = 5
    y = 0
    z = x/y
except:
    print('lo script ha date Errore')
finally:
    print ('grazie per aver usato questa App')


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

try:
    for i in ['a','b','c']:
    print(i**2)
except TypeError:
    print('non puoi eseguire tale operazione con', i)
