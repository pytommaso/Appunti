

# Recursion:
# This means that the function will continue to
# call itself and repeat its behavior until
# some condition is met to return a result.


# n FATTORIALE EXAMPLE:

def factorial_recursive(n):
    # Base case: 1! = 1
    if n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n-1)

RETURS: 5*factorial_recursive(4)
            4*factorial_recursive(3)
                3*factorial_recursive(2)
                    2*factorial_recursive(1) = 2 * 1
                = 3 * (2 * 1)
            = 4* (3 * (2 * 1))
        = 5* (4* (3 * (2 * 1))) = 120


# SANTA EXAMPLE
# houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]
#
# # Each function call represents an elf doing his work
# def deliver_presents_recursively(houses):
#     # Worker elf doing his work
#     if len(houses) == 1:
#         house = houses[0]
#         print("Delivering presents to", house)
#
#     # Manager elf doing his work
#     else:
#         mid = len(houses) // 2
#         first_half = houses[:mid]
#         second_half = houses[mid:]
#
#         # Divides his work among two elves
#         deliver_presents_recursively(first_half)
#         deliver_presents_recursively(second_half)
