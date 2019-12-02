
# VARIABLES
numbers
strings
bool            # False<True    !
NoneType	       None
# Bool convert and back
bool('string')
bool(' ')
bool('')
bool(3)
bool(0)

str(True) => 'True'
int(True) => 1
int(False) => 0


# VARIABLES GROUPED
lists
tuples
dictionaries
sets            # don't allow for duplicate items!   ex: set(list)
arrays          # ???


# Iterable - ITERATOR
Iterable:               string, list, tuple, dict, set, frozenset
ITERATOR:               IS ITERABLE, HAS next() method
Iterable-->ITERATOR:    iter(iterable) from itertools
