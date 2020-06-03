# This problem was asked by Jane Street.

# cons(a, b) constructs a pair, and car(pair) and cdr(pair) 
# returns the first and last element of that pair. 
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

# Implement car and cdr.

# algebraic laws: (car x xs) = x 
#                 (cdr x xs) = xs 
#                 (checked runtime error with car of empty list)
#                 (cdr []) == []
#                 (cdr x []) == []

def car(f):
	return f(lambda x,y: x)

def cdr(f):
	return f(lambda x,y: y)

# print(cons(3,4)(lambda x,y: x))
# print(car(cons(3,4)))
assert car(cons(3,4)) == 3
assert cdr(cons(3,4)) == 4