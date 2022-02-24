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
##  TABLE OF CONTENT
##
##  01. Introduction to Python
##  02. Sequences and Collections
##  03. Flow Control and Repetition
##  04. Functions and Lambda Expressions
##  05. Classes and Inheritance
##  06. Exceptions and File I/O
##  07. Higher-Order Functions and Comprehensions: map, filter, reduce, more
##                              generators, meta-functions, comprehensions
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
###   07. HIGHER-ORDER FUNCTIONS AND COMPREHENSIONS
###



# As seen earlier, Python supports several Functional Programming features,
# including Higher-Order Functions: this means functions are objects like any
# other i.e., first-class entities, and can be stored in variables, modified
# dynamically, passed as function arguments, returned as the value of other
# function calls, etc. (cf. Functions and Lambda Expressions section)

# Why iteration? Why do we need 'for loops'? Recall that iteration as such
# only exists because of computer hardware. Mathematically, repetition is
# induction is recursion. It is also about problem solving: programmers work
# mostly by recognizing categories of problems that come up repeatedly and
# remembering the solution that worked last time; therefore, programmers
# should learn these program patterns (software design patterns) and apply
# them as appropriate for each specific problem.

# Here are the most common patterns for repetition, which high-level (a.k.a.
# higher-order) functions can help model and apply easily: Every (apply/map),
# Keep (filter), Accumulate (reduce), Combine (composition), side effects.

# It is a fact than most complex loops are actually a mixture of the above,
# and could be split into component patterns (example of code refactoring).
# In the end there are very few cases where coding a loop is actually needed.
# (cf. Introduction to Functional Programming slides for more...)



################################
##
##  EVERY PATTERN - APPLY/MAP
##


#%% The EVERY Pattern - This is when we want to perform the same query to a
#   collection of objects. Typically we collect the results of transforming
# each item into something else. Functions: apply/map.


# Example of 'low-level' list processing
lst = [1,2,3,4,5,6,7,8]
rsl = []
for i in range(len(lst)):           # bad (imperative or "C style")
    rsl.append(lst[i]**2)

rsl = []
for n in lst:                       # much better (range loop)
    rsl.append(n**2)                # or: rsl += [n**2]


# Map: from list (or other iterable) to list: map(func,iter) -> list
#      one-to-one mapping: [x1, x2, ... xN] -> [f(x1), f(x2), ... f(xN)]
# Use map to repeatedly apply a transformation and collect the results.

# Example above:
map( lambda n: n**2, lst)           # best - applying a lambda expression!


#%% note: Python has a simple syntax but, not simple enough yet; e.g.
#   Python: map( lambda n: n**2, range(1,1001) )
# vs. Haskell: map ^2 [1..N]

list( map( lambda n: n**2, lst))    # note that map is actually a generator
                                    # (cf. Iterators and Generators section)
lss = ['1','2','3','4']
list( map( int, lss))               # applying a (named) function

list( map( lambda n: n**2, map( int, lss))) # composition - very simple
                                    # but requires multiple traversals

list( map( lambda n: int(n)**2, lss)) # same coded manually, one traversal


# note: Functional Programming is all about function COMPOSITION (see below)
# e.g. Python:  map( ... n**2, map( ... int, range(1,N+1) ))
#  vs. Haskell: map (^2 . int) [1..N]
# Because it is more efficient to compose first, then apply!


#%% Deck of cards example - high level programming
cards = ['1S','3C','08D','QH','7C','10H','JD','13S']

list( map( lambda s: s[-1], cards))

sorted( set( map( lambda s: s[-1], cards))) # 'set' for unicity! [FP]

# get the card values
list(map( lambda s: int(s[:-1]) if s[:-1].isnumeric() else 0, cards))
sum( map( lambda s: int(s[:-1]) if s[:-1].isnumeric() else 0, cards)) #(HHGG!)

list( map( lambda N: 0.70*80+0.30*N, range(40,100,5))) # ex. from Intro


#%% Applying a predicate function to every element, logical composition
list( map( lambda n: n%2 != 0, lst))

def odd(n): return n%2 != 0
list( map( odd, lst))

any( map( odd, lst))                # true if any is true (logical OR)
all( map( odd, lst))                # true if all are true (logical AND)


# Map can handle multiple arguments as well (more examples below)
v1,v2 = [1, 2, 3],[7, 5, 3]
list( map(lambda x,y: x*y, v1, v2))



################################
##
##  KEEP PATTERN - FILTER
##


# The KEEP Pattern - This is when we want to choose some of the items in a
# collection of objects. We collect the results of this selection and forget
# about the other items. Functions: filter.


#%% Example of 'low-level' list processing ("C style" - don't do that)
rsl = []
for n in lst:
    if odd(n): rsl.append(n)

# Filter: from list (or other iterable) to sublist: filter(func,iter) -> list
# Use filter to repeatedly apply a predicate and select items accordingly.
# Examples above:
list( filter(odd, lst))

list( filter( lambda x: x%2 != 0, lst)) # note that filter is also a generator

list( filter( lambda s: not s[0].isdigit(), cards))

list( filter( lambda s: s.startswith(('K','Q','J')), cards))


# Record selection
customers = [('Jack', 'jack@apple.com', 11), ('Jill', 'jill@google.com', 3),
             ('Joe', 'joe@apple.com', 7)]
list( filter( lambda x: 5 < x[-1] < 10, customers))
list( filter( lambda x: x[1].split('@')[1].split('.')[0].lower() == 'apple',
              customers))

#%% More examples

# Text filtering (see also Section 9 Regular Expressions)
txt = 'He was carefully disguised yet he was quickly found (polyonymy).'
list( filter( lambda w: w.endswith('ly'), txt.split()))

# Just for fun (what does this do?)
list(filter( lambda x: x**3 - 15*x**2 + 66*x - 80 == 0, range(1,20))) #10**6

# Checking for palindromes - a simple one-liner!
words = ['geeks', 'geeg', 'keek', 'practice', 'aa', 'Abba', 'racecar']
list(filter(lambda w: w == ''.join(reversed(w)), words))
list(filter(lambda w: w == w[::-1], words))

list(filter(lambda w : w not in words[1::2], words))



################################
##
##  ACCUMULATE PATTERN - REDUCE
##


# The ACCUMULATE Pattern - This is when we want to combine some data by
# applying some process to a collection of objects. We collect the single
# result obtained from aggregating partial results (e.g. sum, count, etc.)
# Functions: reduce.


#%% functools module for higher-order functions
from functools import reduce        # (used to be in main module)

# Reduce: from list (or other iterable) to value: reduce(func,iter) --> value
# Use reduce to repeatedly apply a function and aggregate the results.
# Example of a sum:
reduce(lambda x,y: x + y, lst)      # evaluated recursively, left to right
                                    # i.e. as follows: ((((1+2)+3)+4)+5)+...

sum(lst)                            # same, using built-in sum function
sum(x for x in lst)                 # comprehension style (see below)
sum(x for x in lst[::2])            # same as sum(lst[::2]) in this case

reduce(lambda x,y: x * y, lst)      # product!

from math import prod               # since [v3.8]
prod(lst)                           # same, using built-in prod function

# Careful, 'product' is a different function i.e., Cartesian product
from itertools import product
list( product([1,2,3],['a','b']))


# Example of finding the minimum:
lsr = [10,7,21,5,33,14,50]
reduce(lambda x,y: x if x < y else y, lsr) # 10,7 -> 7; then 7,21 -> 7;
                                           # 7,5 -> 5; 5,33 -> 5; etc.

reduce(min, lsr)                    # same, using built-in min function
min(lsr)                            # (which is recursive, of course)


#%% Functional Programming languages include a generic FOLD function or even
# a family of higher-order functions realizing high level software patterns.
# Folding allows to deconstruct or reduce data. A typical signature for fold
# is  fold f a s  where
# f is a higher-order function taking two arguments, an accumulator and an
# element of the sequence s. It is applied recursively to each element of s.
# a is the initial value of the accumulator and an argument of the function f.
# s is a sequence of elements.
#
# Fold functions come in different kinds, the two main linear ones are foldl
# and foldr, that are left- and right- associative, respectively. [This also
# related to grammars and parsing, cf. chapters 3 and 4.]
#
# Example:  foldl * 10 [3,4,5] evaluates to (((10*3)*4)*5)
# Likewise: foldr * 10 [3,4,5] evaluates to (3*(4*(5*10)))
# Clearly for commutative operators e.g., addition and multiplication, both
# are equivalent. Not so otherwise e.g., subtraction and division.
# Example: foldl / 10 [3,4,5] is (((10/3)/4)/5) = 0.1666
# However: foldr / 10 [3,4,5] is (3/(4/(5/10))) = 0.375
#
# So, reduce in Python is basically foldl (left-associative, as seen above).

import operator                     # for add, sub, mul... (cannot use + * -)
# foldl in Python
foldl = lambda fun, acc, xs: reduce(fun, xs, acc)

foldl(operator.mul, 10, [3,4,5])
foldl(operator.truediv, 10, [3,4,5]) # (truediv is / and floordiv is //)

# foldr can be implemented in Python using the duality theorem, which states
# that a right-associative operation applied to a sequence of elements is the
# same as the left-associative equivalent applied to the reverse sequence.
foldr = lambda fun, acc, xs: reduce(lambda x,y: fun(y,x), reversed(xs), acc)

foldr(operator.mul, 10, [3,4,5])
foldr(operator.truediv, 10, [3,4,5])


# note: C++14 has accumulate, Maple/Mathematica/Matlab have fold (foldl/foldr),
#       Java 8, JavaScript 1.8, R, Swift 3 have reduce (foldl) ...
#       Haskell and List/Scheme have foldl and foldr.

# note: map/filter are high-level replacements for loops that apply a process/
# predicate to a collection of items, respectively. reduce (foldl) is a high-
# level replacement for loops that accumulate a result, hence also for
# accumulator-recursive functions!



################################
##
##  COMBINE PATTERN
##


#%% The COMBINE Pattern - This is when we apply two or more of the patterns
#   above to produce a more complex process e.g., map-reduce where we first
# transform all objects in a collection then aggregate all results.
# Note that COMPOSITION is when we first create a function that is the
# combination of several simpler functions, then apply it to the data.
# (Python does not support implicit composition hence optimization.)

v1,v2 = [1, 2, 3],[7, 5, 3]
reduce(lambda x,y: x+y, map(lambda x,y: x*y, v1, v2)) # dot product!
reduce(operator.add, map(operator.mul, v1, v2))

def dotproduct(v1,v2):
    return sum(map(operator.mul, v1, v2))   # sum pattern (map + add)
dotproduct([1,3,5,7],[2,4,6,8])

sum(x*y for x,y in zip(v1, v2))     # same, using comprehension (see below)


#%% Map-Reduce - a rather famous programming idiom, where we apply some
#   transformation and aggregate the results into one. (It is also Google's
# algorithm of fame: map a search query to multiple servers then aggregate
# and present the results to the client i.e., kind of:
# reduce( combine_results, map( search_query, all_servers))

# Cards example again, using string + operator (i.e., add/concat)
reduce(operator.concat, map(lambda s: s[-1]+'-', cards))[:-1]

# Again, performance is/should not be an issue... Is this different/better?
reduce(operator.concat, map(lambda s: s[-1]+'-', cards[:-1])) + cards[-1][-1]

reduce(operator.add,
       map( lambda s: int(s[:-1]) if s[:-1].isnumeric() else 0, cards))#(HHGG!)
# same as
reduce(operator.add,
       map( lambda s: int(s[:-1]),
            filter(lambda s: s[:-1].isnumeric(), cards))) # [FP]
# also
sum(map( lambda s: int(s[:-1]),
         filter(lambda s: s[:-1].isnumeric(), cards))) # [FP]


#%% note: Functional Programming is all about function COMPOSITION; e.g.
#   Python: sum( map( lambda n: n**3, range(1,1001) ))
# vs. Haskell: (sum . map(^3)) [1..N]
#
# In Python we apply a function and get a result, to which we apply another
# function, etc. -> cascade of function calls f(g(h(x))) or x.h().g().f()
#
# In pure FP like Haskell we build the function via composition (f.g.h) then
# apply it -> only one function call, allows optimization... (f.g.h)(x)

def compose(f,g): return lambda x: f(g(x))  # composing two 1-arg functions

sqint = compose(lambda n: n**2, int)        # convenient but no optimization
list( map( sqint, lss))


# "To calculate the factorial of n, multiply all numbers from 1 to n."
# (i.e. "apply a multiplication function to all numbers from 1 to n.")

def factorial(n):
    return reduce(lambda x,y: x*y, range(1,n+1))

factorial(100)

def rproduct(iterable, start=1):
    return reduce(operator.mul, iterable, start) # generic version
rproduct(lst)                        # usage is similar to sum()
help(sum)
rproduct([2,3,5], start=10)          # evaluates as (((10*2)*3)*5)

def factorial(n):
    return product(range(1,n+1))    # factorial now defined using product

fact = lambda n: product(range(1,n+1)) # equivalent lambda expression

# note: compare vs. Haskell: fact n = product [1..n]


# Slightly obfuscated example (the aulde rot13 cipher)
def rot13(s):
    return reduce(lambda hold,nixt:
                  hold+chr(((ord(nixt.upper())-65)+13)%26+65), s, '')
xtxt='ZNLORABGGBBHFRSHY'
rot13(xtxt)
rot13(rot13(xtxt))


#%% SIDE EFFECTS occur when we apply a function that does not transform the
#   objects in a collection, and does not calculate some result out of the
#   data, but instead produces a by-product (e.g. print, save, etc.)
# It is a fact than most complex loops are actually a mixture of the above,
# and could be split into component patterns (example of code refactoring).
# In the end there are very few cases where coding a loop is actually needed.
# (cf. Introduction to Functional Programming slides for more...)

map( print, lss )                   # which result?
list( map( print, lss ))            # force evaluation (map is a generator)

set( map(lambda x: print('**',x,'**', sep=''), lss )) # same, custom print

# Special var: _ (single underscore) is the "don't care" argument (inherited
# from Prolog!) that is typically used when a variable name is expected but
# we won't use it. This is for readability's sake. Examples:
name, age, _ = ('ali', 23, 'ahb88@yahoo.com')
a, _, c, _, e = (1,2,3,4,5)
a, *_, e, f = (1,2,3,4,5,6)         # extended unpacking

# Same in a range loop where we ignore the elements, because of... side effect:
for _ in map( print, lss ): pass

# BUT, this is of course a case for NOT using 'map' -- since there is already
# a loop anyway(!) and it is the side effect that is being repeated. Thus:
for x in lss: print(x)



################################
##
##  MORE HIGH-ORDER FUNCTIONS
##


#%% Generator functions that implement less common but useful patterns

from itertools import accumulate, starmap, takewhile, dropwhile, compress, \
     zip_longest, repeat, islice, combinations, permutations#, chain, groupby

list( accumulate(lst))              # produces 1 3 6 10 15 ...

ppl = [(2,5), (3,2), (10,3)]
list(map( lambda t: pow(t[0],t[1]), ppl)) # 2^5, 3^2, etc. (not very Pythonic)
list(map( lambda t: pow(*t), ppl))  # (map . star) composition
list( starmap(pow, ppl))            # same but simpler syntax

# if data in separate list:
pv,pe = [2,3,10],[5,2,3]
list( map(pow,pv,pe))

list( map(operator.mul, v1,v2))
list( starmap(operator.mul, zip(v1,v2)))

sum( starmap(operator.mul, zip(v1,v2))) # dot product again


#%% Functional repeat - supply a stream of items to be used with map or zip
list(map(pow, range(10), repeat(2)))    # list of squares

# note: repeat(item) generates infinitely many occurences of the given item(!)
# so this will never end:  for x in repeat('hello'): print(x)
# In the above, range() stops after producing 10 values, and so will repeat.
# repeat(item,n) yields the item finitely i.e., n times.

# repeat thus provides a very fast way to loop a fixed number of times, e.g.
#   for _ in repeat(None, 10000): print('do something 10000 times')
# is much faster and uses less memory than:
#   for i in range(10000): print('do something 10000 times')
# because the former only updates the reference count for the existing None
# object while the latter needs to create 10,000 distinct integer objects!
for _ in repeat(None,5): print('got it?')


# Get items sequentially so long as they satisfy a condition
rl = [3,5,1,8,3,12,4,2,9,16,7]
list( takewhile(lambda n: n<10, rl))    # gets 3,5,1,8,3
list( takewhile(lambda n: n%2!=0, rl))

list( dropwhile(lambda x: x<10, rl))    # yields 12,4,2,9,16,7

list( zip_longest('ABCD', 'xy', fillvalue='_')) # yields Ax By C_ D_


# Filter based on given values, not by applying a predicate
items = ['amy', 'bob', 'ceb', 'dan', 'eva', 'fin', 'geo', 'hal']
selectors = [True,False,True,True,False,True,False]
list(compress(items,selectors))


# also: islice, combinations, permutations, combinations with replacement
#from itertools import islice, combinations, permutations

list(islice(items,2,6))                 # slicing! (not a generator)
print( items[2:6] )                     # same using bracket notation

list(combinations('ABCD', 2))
list(permutations('ABCD', 2))


# also: Itertools Recipes @ https://docs.python.org/3/library/itertools.html



################################
##
##  META FUNCTIONS
##


#%% A function that creates a function! (See also earlier log example etc.)
def make_adder(n):
    def adder(x): return x+n
    return adder

f33 = make_adder(33)                # creating a new adder function
f33 (5)                             # calling the function

def make_adder(n):
    return lambda x: x + n          # same, but simpler

f42 = make_adder(42)
f42 (3)
make_adder(100) (3)                 # same, without a reference

(lambda x: x + 20) (3)              # lambda expression = anonymous function

mad = make_adder
mad.__name__                        # name attribute
f33.__name__                        # 'adder' function
f42.__name__                        # just a lambda

# note: this is similar to Curried Functions (see also Continuations) e.g.
# add(x,y) is really make_adder(x) (y) and each function has one argument.


# A meta function for automatically tracing a function!
def fib(n):
    if n == 0 or n == 1: return n
    else: return fib(n-1) + fib(n-2)

def trace(f):
    def traced_f(x):
        print(f.__name__,'(',x,')', sep='')
        value = f(x)
        print('return', repr(value))
        return value
    return traced_f

fib(3)
fib = trace(fib)                    # replaces fib with the traced version!
fib(3)

# Note: the above 'trace' function assumes f requires a single argument. To
# generalize, we need 'traced_f' to accept a variable number of arguments.
# Also, indenting the output is really needed for clarity(!)

# Using the (built-in) decorator pattern allows defining a function and
# enable 'trace' on it in a single block of code! (but. no indent :(
# Note that in Python decorators are functions, whereas in Java they are
# keywords for the compiler... (cf. section 4 about Functions).
@trace
def fib(n):
    if n == 0 or n == 1: return n
    else: return fib(n-1) + fib(n-2)



################################
##
##  COMPREHENSIONS
##


#%% List comprehension: [f(x) for x in items] same as map(f,items)

# Implicit lambda expression, with intuitive syntax for repetition
[x**2 for x in range(1,11)]

list(map(lambda x: x**2, range(1,11))) # same using map (generator)

# What if using a range loop instead? back to "C-style" coding:
rsl = []                            # <<<
for x in range(1,11): rsl.append(x**2)
# ^^^ similar ^^^     ^^^ low-level list update ^^^


# Comprehensions offer a shorter, more intuitive syntax, but do not add new
# functionality. Everything can be done using HOFs instead.
# A key difference though is that map, filter, etc. are generators which yield
# elements one at time, whereas a list or set comprehension generates all the
# data from the onset (which may take time, and a lot of memory!)

for n in [x**2 for x in range(1,11)]: print(n)
for n in map(lambda x: x**2, range(1,11)): print(n)
# same, but what if 10_000_000 instead of 11? ...

# Nested comprehensions - same as earlier example
[x**2 for x in [int(y) for y in lss]]
list( map( lambda n: n**2, map( int, lss)))

# Composition reduces complexity
[int(x)**2 for x in lss]
list( map( lambda n: int(n)**2, lss))


#%% List comprehension with conditional statement/s
[x for x in range(20) if x%3 != 0]

list(filter(lambda x: x%3 != 0, range(20))) # same using filter (generator)

# Bissextile year example - map and filter mixed
leapyears = [y for y in range(1960,2040)
             if (y%4 == 0 and y%100 != 0) or (y%400 == 0)]

leapyears = [y for y in range(1960,2040,4) if y%100 != 0 or y%400 == 0]
print(leapyears)

# File extension filter example, using set comprehension
files = {'a.txt', 'b.jpg', 'C.HTM', 'd.doc', 'E.pdf', 'f.html'}
htmlf = {f for f in files if f.lower().endswith(('.htm','.html'))}
print(htmlf)                        # yields {'C.HTM', 'f.html'}


#%% Other comprehensions: dictionary, set, tuple, and generators

[(x, x**2) for x in range(1,7)]     # list (sequence) of tuples
{x : x**2 for x in range(1,7)}      # dictionary (not nec. ordered)
{x**2 for x in range(1,7)}          # set (not nec. ordered)

(x**2 for x in range(1,7))          # tuple? no it's a generator!

tuple((x**2 for x in range(1,7)))   # now a tuple is created (constructor)
tuple(x**2 for x in range(1,7))     # simpler (without extra parentheses)

sum( x**2 for x in range(1,7) )     # implicit generator used
sum( (x**2 for x in range(1,7)) )   # same
sum( [x**2 for x in range(1,7)] )   # less efficient, since a list is created


#%% Multi-dimensional list comprehension
[(x, y) for x in [1,2,3] for y in [3,4]]
[(x, y) for x in [1,2,3] for y in [3,4] if x != y]
# same, imperative style ("C style")
rlt=[]
for x in [1,2,3]:
    for y in [3,4]:
        if x != y:
            rlt.append((x,y))

from math import pi
[round(pi, p) for p in range(1, 8)]

matrix = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12] ]
[ [row[i] for row in matrix] for i in range(4) ] # matrix transpose!

list(zip(*matrix))                  # same, using built-in functions!

for a,b,c in zip(*matrix): print(a,b,c) # show the transposed matrix (4 lines)


#%% More examples

# Quick sort, functional programming style!
def qsort(L):
    return ( qsort( [a for a in L[1:] if a < L[0]])
             + [L[0]] +
             qsort( [b for b in L[1:] if b >= L[0]]) ) if L else []

qsort([1,5,7,4,2,6,9,0,3,8])


# Classic FizzBuzz programming exercise again
for k in range(1, 101):
    words = [word for n,word in ((3,'Fizz'), (5,'Buzz')) if k%n==0]
    print(''.join(words) or k)


# note: For really complex cases, it is advised to use map/filter (or even
# range 'for' loops ) rather than comprehensions (esp. with nested loops,
# and/or multiple conditionals).
# The following example are good but not very readable...


# Print the first 20 Fibonacci numbers
print(list(map(lambda x,f=lambda x,f:(f(x-1,f)+f(x-2,f)) if x>1 else 1:
               f(x,f), range(20))))

# Print all prime numbers less than 1000
print(list(filter(None,map(lambda y:y*reduce(lambda x,y:x*y!=0,
map(lambda x,y=y:y%x,range(2,int(pow(y,0.5)+1))),1),range(2,1000)))))


# Print an ASCII version of the Mandelbrot fractal set (will only look nice
# if the window width is 80 columns):
"""
print((lambda Ru,Ro,Iu,Io,IM,Sx,Sy:reduce(lambda x,y:x+y,map(lambda y,
Iu=Iu,Io=Io,Ru=Ru,Ro=Ro,Sy=Sy,L=lambda yc,Iu=Iu,Io=Io,Ru=Ru,Ro=Ro,i=IM,
Sx=Sx,Sy=Sy:reduce(lambda x,y:x+y,map(lambda x,xc=Ru,yc=yc,Ru=Ru,Ro=Ro,
i=i,Sx=Sx,F=lambda xc,yc,x,y,k,f=lambda xc,yc,x,y,k,f:(k<=0)or (x*x+y*y
>=4.0) or 1+f(xc,yc,x*x-y*y+xc,2.0*x*y+yc,k-1,f):f(xc,yc,x,y,k,f):chr(
64+F(Ru+x*(Ro-Ru)/Sx,yc,0,0,i)),range(Sx))):L(Iu+y*(Io-Iu)/Sy),range(Sy
))))(-2.1, 0.7, -1.2, 1.2, 30, 80, 24))
#    \___ ___/  \___ ___/  |   |   |__ lines on screen
#        V          V      |   |______ columns on screen
#        |          |      |__________ maximum "iterations"
#        |          |_________________ range on y axis
#        |____________________________ range on x axis
"""


##
##  END
##
