###############################################################################
###
###   PYTHON 3: FROM IMPERATIVE TO OBJECT-ORIENTED TO FUNCTIONAL PROGRAMMING
###
###   Copyright © 2013-2021 Michel Pasquier
###
###   This tutorial is meant to be used in class, interactively. By design,
###   it lacks the detailed explanations which are given by the instructor.
###   For these, and much more, see the many references provided throughout
###   these files as well as on the course site.
###



################################
##
##  TABLE OF CONTENT.
##
##  01. Introduction to Python
##  02. Sequences and Collections
##  03. Flow Control and Repetition: comparison, conditionals, iteration;
##                                   range, enumerate, zip; and more ...
##  04. Functions and Lambda Expressions
##  05. Classes and Inheritance
##  06. Exceptions and File I/O
##  07. Higher-Order Functions and Comprehensions
##  08. Iterators/Generators and Lazy Data Types
##  09. Regular Expressions and Pattern Matching
##  10. Reflection and Meta-programming
##  11. Modules and Libraries in Python
##  12. Graphics and GUI Extensions
##  13. Threads and Concurrency
##  14. Miscellanies and References
##  15. Scientific Python
##



###############################################################################
###
###   03. FLOW CONTROL AND REPETITION
###



################################
##
##  COMPARISON
##


#%% Comparison examples, with cascading
x = y = 5
0 < x
0 < x or 0 < y                      # intuitive syntax! (and, or, not)
x > 1 and x <= 10                   # "C style" comparison
1 < x <= 10                         # same, Python style (a.k.a. 'pythonic')

0 < x == y                          # same as 0 < x and x == y
x is y                              # intuitive again (but see below)

5 and True                          # returns True
5 and 10                            # returns 10
10 or False                         # 10 (allows cascading operations)

# Order of precedence: or, and, not, in, not in, is, is not, <, >, ...
# e.g.
not False and False                 # False
not (False and False)               # True
not False or True                   # True
not (False or True)                 # False
False and True or True              # True
False and (True or True)            # False


#%% Comparing objects vs. references: use operator '==' to compare values
#   and objects; use 'is' to compare only references.

n1 = 1.23 ; n2 = 1.23               # sequential assignment (or 2 lines)
n1 == n2                            # same value
n1 is n2                            # different identity (object)
n3 = n1
n1 is n3                            # references to the same object

# Python has a SyntaxWarning to warn about dubious syntax (that is typically
# not a SyntaxError. Example:
#n1 is 1.23                          # Warning: use == to compare literals

l1 = [1,2,3] ; l2 = [1,2,3]         # 2 identical lists
l1 == l2                            # same value, but
l1 is l2                            # different identity (object)

# Object identity (ID) - this is guaranteed to be unique among simultaneously
# existing objects (note that CPython uses the object's memory address).
print(id(l1))
id(l1) == id(l2)                    # same as: l1 is l2


#%% Particular cases:
s1 = 'hi' ; s2 = 'hi'
s1 == s2                            # same value
s1 is s2                            # True! (only one string, like in Java:
                                    # strings are immutable -> shared)

s3 = 'h' + 'i'                      # creates another string 'hi'
s1 == s3                            # same value.
s1 is s3                            # same identity again(!)

s4 = ''.join(['h', 'i'])            # creates another string 'hi'
s1 == s4                            # same value
s1 is s4                            # different identity

n1,n2 = 10**6, 1_000_000            # integers are also immutable
n1 == n2                            # True, as expected: same value
n1 is n2                            # same identity (object) again

x1 = 2**100000 ; x2 = 2**100000     # counter example, very large integer
x1 == x2                            # same value
x1 is x2                            # different identity



################################
##
##  CONDITIONAL STATEMENTS
##


#%% Classic if-then-else block

x,y = 4,3
if x > y:                           # parentheses are optional, colon is not
    print("it's true then")         # indentation serves as block delimiter

if x < 0:
    print('negative')
elif x > 0:                         # optional conditions (as many...)
    print('positive')
else:                               # optional default case
    print('zero!')


if (x>=10 and x<100):               # "C style" coding (bad) - no && though
    print('2-digit number')

if 10 <= x < 100:                   # "Pythonic" style (good)
    print('2-digit number')


#%% Nested conditional statements
if x > 0:                           # if block
    if y > 0:                       # indented hence nested if block
        z = x * y
    elif y < 0:                     # matching based on indentation
        z = x * -y
    else:
        z = 1
    print('z =', z)                 # back to outer if block scope
else:
    z = -x * x
print('done')                       # back to main script (top level)


#%% Alternative syntax

# Equivalent to C/C++ statement: ( Test ? Exec_if_True : Exec_if_False )
# which becomes: Exec_if_True if Test else Exec_if_False [FP]
x, y = 10, 5
minxy = x if x < y else y           # (x) < (y) ? (x) : (y)) in C/C++

# The same syntax is used in lambda expressions (cf. section 4 Functions)
# and in comprehensions as well (cf. section 7 Higher-Order Functions).

# Also to make code shorter and nicer (more readable/writable):

def fmax(a, b): return a if a > b else b    # functional style [FP]
# vs.
def imax(a, b):                             # imperative style
	if a > b: return a
	else: return b



################################
##
##  SWITCH-CASE STATEMENTS
##


# Included in Python 3.10, switch-case statements go beyond C-like switch
# statements to offer advanced structural pattern matching, akin to what is
# available in functional programming languages (such as Haskell, notably).


#%% Simple switch-case [2DO] -- cf. https://www.python.org/dev/peps/pep-0634/

# Pattern matching [2DO]



################################
##
##  LOOP STATEMENTS
##


# In reality, loops are not needed at all (cf. section 7 about Higher-Order
# Functions and iteration patterns). Even if, recursion is often better...


#%% Classic while loop

x = 5
while x > 0:
    print('x is', x)
    x -= 1

# Example calculating and printing Fibonacci numbers
a,b = 0,1
while b < 100:
    print(b)
    a, b = b, a+b                   # parallel assignment (nice, efficient)


# Forever loop, needs keyboard interrupt (Ctrl+C) to halt:
#while True: pass

def function_to_code_later():       # (function body cannot be empty)
    pass                            # used as "to do" marker


#%% For loop, iterates over anything that is iterable (e.g., a sequence)

for item in [1,2,3]:                # list
    print(item)

lst = [1, 'two', [3, 'three', 0x111], 'four']
for item in lst:                    # list all items (Java/Python/C++ style)
    print(item)

for i in range(len(lst)):           # same ("C style" - very bad)
    print(lst[i])

for i in range(len(lst)):
    print('lst[', i, '] =', lst[i]) # index + item ("C style" again)

for i, v in enumerate(lst):         # same (the Python way!)
    print('lst[', i, '] =', v)


for item in 'a', 'b', 'c':          # implicit tuple
    print(item)

s = 'sample string'
for c in s: print(c)                # string as char sequence, as: list(s)

d = { 'fr': 'France', 'uk': 'United Kingdom', 'it': 'italy' }
for k in d.keys(): print(k)         # dictionary keys

for k in d: print(k)                # same (simpler/better)

for v in d.values(): print(v)       # dictionary values

for k in d: print(d[k])             # same

for i in range(20):                 # range iterator: generates all items,
    print(i)                        # one at a time (one per iteration)


#%% Classic FizzBuzz programming exercise: "Write a program that prints the
#   numbers from 1 to 100. But, for multiples of three, print "Fizz" instead
# of the number and, for multiples of five, print "Buzz" instead. For numbers
# which are multiples of both three and five print "FizzBuzz".

fizz,buzz = 'Fizz','Buzz'           # imperative programming style version
for k in range(1,33):
    if k % 15 == 0:
        print(fizz+buzz)
    elif k % 3 == 0:
        print(fizz)
    elif k % 5 == 0:
        print(buzz)
    else:
        print(k)
    k += 1

# A shorter/better functional programming style version [FP], and therefore
# also a more Pythonic solution, is:
for k in range(1, 33):
    print('Fizz' * (not k%3) + 'Buzz' * (not k%5) or k)

# Even more Pythonic, using list comprehension and * operator (cf. section 7)
print( *['Fizz' * (not k%3) + 'Buzz' * (not k%5) or k
         for k in range(1, 33)], sep='\n')


################################
##
##  MORE ITERATION EXAMPLES
##


#%% Range iterator / iterable
print(range(5))                     # not a list, actually
type( range(5))                     # it's a range object - an iterator!
list( range(5))                     # converting to list forces iteration

for i in range(5): print(i)         # for loop also forces iteration

set(range(2,8))                     # converting to a set
tuple(range(2,8,2))                 # converting to a tuple, with step of 2
list(range(100,0,-10))              # descending order

# Note: suppose range parameters are given in a list (e.g. passed to a function)
r = [2,12,2]
#list( range(r))  # TypeError: 'list' object cannot be interpreted as integer
list( range(r[0],r[1],r[2]))        # correct but inconvenient
list( range(*r))                    # flatten the list! via unpacking
                                    # (works for all iterables: list, tuple...)

print(enumerate(('a','b','c')))     # enumerate object - another iterator
print(list(enumerate(('a','b','c'))))# converting to list forces iteration


#%% More loops
rg = range(1, 11, 2)
for ri in reversed(rg):             # iterating in reverse, useful if the
    print(ri)                       # range is not known beforehand (arg)
for i in range(9,0,-2): print(i)    # same (hardcoded)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for fruit in sorted(set(basket)):   # converting to a set removes duplicates!
    print(fruit)                    # then into a sorted list [FP]

# Iterating with multiple elements at the same time
for x,y in [(1,2), (7,4), (3,6)]: print(x,'<->',y)

d = { 'fr': 'France', 'uk': 'United Kingdom', 'it': 'italy' }
for item in d.items(): print(item)          # iterating over tuples
for k,v in d.items(): print(k,'<->',v)      # unpacking multiple items


#%% Synchronized iteration!
fstnames = ['Alex',    'Bobby',   'Clara']
surnames = ['McGuire', 'Nielsen', 'Olsen', 'Xtra_ignored']

for n, s in zip(fstnames, surnames):
    print(f"{n}'s surname is {s}.")

z = zip(fstnames, surnames)         # zip object - another iterator
next(z)                             # (cf. Iterator / Generator section)
next(z)                             # next() generates the next item
print(list(z))                      # print remaining items

# note: enumerate() could be implementing easily using zip() and range()
t = ('a','b','c')
list(zip(range(len(t)),t))          # same as: list(enumerate(t))


#%% Assignment expression in loops

# The assignment expression (since Python v3.8) allows writing shorter code
welcome = 'hello'
print(welcome)
# These two steps can be combined using the 'walrus' operator := i.e.:
print(welcome := 'hello')

# note: This addresses a common error in C++ etc.

# One pattern that shows some of the strengths of assignment expressions is
# a while loop where you need to initialize and update a variable, e.g.

def get1():
    data = []                       # correct logic, but it's verbose and
    last = input('? ')              # the input() statement is repeated...
    while last != '.':
        data.append(last)
        last = input('? ')
    return data

def get2():
    data = []                       # alternative logic, still verbose
    while True:
        last = input('? ')          # this time no statement is repeated,
        if last == '.': break       # but that infinite loop with a break...
        data.append(last)
    return data

def get3():
    data = []                       # more concise logic and code, where the
    while (last := input('? ')) != '.': # test is back where it belongs
        data.append(last)
    return data


#%% Loop else! where code executes after loop completion (like 'finally')
for i in range(5):
    print('i =', i)
else: print('done')                 # here 'else' makes no difference

# Example of identifying prime numbers
for n in range(2, 20):
    for x in range(2, n): # try all divisors (see note below)
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number') # only when not breaking from the loop

# note: the classic improvement that is to stop the loop at sqrt(n) fails here
# if coded as range(2,int(n**0.5)) because, when n is 2 range(2,num) is empty,
# the if check is not performed, and therefore the else block executes...

# Another example
def guess_password():
    for i in range(3):
        password = input('Enter password: ')
        if password == 'secret':
           print('You guessed the password!')
           break
    else:
        print('3 incorrect password attempts')

# If you make an incorrect guess 3 times in a row, the message from the else
# block will be printed; but if you guess the correct password in your first
# three tries, the message from the else block will not be printed...

# The usual advice, however, is NOT to use the loop-else statement, because
# it can be replaced by more fundamental and understandable Python constructs.



##
##  END
##
