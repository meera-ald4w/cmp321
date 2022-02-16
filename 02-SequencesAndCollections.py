###############################################################################
###
###   PYTHON 3: FROM IMPERATIVE TO OBJECT-ORIENTED TO FUNCTIONAL PROGRAMMING
###
###   Copyright © 2013-2021 Michel Pasquier
###
###   This comprehensive tutorial is meant to be used interactively in class.
###   By design, it lacks the detailed explanations which are offered by the
###   instructor. For these, and much more, see the many references provided
###   throughout these files as well as on the course site.
###



################################
##
##  TABLE OF CONTENT
##
##  01. Introduction to Python
##  02. Sequences and Collections: generic data structures (and algorithms)
#                                  list, tuple, dictionary, set, and more...
##  03. Flow Control and Repetition
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
###   02. SEQUENCES AND COLLECTIONS
###



################################
##
##  LISTS
##


#%% The list class is a mutable, sequential data structure, implemented as a
#   variable-length array of references to objects, using exponential over-
#   allocation for performance.
#
# It is the one data structure to use instead of static/dynamic arrays or
# singly/doubly connected node structures or vector/list objects (C++/Java).
# Note also that it provides better readability and writability...

l = ['one', 'two', 'three']
type(l)                             # 'list' object
isinstance(l, list)                 # checking the type (hierarchical)
isinstance(l, (list,tuple))         # OR: true if a list or a tuple

l.append('four')                    # appending one item at the end
l.insert(2,'more')                  # inserting at position (given index)

l = l + ['five', 'six']             # list concatenation
['zero'] + l
l.extend([7,8,9])                   # appending multiple items
l * 2                               # repetition! -> new list object

ll = l[:]                           # list copy
l2 = l.copy()                       # many classes implement copy / deepcopy
l3 = list(l)                        # same (like copy constructor)

# Careful again, there is no checking: list = [1,2,3] destroys the class!
# It works because a "class name" is just a reference to an object (instance
# of the 'class' class!) and references can be changed (reassigned).


#%% Generic containers and sequences (only contains references anyway!)
lst = [123, 4.5, ['hi'], 6-7j, 'wow', (8,9), False, 0xFF, ]
print(lst)                          # (trailing comma is ok too!)

a,b,c,d,e,f,g,h = lst                 # unpacking all elements
newlst = [ a,b,c,d,e,f,g,h ]

for item in lst:                    # 'for' loop needs an iterable e.g., list
    print(item, '\t: ', type(item)) # (cf. section 8 Iterators and Generators)

for item in lst[::2]:               # slicing allows for custom range loops!
    print(item, '\t: ', type(item)) # (unlike in C++/Java -> need iterators)


#%% Nested lists and indexing
nst = [1, [3.5, 'hi', 2-3j, ['nothing', False]], 0xFFFF ]
len(nst)
nst[1]
nst[1][-1][0]

# Multi-dimensional 'arrays' e.g., matrices
mtx = [ [11, 12, 13],
        [21, 22, 23],               # 1 line or multiple lines (rows) for
        [31, 32, 33] ]              # clarity's sake (bracket delimiters)
mtx[1][2]

# note: use NumPy module for really fast array/matrix and other math functions!
try:
    import numpy
    na = numpy.array(range(10))
    print(na)                       #-> [0 1 2 3 4 5 6 7 8 9]  (w/out comma)
    nmtx = numpy.array(mtx)         # compare repr. of nmtx vs. mtx above
    print(nmtx)
except ModuleNotFoundError:         # (cf. section 6 Exceptions and File I/O)
    print('numpy not installed')


#%% List indexing and slicing (like with strings, other containers/sequences)
i2 = l[2]
l2 = l[2:4]
l[3] = 'None'                       # replacing one item
print(l)
l[2:4] = [3, 33, 333]               # replacing a slice! (multiple items)
del l[-1]                           # remove last element (reference)
del l[0:2]

lx = list(range(12))                # (range is a generator; see that section)
lx[2:6] = 'oops'                    # string (implicitly) as list!
list('oops')                        # explicit conversion
#lx[2:6] = 111                      # TypeError: can only assign an iterable
lx[2:6] = ['oops']

lx[0:4] = []                        # remove slice - same as del lx[0:4]
lx[1] = ['a', 'aa', 'aaa']          # one item replaced by nested list!
lx[1:2] = ['a', 'aa', 'aaa']        # slide (one item) replaced by others
lx[:] = []                          # clear the list


#%% List comparison (recursive)
[1, 2, 3] < [1, 2, 4]               # works with lists, tuples ...
(1, 2, 3) < (1, 2, 3, 4)            # (but not with dictionaries)
[1, 2, 3] == [1.0, 4/2, 2*1.5]
[1, ['a', 'b'], 3] < [1, ['x', 'y'], -2]

l2 = l[:]                           # copy
l == l2                             # same items - compares the values
l is l2                             # different object - compares references!
                                    # (more in the next section)


#%% More list operations
nl = [1,2,4,8,16,32]
rl = nl.copy()                      # same as nl[:]
rl.reverse()                        # reversing in place, vs. reversed(nl)
sl = sorted(rl)                     # new sorted list
print(nl, rl, sl, sep='\n')
rl.sort()                           # sorting in place
#l.sort()                           # TypeError: '<' not supported (int vs. str)

bl = ['hello', 'cheers', 'hi', 'bye']
sorted(bl)                          # default sort, in ascending order
sorted(bl, reverse=True)            # in descending order (optional parameter)
sorted(bl, key=len)                 # using a custom key function [FP]

bl.remove('hi')                     # removing a given value (string 'hi')
rl.remove(4)                        # removing a value (int 3 here)
#rl.remove(77)                      # ValueError: x not in list
rl.pop(3)                           # removing at position (4th item here)
print(rl)
rl.count(4)                         # number of items with value 4

# References again
a = [1, 2, 3]                       # 'a' reference to a 'list' object
b = a                               # 'b' another reference to the same
a.append(4)                         # list object modified
print(b)
b = a[:]                            # now 'b' is copy of 'a' (diff object)
a.append(5)
print(a, 'vs.', b)


#%% List is all you need - serves as array, stack, queue...

# List as Stack (fast)
nl.append(6)                        # push: same as append (at the end)
nl.pop()                            # pop: delete and return last item
nl[-1]                              # top: return last item

# List as Queue (slow)
nl.append(8)                        # enqueue: same as append (at the end)
nl.pop(0)                           # dequeue: delete/pop the first item

# A more efficient queue data structure is provided in the collections module,
# that is a double-ended queue. It is implemented smartly as a linked-list of
# blocks of pointers that efficiently grows of shrinks to accomodate data.

from collections import deque
q = deque(['Eric', 'John', 'Mike'])
q.append('Toby')                    # enqueue: same as append
q.popleft()                         # dequeue: delete/pop left (first) item
print(q)

enq = deque.append                  # one can even create function aliases!
deq = deque.popleft                 # (just more references)
deq(q)
enq(q,'Zara')


#%% More collections are available e.g., min heap (for priority queue) via
#   heapq algorithms, plus utilities such as merge, nlargest, nsmallest...

from heapq import merge, nlargest
nlargest(3, [4,3,6,2,8,0,7,1,9,3])  # cf. selection problem

list(merge([1,3,5,7], [0,2,4,8]))   # (merge is a generator; see that section)

def merge_sort(a):                  # recursive version, imperative style
    if len(a) <= 1: return a        # (but using Python features)
    mid = len(a) // 2
    left = merge_sort( a[:mid] )
    right = merge_sort( a[mid:] )
    return merge( left, right)

list( merge_sort([3, 4, 1, 9, 0, 8, 6, 2, 7, 5]))

def merge_sort(a):                  # functional programming version [FP]
    return a if len(a) <= 1 else \
           merge( merge_sort(a[:len(a)//2]), merge_sort(a[len(a)//2:]))



################################
##
##  TUPLES
##


#%% The tuple class is like a lightweight, immutable list. It offers fewer
#   methods but much better performance. For instance, the memory used for
#   tuples is managed very cleverly to minimize de/allocation...
#
# Note that tuples are used a lot *inside* Python to implement many language
# features, such as parallel assignment, returning multiple values from a
# function (see examples hereafter), etc.

t = (1,2,3)                         # a 'tuple' object
type(t)

#t[1] = "one"                       # TypeError: no item assignment

u = 2, 4, 6                         # packing (parentheses are optional)
print(u)
t + u[1:2]                          # new tuple, via slicing + concatenation

x,y,z = t                           # unpacking (num of values must match)

for item in t: print(item)          # tuples are also iterables

a, b = 1, 2                         # parallel assignment again: implemented
a, b = (1,2)                        # via a tuple!
tp = (1, 2)                         # same, items are first packed in a tuple
a, b = tp                           # which is then unpacked

def sqpair(x): return x, x**2       # functions can return multiple values!
v,v2 = sqpair(7)                    # (w/ good readability and writability)

def sqPair(x): return tuple(x, x**2)# same, but tuple is created explicitly

u = 2,                              # singleton (comma needed, else 'int')
u = ('two',)                        # singleton (comma, else 'string')


#%% More examples e.g. conversion
lt = list(t)                        # list constructor (with tuple arg)
lt[1] = -2 ; lt.append(4)
tt = tuple(lt)                      # tuple constructor (with list arg)

pA , pB = (2,7) , (5,-1)            # two 2D points (immutable!)
pA[0] * pB[0] + pA[1] * pB[1]       # dot product

# More elegant with NAMED TUPLES i.e., tuples with fields (immutable struct)
from collections import namedtuple
point = namedtuple('point', ['x', 'y']) # 2D point struct (opt: verbose=True)

pA, pB = point(2,7) , point(5,-1)   # same syntax as when using a point class
pA.x * pB.x + pA.y * pB.y           # now accessing fields/attributes by name!

px, py = pA                         # unpack like a regular tuple
px == pA.x

#pA.x = 5                           # AttributeError: can't set attribute


# A general design rule is that "tuples have structure, lists have order".
# So tuples are used as heterogeneous data structures containing unmodifiable
# data e.g., the name, ID, and birthdate of a person, the X,Y coordinates of
# a point in the plane, numbers, etc.
# While they can contain any data, lists are homogeneous more often than not
# e.g., one may define a list of student names or IDs, a shopping list (of
# products), a list of 2D points (for a polygon), etc.
# Yes, the list data structure in Python is generic (it can store anything)
# but that is really a consequence of having dynamic types...


# note: A tuple is immutable, which means we cannot add, remove, or change any
# of its content e.g., any of the four references in the example below.
# However, through those references, we can modify the objects being referred
# to, IFF they are mutable (like in Java) e.g., any of the lists below.
tt = ([1, 2, 3], [4, 5], [6, 7, 8], [9])
#tt[1] = [444,2,1]                  # TypeError: ... no item assignment
tt[1][0] = 444
tt[1][0:2] = ['tada', 'voila', 'done']



################################
##
##  DICTIONARIES
##


#%% The dictionary class is a mutable associative array (a.k.a. map) that is
#   implemented as a hash table with open addressing, with sophisticated
#   hashing and rehashing functions (see below).

# A dictionary stores key-value pairs e.g.
d = { 'fr': 'France', 'uk': 'United Kingdom', 'it':'???' }
type(d)                             # 'dict' object
print(d)                            # actual order may depend on hashing

#d[1]                               # KeyError: only key indexing allowed
d['fr']                             # same as d.get('fr')
d.keys()
d.values()
d.items()

for k in d: print(k)                # dictionaries are iterables

for k in d.keys(): print(k)         # same, iterating over dictionary keys

for v in d.values(): print(v)       # iterating over dictionary values
for k in d: print(d[k])             # same, getting values from the keys


d['it'] = 'Italy'                   # replacing value for given key
d['ch'] = 'Switzerland'             # adding new key-value pair
del d['uk']                         # removing key-value pair

d[42] = 'yes'                       # adding key 42 (not an index)

a,b,c = {1:'a', 2:'b', 3:'c'}       # unpacking a dictionary (keys)
print( [*d] )


#%% Example of a dictionary of 2D points (defined earlier)
points = { 'A': (2,5), 'B': (4,1), 'C': (-2,0), 'P': point(7,11) }

print(points.keys())                # iterator (cf. section 8 Iterators)
print(list(points.keys()))          # now a list is explicitly generated

points['B']
points['A'][0]
points['P'].x                       # nicer syntax using namedtuple

for k in points.keys(): print(points[k]) # point coords
for k in points: print(points[k])   # simpler
for v in points.values(): print(v)  # better


#%% Any *immutable* object can be used as a key e.g. int, string, tuple...
d[3.14] = 'pi'
d[(1,2,3)] = 'a tuple key!'
d['flag'] = ['red','green','blue']
print(d)
#d[[1]]=1                           #-> TypeError: unhashable type: 'list'

# Hashing is built-in for all Python immutable classes
hash(1)
hash('1')                           # string hash - function or method
'1'.__hash__()                      # (cf. section 5 Classes and OOP)
hash((1,2))
#hash([1,2])


# Every immutable class in Python comes with a built-in __hash__() function.
#
# Example - Hash function for strings / the str class (pseudo-code):
# arguments: string object; returns: hash
# function string_hash:
#    if hash cached: return it
#    set len to string's length
#    initialize var p pointing to 1st char of string object
#    set x to value pointed by p left shifted by 7 bits
#    while len >= 0:
#        set var x to (1000003 * x) xor value pointed by p
#        increment pointer p
#    set x to x xor length of string object
#    cache x as the hash so we don't need to calculate it again
#    return x as the hash
#
# Rehashing is performed via efficient randomized quadratic probing.


#%% The dictionary data structure is not immutable, but is now ordered [v3.7].

dd = dict([ ('z', 26), ('g', 7), ('k', 11) ])
print(dd)

# note that "order of insertion" is exactly that; if you want sorted, do:
print(sorted(dd.items()))
# (whereas sorted(dd) only returns the sorted dictionary keys)

# because of the order, we can have pop() and popitem() for instance:
dd.popitem()


# The new implementation stores in the hash tables indices to the elements
# stored in a separate entries table - as illustrated below.
#
# Old design:                 New design:
#   --- Hash table ----         - Hash table -   -- Entries table --
#   | key 2 | value 2 |         |      2     |   | key 0 | value 0 |
#   -------------------         --------------   -------------------
#   |       |         |         |            |   | key 1 | value 1 |
#   -------------------         --------------   -------------------
#   | key 0 | value 0 |         |      0     |   | key 2 | value 2 |
#   -------------------         --------------   -------------------
#   | key 1 | value 1 |         |      1     |   |       |         |
#   -------------------         --------------   -------------------


#%% Ordered dictionary, where items are stored in order of insertion
from collections import OrderedDict
od = OrderedDict([ ('z', 26), ('g', 7), ('k', 11) ])
print(od)

# Since the standard Python dictionary now behaves like an OrderedDict, there
# is no real need for the latter anymore... both are nearly the same. (It will
# remain in the collections module so as not to break existing code...)

# OrderedDict has some additional methods such as to reorder elements, e.g.:
od.move_to_end('z')
print(od)
# which can be emulated in a dictionary anyway, as
dd['z'] = dd.pop('z')


# Immutable dictionary: frozendict, available as third-party module  (not
# included in Python because the demand is low, according to the designers)

# Note that the concept of immutable vs. mutable classes and objects was made
# popular by the Java language, and is adopted heavily by Python. (C++ does
# not provide immutable versions of classes.)



################################
##
##  SETS
##


#%% Set class (mutable), unordered collection of unique items (all of which
#   must be hashable objects)

s1 = { 'France', 'United Kingdom', 'Italy', 'Germany' }
type(s1)

s2 = set([1,4,7,9,4,8,2,1,4,9,8,1,4,7,2,4,8,1,4]) # set created from a list
print(s2)                           # each item is now unique

# note: we can use set to remove duplicates! e.g. alist = list(set(alist))


for item in s1: print(item)         # sets are iterables too

s3, s4 = set('pecan'), set('pie')
s3 & s4                             # intersection -> {'p', 'e'}
s3.intersection(s4)                 # same
s3 | s4                             # union: {'i','n','c','a','e','p'}
s3 - s4                             # difference: {'c', 'a', 'n'}
s3 ^ s4                             # symmetric diff: {'i', 'n', 'c', 'a'}
s3 &= s4                            # intersection update: s3 is {'p','e'}
s3 <= s4                            # subset
s3.issubset(s4)
s3 |= s4                            # update -> s3 is {'i', 'p', 'e'}
s3.update(s4)

list({'one', 'two', 'three', 'four', 'five'}) # there is no order


#%% Frozen set, immutable version [FP]
s5 = frozenset(s4)
s4.add('x')
print(s4, 'vs', s5)                 # {'i', 'p', 'x', 'e'} vs frozenset...

#s5.add('x')                        # AttributeError: no attribute 'add'


# Sequence: a collection data type that supports the membership operator 'in',
# the size function 'len()', and is iterable e.g., list, tuple, dict, set...
# (Cf. Section 8 Iterators and Generators)



################################
##
##  OTHER COLLECTIONS
##


# collections module: Counter (bag), OrderedDict, defaultdict, UserDict,
# deque, ChainMap, Container, Hashable, Sized, Mapping, MutableMapping, ...
# Iterable, Iterator, Generator (cf. later sections)

# to see all: import collections ; dir(collections)
from collections import Counter

c = Counter('abcdeabcdabcaba')      # count elements from a string
c['a']                              # count of letter 'a'
c.most_common(3)                    # three most common elements
sorted(c)                           # list all elements (only once)
''.join(sorted(c.elements()))       # list elements with repetitions



################################
##
##  LISP/SCHEME EMULATION
##


#%% To get Lisp-style linked lists, one can emulate cons cells using tuples:
lisp_list = ("like",  ("this",  ("example", None) ) )

def car(lst): return lst[0]
def cdr(lst): return lst[1]
def cons(atm,lst): return (atm, lst)

car( cdr( lisp_list))               # lisp: (car (cdr lisp_list))
cons('just', lisp_list)             # lisp: (cons 'just' lisp_list)

# etc. Writing a Lisp interpreter in Python is left as an exercise. %^)

# Some idea to get started:
def lisp_eval(code):
    expr = code[1:-1].split(' ')
    return eval(expr[0] + '(' + expr[1] + ')')

lisp_eval('(car lisp_list)')        # works fine -> 'like'

#lisp_eval('(car (cdr lisp_list))') # needs recursive evaluation...


##
##  END
##
