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
##  05. Classes and Inheritance: attributes, functions, scope, inheritance,
##            reflection, abstract classes, multiple inheritance, interfaces
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
###   05. CLASSES AND INHERITANCE
###


"""
  Different programming languages define "object" in different ways. In some,
  it means that all objects must have attributes and methods; in others, it
  means that all objects are subclassable. In Python, the definition is looser;
  some objects have neither attributes nor methods, and not all objects are
  subclassable. But everything is an object in the sense that it can be
  assigned to a variable or passed as an argument to a function.

  This is so important that I'm going to repeat it in case you missed it the
  first few times: Everything in Python is an object. Strings are objects.
  Lists are objects. Functions are objects. Even modules are objects.

                                  -- Dive Into Python, Mark Pilgrim 2009
"""


################################
##
##  CLASSES AND ATTRIBUTES
##


#%% Class definition
class Stack(object):                # subclass of the 'object' class (default)
    """
    A well-known linear data structure that implements FIFO access
         . . .
    """                             # doc string

    verbose = False                 # (static) class variables
    counter = 0                     # number of stack instances

    # __new__() is the constructor. There is no need to override it unless one
    # is subclassing an immutable type (such as str, int, unicode, or tuple).
    # It is called first, creates a new instance, and calls the __init__()
    # function that is responsible for initializing the instance attributes.

    def __init__(self):             # initializer
        self.items = []             # instance variable (self = this)
        Stack.counter += 1          # accessing the class variable

    def __del__(self):              # Python has garbage collection...
        Stack.counter -= 1

    def push(self, x):
        self.items.append(x)        # accessing instance variable

    def pop(self):
        if not(self.isempty()):     # calling another function/method
            x = self.items[-1]
            del self.items[-1]
            return x
        else:
            print('cannot pop an empty stack')
            return None

    def isempty(self):
        return not self.items       # or (C style): len(self.items) == 0
                                    # or (still ugly): self.items == []
    def print(self):
        print(self.items)           # (see also __str__ function)

    def count():                    # class function (static method)
        return Stack.counter

    def Stack(self):                # (for demo only - not advisable)
        print("regular class function - NOT a constructor!")


#%% Creating instances, using class methods, etc.

s = Stack()                         # instance created: calls __new__()
print(vars(s))                      # then __init__()

s.push(2)                           # function (method) call  [OO]
s.push(4)
Stack.push(s,6)                     # same, as pure function call!
type(Stack.push)                    # note: compare to e.g., math.pow(2,5)

s.Stack()                           # careful: just another method call(!)

s.print()
s.items                             # no data hiding! see below for details
#s.items = 'gone is your data'      # (usual big warning applies...)

s.pop()
Stack.pop(s)

Stack.verbose                       # class variable
s.verbose                           # shared by all instances

Stack.count()                       # calling the class function
Stack.counter                       # accessing the class variable
s.counter                           # same, from the object (shared by all!)


#%% More examples, modifying classes and instances dynamically

s2 = Stack() ; s3 = Stack()
Stack.count()                       # 3 stack objects now
del s2
Stack.count()                       # 2 left
s3 = 'not a stack anymore'
Stack.count()                       # 1 only (garbage collection!)
s = Stack()                         # now 1 or 2?

# note: del() does not necessarily call __del__(); it simply decrements the
# object's reference count, and if this reaches zero __del__() is called.

# s.count()                         # error, same as Stack.count(s)
s.isempty()                         # implicit parameter
Stack.isempty(s)                    # same, explicit parameter
Stack.print(s)                      # same as s.print(), but
print(s)                            # Stack obj, need custom __str__ function


#%% Inspecting, modifying classes or instances (see also Reflection, later)
s.push(5)
s.push(7)
print(vars(s))
s.data = 'wow!'                     # new attribute created dynamically!
s.data                              # (better not do that?!? unless...)
'data' in dir(s)
del s.data

def lineprint(self):                # new class method added dynamically!
    for x in self.items: print(x)
Stack.lineprint = lineprint
s.lineprint()



################################
##
##  STRUCT / RECORD
##


#%% A class with no method can be used to mimic a C-style struct/record
#   (because a C++ struct is exactly like a class anyway). In Python we
#   can use a namedtuple instead (often a better design).

class Employee: pass                # class with no variable, no function

john = Employee()
john.name = 'John Doe'              # all attributes created dynamically!
john.dept = 'business'
john.salary = 1000                  # struct now has name, dept, and salary


class Student:
    def __init__(self, name='', major='n/a'):
        self.name, self.major = name,major

mary = Student('Mary Smith')
mary.major = 'CS'

print(john.name, 'is in', john.dept, 'and', mary.name, 'studies', mary.major)



################################
##
##  SCOPE (again)
##


#%% Python scoping rules apply everywhere the same, in functions, classes,
#   code blocks, and any combinations thereof...

v = 1                               # script scope variable (a.k.a "global")

class TScope(object):

    v = 2                           # class variable / class attribute

    def __init__(self):
        self.v = 3                  # member variable / object attribute

    def scopes(self):
        v = 4                       # local variable (of function/method)

        print("  global v:",  globals()['v'])
        print("    locals:",   locals()['v']) # locals: {'self': ..., 'v': 4}
        print("vars(self):", vars(self)['v']) # vars: {'v': 3}

        print("   class v:", TScope.v) # or just v, if no local var
        print("  member v:",   self.v)
        print("   local v:",        v)

TScope().scopes()

print(TScope.v)                     # -> 2 (class variable)
print(TScope().v)                   # -> 3 (attribute of new object)



################################
##
##  NESTED CLASSES
##


#%% In Python anything can be nested within anything. Functions in the main
#   are regular functions while functions nested within a class are methods.
# Classes can be nested with classes or functions... basically they should
# be defined wherever appropriate, regardless of other considerations.

class Outer(object):
    outvar = 1
    class Inner:
        def printOuterVar():
            print(Outer.outvar)     # Outer class name needed (for scope!)

Outer.Inner.printOuterVar()         # shows the nested attribute

#  . . .    print(outvar)   would cause a NameError: 'outvar' not defined

# note: Unlike in Java, in Python (also C++ and C#) there is no implicit
# binding between the nested/inner class and the enclosing/outer class.
# -> required is: print(Outer.outvar)

print(Outer.outvar)                 # works, of course ("public" class var)


# Classic example of a linked list with a nested node class
class doubly_linked_list(object):
    class Node:
        def __init__(self, data=None, prev=None, next=None):
            self.data, self.prev, self.next = data, prev, next

    def __init__(self):
        self.head, self.tail = List.Node(), List.Node()
        self.head.next = self.tail
        self.tail.prev = self.head

List = doubly_linked_list           # (let's use a better name -> alias)

List().head.next == List().tail     # "public" access! (well, not really)

List.Node(data=1,next=List.Node(2)).next.data # nested class is "public"!


# Example of a class nested within a function
def makeRecord():
    class record:
        def __init__(self,data=None): self.data = data
    return record

rec = makeRecord()                  # class created dynamically (closure again)
r = rec('some data')                # new instance with ad hoc data
r.data



################################
##
##  ATTRIBUTE ACCESS
##


#%% Attributes and methods starting with an underscore are treated as
#   non-public ("protected"). Names starting with a double underscore are
# considered strictly private (Python mangles class name with method name
# in this case: obj.__var has actually the name _classname__var)

class PPPClass(object):
    def __init__(self):
        self.a   = 1                # "public" variable
        self._b  = 2                # non-"public" variable
        self.__c = 3                # "private" variable

    def __print(self):              # "private" method
        print(self.a, self._b, self.__c)

    def print(self):                # "public" method (calling the above)
        self.__print()

    lpr = lambda self: self.__print()   # same as above

p = PPPClass()
p.a                                 # only visible attribute (cf. thumbnail)
p._b                                # accessible but not visible
# p.__c                             # error - not accessible
# p.__print()                       # (since the name has been mangled)
p.print() ; p.lpr()

dir(p)                              # reveal all "hidden" attributes i.e.
vars(p)                             # variables and methods

p._PPPClass__c                      # now we can access the "private" variable
p._PPPClass__print()                # and call the "private" method (!)

for a in vars(p):                   # inspect attributes programmatically
    if '__' in a: print(a, ':', getattr(p,a))

setattr(p,'a',666)                  # change attribute programmatically
setattr(p,'lpr', lambda: print('hacked!'))
p.lpr()


# Note: Python is designed to be simple, interpreted, and then scripts are
# distributed as source 99.1% of the time. So, if users have the source code,
# they can see everything and change anything they like! Hence there is no
# point declaring something "private", when users can make it "public"!
#
# Therefore Python has encapsulation/classes and polymorphism/inheritance but
# no data hiding. Also it allows function overriding, but not overloading.
# (Note that implementing access control - private vs. public vs. protected -
# implies a lot of complexity as well as performance overhead at runtime...)



################################
##
##  REFLECTION
##


#%% About the special attributes again

s.__dict__                          # class-defined attributes

s.__class__.__name__                # name of class
s.__class__.__doc__                 # documentation string
s.push.__name__                     # likewise, name of method

dir(s)                              # get names of all attributes and methods
                                    # incl. __init__(), __hash__(), __eq__()
s.__dir__()                         # ... __class__, __doc__, ...

if 'count' in dir(Stack):           # check if a method exists (by name)
    print(Stack.count())


#%% Special/magic methods:
#
# __new__([args])               constructor (but see previous notes)
# __init__(self [, args])       initializer, called after the constructor
# __del__(self)                 destructor (optional)   del(self)
#
# __hash__(self)                hashing function:       hash(self)
# __len__(self)                 length/size of:         len(self)
# __str__(self)                 string representation:  str(self)
# __repr__(self)                object representation:  repr(self)
# __format__(self, format_spec) formatted string repr:  format(...)
#
# __dir__(self)                 attribute lister:       dir(self)
# __call__(self [,args])        makes it callable:      self(...)
# __hasattr__(self, name)       attribute checker
# __getattr__(self, name)       attribute getter:       getattr(self, name)
# __setattr__(self, name, val)  attribute setter:  setattr(self, name, val)
# etc.

class Class2Print(object):
    __begin, __end = '<< ', ' >>'

    def __init__(self,data):
        self.__data = data

    def __str__(self):
        return self.__begin + str(self.__data) + self.__end
        # or   repr(self.__begin + str(self.__data) + self.__end)

Class2Print(12345)                  # a Class2Print object
Class2Print(12345).__str__()
print(Class2Print(12345))           # print info string from __str__()


#%% More special/magic methods, for standard operators (NOT "overloading"!
# this is more like Java interface - cf. "duck typing"...)
#
# __add__(self, other)          addition operator:      self + other
# __iadd__(self, other)         additive assignment op: self += other
# __mul__(self, other)          multiplication op:      self * other
# ...
# __truediv__(self, other)      division operator:      self / other
# __pow__(self, other)          power operator:         self ** other
#
# __contains__(self, item)      in operator:            item in self
# __getitem__(self, key)        RHS bracket operator:   self[key]
# __setitem__(self, key, item)  LHS bracket operator:   self[key] = item
#
# __eq__(self, other)           comparison operator:    self == other
# __ne__(self, other)           difference operator:    self != other
# __lt__(self, other)           less than operator:     self < other
# ...
# Good overview @ https://rszalski.github.io/magicmethods/


# note: repr vs. str - both functions return a string for printing, but:
str(123)                            # string '123'
repr(123)                           # same - but now:
str('Python')                       # -> 'Python'
repr('Python')                      # vs. "'Python'"

# The __str__ function (str) converts an object into a human-readable form
# i.e. what you, as a user, might wish to see when you print an object out.
# The __repr__ function (also repr) converts an object into a string which
# you, as a programmer, might wish to have to recreate the object e.g.
# using the eval() function.

eval(repr('Python'))
#eval(str('Python'))                # NameError: 'Python' not defined
import datetime
now = datetime.datetime.now()       # now compare:
str(now)                            # -> '2018-03-01 15:52:15.760365'
repr(now)                           # -> code to create the above!
# -> 'datetime.datetime(2018, 3, 1, 15, 52, 15, 760365)'
print(eval(repr(now)))

# note: Python 2 had the backquote (like Lisp/Scheme!) as a shortcut for
# repr i.e. you could write print(" answer = `f()` ") where f() would be
# evaluated, so the output might be e.g. answer = 42
#
# In Python 3 you can do the same with: print(" answer = " + repr(f()))
# In v3.6 onward you can use formatted strings: print(f'answer = {f()}')
# so basically curly brackets have replaced the Lisp-like backquotes...

# note also that the print() function uses __str__, if defined, and __repr__
# otherwise. The interpreter uses __repr__ only.



################################
##
##  OBJECT-ORIENTED PROGRAMMING
##


#%% Methods vs. functions, classes vs. modules ...

import math                         # math.py module
math.pi                             # constant
math.gcd(15,40)                     # function

class math(object):                 # math class (oops, no more module...)
    pi = 3.1415                     # constant
    def gcd(a, b):                  # function
        while a != 0: a, b = b%a, a
        return b
math.pi                             # class or module? same syntax!
math.gcd(15,40)                     # (it's all about scope, nothing else)


# list class
l = [1,2,3,4]
l.append(5)                         # OO style, equivalent to
list.append(l,5)                    # a function call


#%% Really it is all references/objects nested within one another... Example:

import collections                  # collections.py module
q = collections.deque()             # deque class

q.clear()                           # OO style, equivalent to
collections.deque.clear(q)          # a function call

collections                         # module    |
collections.deque                   # class     |  4 levels of encapsulation
collections.deque.clear             # function  |  (all are refs to objects)
collections.deque.clear.__name__    # object    V


class collections:                  # nested class scopes
    class deque:
        class clear:
            pass

collections.deque.clear.__name__    # same syntax, different refs/objects

# __code__ + see above OO vs. FP style ...



################################
##
##  CLASS INHERITANCE
##


#%% Defining a subclass
class PeekStack(Stack):
    "A stack where one can peek at inferior items"

    # no __init__() function since no member variables are added

    def peek(self, n):
        "peek(0) returns top, peek(1) returns item below that; etc."
        if 0 <= n < len(self.items):
            return self.items[len(self.items)-1-n]

    def count(): return 'n/a'       # overriding the inherited function
    count2 = lambda: 'nothing'      # same, using lambda expression syntax

y = PeekStack()                     # calls the inherited constructor
y.push('a')
y.push('b')                         # inherited push function/method
y.push('c')
y.peek(1)                           # subclass function/method
y.print()
PeekStack.count()


#%% Checking the class hierarchy
isinstance(y,PeekStack)
isinstance(y,Stack)                 # both True

issubclass(PeekStack, Stack)
issubclass(bool, int)               # both True
issubclass(float, complex)          # False

# Special attributes again
bool.__bases__                      # parent class/es (in a tuple)
'xyz'.__class__.__bases__

bool.__mro__                        # classes considered when looking for base
PeekStack.__mro__                   # classes during method resolution

int.__subclasses__()                # list of subclasses

x = PeekStack()
if x.__class__ is y.__class__: print('same class')

if x.__class__.__name__ is y.__class__.__name__: print('same class')


#%% Subclassing / inheritance
class LimitedStack(PeekStack):
    "A stack with limit on stack size"

    def __init__(self, limit=100):
        super().__init__()          # call the base class initializer
                                    # alt: PeekStack.__init__(self)
        self.limit = limit          # add a new member variable

    def push(self, x):
        if len(self.items) < self.limit:
            super().push(x)         # call the base class method
        else:
            print("stop pushing!")

    def __len__(self):              # for len()
        return len(self.items)

    def __str__(self):              # for print() or other similar functions
        return str(self.items)      # or: f'{self.items}'

    def __eq__(self,other):         # call base __eq__ first
        return super().__eq__(other) and self.limit == other.limit

z = LimitedStack(3)
z.push(1)
z.push(2)
z.push(3)
z.items
z.push(4)
len(z)
z.items
print(z)


# note: super is actually a class! Its constructor returns a proxy object
# that allows delegating method calls to a parent or sibling class of type.
# This is useful for accessing inherited methods that have been overridden
# in a class. (Now this is one of these really weird Python things... ;)
#
# Use Case 1: super can be called upon in a single inheritance, in order to
# refer to the parent class (or multiple classes) without explicitly naming
# them. It's like a shortcut. (This is the case illustrated above.)
# Importantly, it helps to keep your code maintainable (no explicit name).
#
# Use Case 2: Super can be called upon in a dynamic execution environment
# for multiple or collaborative inheritance. This use is considered exclusive
# to Python, because it is not possible with languages that only support
# single inheritance or are statically compiled (like C++/Java).



################################
##
##  MULTIPLE INHERITANCE
##


#%% Multiple inheritance is available in Python (of course).
#   The 'diamond problem' is solved via an order of precedence (LTR).

class XFather(object):
    def __init__(self):
        print("father side")
    def test(self):
        print("daddy says hi")      #     object
                                    #    /      \
class XMother(object):              #  XFather  XMother
    def __init__(self):             #    \      /
        print("mother side")        #     XChild
    def test(self):
        print("mommy says hi")
    def test3(self):
        print("mommy only")

XMother().test()


class XChild(XFather, XMother):     # order is essential, defines inheritance
    def __init__(self):
        super().__init__()          # super() same as super(XChild, self)
        print("child here")
    def test2(self):
        super().test()
        print("kiddy waves hello")
    def test3(self):
        super().test3()
        print("kiddy again")

c = XChild()
c.test()
c.test2()
c.test3()

print(XChild.__bases__)             # parent classes (in a tuple)
print(XChild.__mro__)               # classes considered for method resolution



################################
##
##  ABSTRACT CLASSES
##


#%% Python on its own does not provide abstract classes! It is the abc module
#   that provides the infrastructure for defining Abstract Base Classes (ABCs).

from abc import ABC, abstractmethod
#import abc

class Shape(ABC):                   # extends the abstract base class

    def __init__(self):
        self.__name = ''
        print("new shape built")

    def set_name(self,name):        # concrete method: inherit or replace
        self.__name = name

    def name(self):
        return self.__name

    @abstractmethod                 # decorator - extends the function!
    def draw(self):                 # denotes an abstract method: must be
        return                      # implemented in concrete subclasses


# note: Decorators are like functions (defined elsewhere) that modify the
# behavior of the "decorated" function (cf. example in section 4).
#
# This is very different from e.g., @override in Java, which is nothing but
# a keyword instructing the compiler to perform some extra checking. (Note
# that the Decorator Pattern has become one of the classic OO Patterns...)

class Cube(Shape):                  # concrete subclass

    def __init__(self):
        super().__init__()
        print("and it's a cube")

    def draw(self):
        print("See me? I'm a", self.__class__.__name__)

class Unknown(Shape):               # abstract subclass
    "fails to implement the abstract draw method"

# sh = Shape()                      # cannot instantiate abstract class
cu = Cube()
cu.draw()
# un = Unknown()                    # cannot instantiate abstract subclass



################################
##
##  INTERFACES IN PYTHON
##


#%% Interfaces are all implicit in Python i.e., there is no explicit interface
# syntax (as in Java). For a Python class to implement an interface means to
# define one or more required functions - that's it!
#
# For any object to be 'printable' in Python i.e., so that print() will work
# with it, its class only needs to implement the __str__() function (and make
# it return a string object comprising the desired attributes). Almost every
# built-in Python class is printable.
#
# For any object to be 'comparable' its class must implement __eq__() so that
# x == y will work as expected (also __ne__() for difference, x != y).
#
# To make any object 'countable', its class needs to implement the __len__()
# function (and make it return an integer). Many Python classes are countable
# e.g., all containers / sequences (list, dict... str...)
#
# To be a container / sequence, a class must implement __contains__() so it
# will work with membership functions e.g., if x in X: ...
# Then, to support slicing, a sequence must implement __getitem__().
#
# For any object to be an 'iterable', its class must implement the __iter__()
# function (to return an iterator, which can be done simply using iter() for
# example). Python classes such as range, zip, and enumerate are iterables, so
# are all containers / sequences...
#
# Likewise an iterator is a class that implements a __next__() function...
# (Cf. section 8 Iterators and Generators).
#
# For a class to be 'hashable' i.e., so it will work with maps and hash tables
# et al, it must implement the __hash__() function. Almost every Python class
# is hashable (if it makes sense).
#
# To make any object 'callable', like a function, its class needs to implement
# the __call__() function (the body of which is executed when a call is made).
#
# To implement an interface in Python means to fully and properly implement
# the desired functions and behaviour: it is the programmer's responsibility
# to do so (Python will not check). If coded correctly, then it "just works".
#
# This design paradigm is known as Python "duck typing": if your code "looks
# like a duck and quacks like a duck, it's a duck!". (In AI we also calls
# this de-duck-tive reasoning ;-)
#
# Note that, in addition to the above examples, Python uses interfaces for:
# Classifier, Clustering, Converter, Distribution, Evaluation, Regression,
# Serialization, and many more.
# (See also: Python design by Contract @ http://pythondbc.codeplex.com/)



##
##  END
##
