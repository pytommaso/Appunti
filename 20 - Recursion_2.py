

def sum_recursive(n, current_sum):
    # Base case
    # Return the final state
    if n == 11:
        return current_sum

    # Recursive case
    # Thread the state through the recursive call
    else:
        return sum_recursive(n + 1, current_sum + n)

# - - - - - - - - - - - - - - - - - -

# list is a Recursive Data Structures
attach_head(1,                                                  # Will return [1, 46, -31, "hello"]
            attach_head(46,                                     # Will return [46, -31, "hello"]
                        attach_head(-31,                        # Will return [-31, "hello"]
                                    attach_head("hello", [])))) # Will return ["hello"]

# Recursive data structures and recursive
# functions go together like bread and butter
