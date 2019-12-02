

# COMBO EXAMPLE
game=[1,2,3]

print(len(game))

print(range(len(game)))

for n in reversed(range(len(game))):
    print(n)

for n in enumerate(reversed(range(len(game)))):
    print(n)

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

def master_yoda(text):
    print(' '.join(text.split(' ')[::-1]))

master_yoda('ciao mamma bella')

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

def almost_there(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

def has_33(nums):
    for i in range(0, len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

def palindrome(s):
    s = s.replace(' ','')
    reversed = (s[::-1])
    print(s == reversed)


r = 'nurres run'

palindrome(r)
