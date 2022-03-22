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
##  07. Higher-Order Functions and Comprehensions
##  08. Iterators/Generators and Lazy Data Types: containers etc., iterables,
##                    iterators, generator functions, generator expressions
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
###   08. ITERATORS / GENERATORS AND LAZY DATA STRUCTURES
###



################################
##
##  CONTAINERS / SEQUENCES
##


#%% A container / sequence is a finite data type that stores items linearly,
#   lives in memory, and typically holds all its data in memory too. It must
# support the membership operator in() and the size function len(). Python
# containers are typically iterables, so they work in a 'for' loop.
#
# Examples in Python include: list (and deque), set (and frozenset), dict
# (and defaultdict, OrderedDict, Counter), tuple (and namedtuple), str...

# Boolean expressions
if 1 in [1,2,3]: print('ok')        # list membership

4 not in {1,2,3}                    # set membership
3 in {1:'foo',2:'bar',3:'nil'}      # dict membership (checks the key)
'b' in 'foobar'                     # string membership (substring)

assert(len([1,2,3]) == len({1:'foo',2:'bar',3:'nil'}) == len('foo'))
# (cf. section 10 Reflection and Meta-Programming for assertions et al)


# A container implements the in() function as __contains__() and the len()
# function as __len__(). This is kind of an interface (Java style) except
# it is implicit (not interface construct -- cf. Section 5 Classes again).
'foobar'.__contains__('b')
'foo'.__len__()


#%% Containers / sequences can be created either explicitly, or by calling a
#   constructor (conversion), or programmatically, or using comprehensions.

le = [1,2,3,4,5,6]                  # explicit, using square brackets
lc = list('foobar')                 # using the list class constructor
lr = list(range(1,7))

lp = []
for n in [1,2,3,4]: lp.append(1/n)  # implicit/programmatically with 'for'
[1/n for n in [1,2,3,4]]            # or using comprehension syntax
map(lambda n: 1/n, [1,2,3,4])       # but a generator is different (no list!)

# Usage notes: (1) A generator is the most time/memory efficient, e.g.
# map(lambda n: 1/n, range(1,10**10)) -- produces one item at a time!
# (2) List comprehension has a simpler, more intuitive syntax, but creates
# all the data from the onset, e.g. [1/n for n in range(1,10_000)]
# (3) The above can be combined into a generator comprehension.
# (4) For demo or debugging purposes only, one may use: list(map( ...



################################
##
##  ITERABLES
##


#%% An iterable is a class that allows iterating over its instances' content.
#   It must either be an iterator or return an iterator, so that all of its
# items can be retrieved one by one (e.g., by a range 'for' loop / next).
#
# Iterables include data structures, such as containers/sequences (list, set,
# tuple, dict...) as well as open files, open sockets, URLs, etc. Iterables
# may be finite or may just as well represent an infinite source of data.

for n in [1,2,3]: print(n)          # list is iterable

dc = {1:'foo',2:'bar',3:'nil'}
for key in dc: print(key, end=' ')  # dict is iterable

for c in 'foobar': print(c)         # string is iterable

for line in open('python-dev.txt'): # file is iterable (same as io.readlines())
    if line[0] == '*' and line[-2] == 'S':
        print(line)


#%% One can manually create an iterator and use it. The example below creates
#   a list iterator and repeatedly retrieves the next list item.

lst = [1,2,3]                       # iterable list
liter = iter(lst)                   # iterator on the list
print(liter)
next(liter)                         # consuming the next list item, again and
next(liter)                         # again, until items are exhausted

type(liter)                         # -> list_iterator
type(iter(dc))                      # -> dict_keyiterator


# The 'for' loop automatically creates an iterator on the given iterable and
# repeatedly calls the next() function to get every item, until there is no
# more - then it catches the StopIteration exception raised by next().
for n in lst: print(n)

# Disassembling this code shows the explicit call to GET_ITER, which is like
# invoking iter(). The FOR_ITER instruction is equivalent to calling next()
# repeatedly to get every item (not shown in the Python bytecode because it
# is optimized for speed in the interpreter).
import dis
dis.dis('for n in lst: print(n)')

# note (from CMP 305): In C++ a range loop works only if the container class
# has begin/end and a nested iterator class (with operators: ++ * == etc.)


#%% An iterable implements the __iter__() function to return an iterator,
#   which is either itself, or one created by iter(), or a custom iterator.

# Example making a deck of cards iterable
class Card(object):
    FACE = {11: 'J', 12: 'Q', 13: 'K'}
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank if rank <=10 else Card.FACE[rank]
    def __str__(self):
        return '%s%s' % (self.rank, self.suit) # 1S or 4D or QH ...

class Deck(object):
    SUITS = '♠ ♢ ♣ ♡'.split()       # Unicode! or just: ['S', 'D', 'C', 'H']
    def __init__(self):             # list of 52 cards (cf. Comprehensions)
        self.cards = [Card(r, s) for s in Deck.SUITS for r in range(1, 14)]

    def __iter__(self):             # to iterate over the list of cards
        return iter(self.cards)

# Since a list is iterable, we can always iterate over the list of cards:
deck = Deck()
for card in deck.cards: print(card, end=' ')

# But now that Deck implements __iter__(), it is an iterable and we can use
# the shorter and more intuitive: "for every card in the deck" syntax! i.e.
for card in deck: print(card, end=' ')

# Also we can create a list directly (useful if we do not have access to the
# class variable, or if the data is only created when needed).
cardlist = list(deck)



################################
##
##  ITERATORS / LAZY DATA TYPES
##


#%% An iterator is a stateful object that allows iterating over a given
#   container/sequence. It must implement the next() function, that will
# produce the next item when called. Note that, by definition, iterators
# are always iterables.
# Python include many examples of iterators, some are built-in (range, zip,
# enumerate... then map, filter...) and some are in the itertools module.
from itertools import count, cycle, islice

# An iterator may produce an infinite sequence automatically! e.g.:
counter = count(start=10, step=2)
print(counter)
next(counter)
next(counter)
print(counter)
# ...#
#while True: print(next(counter))   # infinite loop -> need ctrl-C
#for x in counter: print(x)
next(counter)
#
# Usage example: while cond_is_true(): do_something(next(counter))


# Iterators and generators realize lazy data structures / datatypes! [FP]
# Unlike containers / sequences that hold all their data in memory and must
# therefore be finite, lazy data structures can be infinite. Their items are
# only created one at a time, as and when requested.


#%% An iterator may produce an infinite sequence from a finite one:
tricolors = ['Red', 'Green', 'Blue']
colors = cycle(tricolors)
for _ in range(9): print( next(colors), end=' ')

# An iterator may also produce a finite sequence from an infinite one:
for color in islice(colors, 0, 4): print( color, end=' ')
print(next(colors))
for color in islice(colors, 2, 7): print( color, end=' ')
print(next(colors))
for color in islice(colors, 0, 9, 3): print( color, end=' ')


#%% An iterator implements the next() function as __next__(). Any object that
#   has a __next__() function is therefore an iterator. As mentioned, any
# object that returns an iterator via the __iter__() function is iterable.

# Example making a Fibonacci numbers iterator! Note that it is an iterable,
# because of the __iter__() function, and it is its own iterator, because of
# the __next__() function. (No point creating another one...)
class Fib:
    def __init__(self):
        self.prev,self.curr = 0,1   # set initial state / values

    def __iter__(self):
        return self

    def __next__(self):             # next() function:
        fibval = self.curr
        self.curr += self.prev      # calculate next value
        self.prev = fibval          # update state
        return fibval               # return current value

#for n in Fib(): print(n, end=' ')  # infinite!

fibiter = Fib()                     # instance of Fib iterator
#fibiter = iter(Fib())
for _ in range(20): print( next(fibiter), end=' ') # for loop calls next()

list( islice(fibiter, 5, 15))       # isslice iterator calls next()

# The state of the iterator (Fib object) is fully kept inside prev and curr
# instance variables. Every call to next() does two things: modify its state
# (for the following next() call) and return the result of the current call.



################################
##
##  GENERATORS (FUNCTIONS)
##


#%% A generator function is a special kind of iterator i.e., a simple function
#   that automatically creates and returns an iterator, without having to code
# the class and __iter__() and __next__() functions. A generator function
# is characterized by the presence of the 'yield' operator.
#
# We call the generator only once, to get the iterator (it's like a factory),
# then we can repeatedly call the next() function on the iterator as before.
# In Python, many built-in iterators are actually implemented as generators.

# Example of a Fibonacci numbers generator:
def fib():
    prev, curr = 0, 1
    while True:                     # allows a potentially infinite sequence
        yield curr                  # pause the loop and returns the value
        prev, curr = curr, prev + curr # update state / values

#for n in fib(): print(n, end=' ')  # infinite! note: same syntax as above!

fibgen = fib()                      # iterator created by fib()
for _ in range(20): print( next(fibgen), end=' ') # for loop calls next()

list( islice(fibgen, 0, 10))        # isslice iterator calls next()

# The state of the generator (returned by fib()) is kept inside prev and curr
# function variables. (This is roughly equivalent to static variables in C++.)
# Every call to next() runs one iteration of the loop, which does two things:
# modify its state and return the current value.


#%% Example: Lazy data type for generating an infinite sequence of integers.
#   It works exactly like count(), except it always starts at 0.

def integers():
    '''set of natural numbers'''
    n = 0
    while True:
        yield n
        n += 1

intiter = integers()
next(intiter)
next(intiter)
# ...
list( islice(intiter, 100, 120))

#for n in integers(): print(n)      # infinite sequence of numbers


#%% Generators can be built from other generator/s; examples:
intgen = map(lambda n: n**2, range(1,1_000_000_000))
print(next(intgen))
print(list( islice(intgen, 0, 10)))

def squares():                      # generates squares infinitely
    for n in integers():            # by generating numbers infinitely
        yield n * n                 # and calculating the square value

list( islice(squares(), 10, 20))

# Implement take() like in Haskell [FP], similar to islice, and others.
# note: Same logic as found in the range 'for' loop implementation!
def take(n, seq):
    '''returns first n values from a given sequence / iterable'''
    seq = iter(seq)
    result = []
    try:
        for i in range(n):
            result.append(next(seq))
    except StopIteration: pass
    return result

print( take(10, squares()))         # take only first 10 values

sq = squares()
print(take(10, sq)) ; print(take(10, sq)) ; print(take(10, sq))

print( take(10, tricolors))         # take 10 values out of? (try it)



################################
##
##  GENERATOR EXPRESSIONS
##


#%% Generator expressions are... comprehensions! (which are equivalent to map
#   or filter...) See section 7 about Higher-Order Functions and Comprehensions
# for many good examples.

# In the cases below, all items must be produced (exhaustively) because list,
# set, and dictionary must be created, which are explicit data structures.
numbers = [1,2,3,4,5,6,7,8]
[n**2 for n in numbers]             # list comprehension
{n**2 for n in numbers}             # set comprehension
{n : n**2 for n in numbers}         # dict comprehension

# By contrast, the equivalent use of map only returns an iterator!
map(lambda n: n**2, numbers)
list( map(lambda n: n**2, numbers)) # forces iterator to produce all values

# The following generator expression is equivalent to the above call to map;
# thus it returns an iterator (note the parentheses - but it's not a tuple!)
(n**2 for n in numbers)

nsquares = (n**2 for n in numbers)  # iterator created
next(nsquares)                      # first square value returned
list(nsquares)                      # explicit list exhaustively generated
for n in nsquares: print(n, end=' ')# all remaining values generated/printed

# Equivalent generator function
def squares_of(numbers):
    for n in numbers:
        yield n**2

for n in squares_of(numbers): print(n, end=' ')
for n in squares_of(range(20)): print(n, end=' ')

sqg = squares_of(numbers)           # iterator created
next(sqg)                           # first square value returned
# ...
for n in range(4): print( next(sqg), end=' ') # more values


#%% The built-in sum() function takes a sequence (iterable) of numbers as
#   argument, or an iterator! The iterator can be created by map, a generator
# expression, or a generator function. Examples:

sum( [1,4,9,16,25,36,49,64] )
sum( {1,4,9,16,25,36,49,64} )
sum( map(lambda n: n**2, numbers) )
sum( (n**2 for n in numbers) )
sum( squares_of(numbers) )
# Note that, when there is only one argument to the calling function, the
# parentheses around the generator expression can be omitted:
sum( n**2 for n in numbers )

# Thus the expressions below are all equivalent; first one is best obviously.
[n**2 for n in numbers]
list(n**2 for n in numbers)
list((n**2 for n in numbers))


#%% Generators are very powerful programming constructs. They allow you to
#   write streaming code with fewer intermediate variables and data structures,
# they are memory and CPU efficient, and typically require less code.
#
# So why do we need iterators if generators are so much simpler and better?
# Well, that is whenever we already have a class, and we just want to modify
# it to provide access to its data!
# In the above, Fib should just be a generator/function but Deck (of cards)
# must be a class. Other examples include all abstract data structures e.g.,
# Stack, Queue, etc. A Binary Search Tree class can (and should) implement
# all traversal operations as iterators! (default being in-order traversal)


# Rule of thumb: whenever you have (imperative style) code similar to the
# following LoopingFunction, replace it with IterFunction:
#
#   def Loop_XFunction(...):          def Iter_XFunction(...):
#      result = []                        for ... in ... :
#      for ... in ... :                       yield x
#          result.append( x )
#      return result
#
# Their usage e.g., in a 'for' loop, is exactly the same of course. Then,
# if you really need an explicit list structure in the end, just do this:
#    list( Iter_XFunction() )



################################
##
##  ASYNCHRONOUS GENERATORS [v3.6]
##


#%% Python now uses asynchronous coroutines instead of threads. Asynchronous
#   coroutines are implemented as an extension to generators, with the key
# benefits of using less memory and being easier to start, to use, and to
# maintain, than traditional threads. For details see the Coroutines and
# Asynchronous Coroutines section in 13. Threads and Concurrency.



################################
##
##  MISC IMPLEMENTATION NOTES
##


# One key difference between Python 3 and 2 is that many functions have been
# re-written as iterators/generators. The most typical examples are range(),
# zip(), enumerate(), count(), etc. (There are many...)

# On a related note, this is also the difference between e.g., reversed(x)
# and x[::-1]. Slicing creates a whole new list, copying every element from
# the original, whereas reversed() just returns an iterator that walks the
# original list in reverse order, without copying anything!



##
##  END
##
