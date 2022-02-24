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
##  04. Functions and Lambda Expressions: function objects, doc, attributes,
##                      scope, default args and keywords, lambda expressions
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
###   04. FUNCTIONS AND LAMBDA EXPRESSIONS
###



################################
##
##  FUNCTIONS
##


#%% Defining a function, signature and body

def welcome():
    print('Welcome to Python!')     # return statement is optional

# Functions are objects! (data in Python)
welcome                             # reference / variable: function welcome
type( welcome )                     # object of 'function' class

welcome()                           # calling the function (w/ parentheses)

#welcome = 3                        # careful again - function ref is gone!
#welcome()                          # TypeError: 'int' is not callable

def vwelcome(version):              # type inference for args too!
    print('Welcome to Python', version)
    print(type(version))            # function body/block is indented
    return version

vwelcome(3)                         # returns an int
print(welcome())                    # returns 'None' (no value)


#%% Documenting a function

def gcd(a, b):
    "greatest common divisor"       # doc string (also used in thumbnail)
    while a != 0:
        a, b = b%a, a               # parallel assignments (via a tuple)
    return b

gcd(12,20)

# Fibonacci numbers again, with full doc string (first line for thumbnail)
def fibonacci(n):
    """Prints all Fibonacci numbers up to n.

Some lengthy story about as Leonardo Fibonacci of Pisa, who popularized the
use of Arabic numerals in Europe in the 13th century, and made many original
contributions to algebra, geometry, number theory, etc. and also how he went
about counting rabbits and thus discovered the so-called Fibonacci series...
"""
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a+b               # parallel assignment (via a tuple)

help(fibonacci)


#%% Function returning multiple values

def sqpair(x):
    return x, x**2                  # actually... returns a tuple!

value, square = sqpair(4)           # unpacking values from returned tuple

quo, rem = divmod(22, 3)            # function returning 2 values (unpacked)
print(quo, 'and', rem)
divresult = divmod(22, 3)           # same, as tuple (no unpacking)


from statistics import mean, stdev, quantiles

def show_stats(data): return mean(data), stdev(data), quantiles(data, n=4)
m,s,q = show_stats([1.0, 2.5, 3.25, 5.75])

# Also, case of a MinMax function that returns both min and max values from a
# sequence, thus requiring 1 traversal only (vs. 1 for min + 1 for max), etc.


#%% Is Python call-by-value or is it call-by-reference (C++ style)?
#   Neither! The best way to describe it is "call-by-object-reference"
# (somewhat a bit like Java itself...) To spell it out with an example:

def plural(noun): return noun+'s'   # noun is a local var/ref. to arg object
pet = 'cat'                         # pet is a ref. to string object ("cat")
plural(pet)                         # noun is pet, they refer to same object

# note: Everything so far has global scope. 'pet' and 'plural' are references
# to string and function objects, resp. - defined at the top level. However,
# 'noun' is defined in the function block hence its scope is limited to it;
# it is a local reference to the same string object as pet (in this case).


# Remember, Python is an interpreted language and everything is evaluated
# dynamically at runtime! The same applies to e.g., function definition:
if pet:
    def dg(n): print(n+2)
else:
    def dg(n): print(n*2)
dg(5)

if pet:
    dg = lambda n: print(n+2)       # equivalent def using lambda expression
else:                               # -> a binding to an anonymous function
    dg = lambda n: print(n*2)       # (see further below)


#%% Nested functions, good for helper functions, also to protect functions
#  from changes, since their scope is only that of the enclosing function.
def iseven(x):
    return x % 2 == 0

def nse(n):
    c = '*'
    def sprint(s):                  # defining function as 'data' - their
        print(c, s, c)              # scope is that of the enclosing block
    sprint( iseven(n))              # calling two local functions
nse(7)
#sprint(7)                          # -> NameError: name 'sprint' not defined
                                    #   (because its scope is the function)

# Nested (accumulator recursive) helper function
def fact(n):
    nval = int(n)
    if nval != n: raise ValueError('argument must make sense as an int')
    if nval < 0: raise ValueError('negative numbers not allowed')
    def fact(n, f=1):
        if n == 0: return f
        else: return fact(n-1, n*f)
    return fact(nval)               # calling local fact function

print(fact(123))



################################
##
##  FUNCTION ATTRIBUTES
##


#%% Specific object attributes follow the "double underscore" syntax e.g.
gcd.__name__
f = gcd                             # alias (another reference)
f(12,20)
f.__name__                          # -> 'gcd'

__name__                            # -> '__main__' (interpreter top level)

# Object attributes can also be retrieved programmatically, using reflection
# (more below). This is similar to, but better and more powerful than, Java
# (cf. also sections 7 Higher-Order Functions and 10 Meta-programming).
getattr(f, '__name__')


# Documentation string attribute, implementation
gcd.__doc__
str.__doc__                         # use print for proper formatting


#%% Purposes of the documentation string:
#   (1) source code information + online documentation via help()
#   (2) generated documentation via e.g., HappyDoc (like Javadoc)
#   (3) ballon help in the shell (e.g., in IDLE, also other IDE's)
#   (4) automated code testing! (cf. section 10 Meta-programming)

def myf(x):
    """my "mystery" function of x (!)

    This is a long description bla bla bla ...
    """
    pass                            # place holder (means: to be coded later)

print(myf.__doc__)                  # same as help(myf)

myf.__doc__ = 'to be written later' # can be changed programmatically

def gcd(a, b):
    "greatest common divisor"
    while a != 0: a, b = b%a, a
    return b

gcd.__code__                        # code of the function! (reflection)

dir(gcd.__code__)                   # inspecting the code symbols
gcd.__code__.co_argcount            # -> 2 arguments to the function
gcd.__code__.co_varnames            # -> ('a', 'b')
gcd.__code__.co_consts              # -> ('greatest common divisor', 0)
for a in dir(gcd.__code__):
    print(a, ':', getattr(gcd.__code__,a))


#%% Any class can be made callable by defining a __call__() method! The
#   instances of the class can then be called like any function.

type(gcd)
gcd.__call__                        # function has __call__()
gcd.__call__(10,35)                 # same as gcd(10,35)

class Callable:
    def __call__(self): print('Did you call me?') # (cf. Class section...)

fun = Callable()
fun()                               # or in one step: Callable()()


#%% Introspection! (cf. also Iterators section and the Dispatcher example)
getattr(1+3j, 'imag')
getattr(gcd, '__doc__')             # retrieve any attribute of an object

mlist = list(range(12))
mname = 'pop'                       # retrieve the function code given an
mpop = getattr(mlist, mname)        # instance of the class (list object)
print(mpop)                         # then calling the function on it
mpop()                              # (can use dir() to find names...)
print(mlist)

def autopop(lst): return getattr(lst, 'pop')()
autopop(mlist)
print(mlist)

def autoexec(obj, fun):             # general, safe version of the above
    if fun not in dir(obj): print('no', fun, 'in', obj.__class__)
    else: return getattr(obj,fun)()

autoexec(mlist,'pop')
autoexec(mlist,'poppy')



################################
##
##  FUNCTION SCOPE
##


#%% Python's scoping rule is a straight search from the inner to the outer
#   scope, and again, and again... Eventually it reaches script level i.e.
#   global scope. An exception is raised if no matching symbol is found.

code = 111                          # script-level variable (a.k.a. "global")

def gff():
    locv = 88
    print('code=', code)            # global variable, found in outer scope
    print('locv=', locv)            # local variable, within function scope

def f1():                           # nested function scope example
    code = 1                        # (similar to nested block scope)
    print('f1: code =', code)
    def f2():
        code = 2
        print('f2: code =', code)
        def f3():
            code = 3                # comment this line, then same in f2, f1
            print('f3: code =', code)
            return code             # scope: f3 -> f2 -> f1 -> script/global
        return f3()
    return f2()


#%% Functions locals() and globals() return a dictionary of variable names
#   and values, defined within the scope where the function is called and at
#   the script level (main), respectively.

globals() is locals()               # same at the script/module level
print(globals().keys())             # show all objects/refs defined so far
print(globals()['code'])

def pgl(n):
    s, v = 'one', (2,3)
    print(locals())
    return globals() == locals()    # local scope is not global scope
pgl(1)

def gfg():
    lovc = 88
    code = 421                      # local var, hides the global var
    print('code=', code)
    print('local variables:', locals())
    print('global code var:', globals()['code'])

def ggf():
    lcode = 2 * code                # accessing var in outer scope is fine
    print(lcode)

def ggg():
    global code                     # needed: which 'code' var(?) - else
    code *= 2                       # UnboundLocalError: ref before assignment
    print(code)

def ghg():
    code = 222
    def ghgx():
        nonlocal code 	            # nonlocal needed to refer to a
        code += 1		   	        # previously bound variable in the
        print(code)	                # nearest outer scope (excl. globals)
    ghgx()

def ghh():
    code = 222
    def ghhx():
        global code 	            # global refers to script-level,
        code += 1		            # regardless of how many scope levels
        print(code)	                # are nested within one another
    ghhx()



################################
##
##  PYTHON CLOSURES
##


#%% A closure is a runtime environment whereby some data from the outer scope
#   is remembered even if it went out of scope or if the function itself was
# removed from the current namespace. The combination of the code and the
# data attached to it (as needed) is called a closure. Example:

def mpr(s):
    def p(): print(s)            # nested function p can access the nonlocal
    p()                          # variable s of the enclosing function
mpr('works fine')

def mprf(s):                     # now returns a nested function p that uses
    def p(): print(s)            # variable s -- after function mprf returned
    return p                     # variable s should go out of scope(?) but

rf = mprf('still works!')        # the created function rf can still access
rf()                             # the data in the former variable s

del mprf ; rf()                  # still works, even though mprf was removed


# Function objects also have a __closure__ attribute that returns a tuple of
# cell objects if it is a closure function (i.e., part of a closure).
# e.g.
rf.__closure__
# Cell objects have an attribute which stores the closure value, e.g.:
rf.__closure__[0].cell_contents  #-> above string, 'still works!'


# When is a closure created in Python? When the following criteria are met:
#   (1) We  have a nested function (a function defined inside a function);
#   (2) The nested function refers to data defined in the enclosing function;
#   (3) The enclosing function returns the nested function.
#
# Note that it makes no difference whether the nested function is defined
# using a def statement or using a lambda expression.

# Why are closures useful? They allow avoiding the use of globals (!) and
# provide some form of data hiding. They can also provide a more elegant
# alternative to implementing a class i.e., when the class has few methods
# (one method, in many cases). When the number of attributes and methods
# is larger, it is usually better to implement a class.



################################
##
##  DEFAULT/KEYWORD ARGUMENTS
##


#%% Default / keyword arguments
def dwelcome(version=3):
    print('Welcome to Python', version)
    return version

dwelcome()                          # use the default
dwelcome(4)                         # override the default
dwelcome(version=5)                 # same, naming the arg explicitly

def daf(x, y=3, s='default'): print(x, y, s)

daf(4)
daf(4, 5)
daf(4, 5, 'hello')                  # override defaults, in order
daf(8, s='ok')                      # "skipping over" the second argument
daf(8, s='ok', y=777)               # using keywords allows to change the order

# Function attribute allows programmatically inspecting default arguments
dwelcome.__defaults__

def tell_defaults(fun):
    print(f'{fun.__name__} has {len(fun.__defaults__)} default arg' +
          's'*(len(fun.__defaults__)-1))
tell_defaults(dwelcome)
tell_defaults(daf)


#%% Positional-only arguments, using a / character at the end [v3.8]
def pwelcome(version=3, /):
    return version
pwelcome()
#pwelcome(version=5)                # TypeError: ... keyword argument given

def xwelcome(name, /, greeting='hello'):
    print(f'{greeting}, {name}')

xwelcome('bob')
xwelcome('bob', greeting="'morning")
#xwelcome(name='bob', greeting="'morning")


# Keyword-only arguments, using a * character at the beginning [v3.8]
def zwelcome(*, name, greeting='hello'):
    print(f'{greeting}, {name}')

zwelcome(name='bob', greeting='cheers')
#zwelcome('bob', greeting='cheers')# TypeError: ... positional argument given


# One can combine positional-only, regular, and keyword-only arguments, by
# specifying them in this order, separated by the / and * characters, e.g.
def hwelcome(name, /, border='=', *, width=50):
    print(f" {name} ".center(width, border))

hwelcome('good morning')
hwelcome('good morning', '_')
#hwelcome(name='good morning', '_')
hwelcome('good morning', border='_')
#hwelcome('good morning', border='_',50)
hwelcome('good morning', border='_',width=50)


#%% Variadic functions i.e., with variable number of arguments - in Python
# they can be collected into a tuple using the * prefix.
# (compare with variadic args in C++/Java using ... with va_list/array)

def starprint(*args):
    for item in args: print('*** ',item)

def concatz(separator, args):       # requires a list of args (inconvenient)
    return separator.join(args)

concatz('/', ['red','green','blue'])

def concatx(separator, *args):      # allows variable number of args
    return separator.join(args)

concatx('/','red','green','blue')   # first arg is the separator

# implementation note: f(*args) replaces apply(f,args) in Python 3


# Extending variadic arguments to keyword parameters (kwargs) allows passing
# any key-value pair in any order (similar to default function parameters).
# They are naturally colleced into a dictionary.

def dbd(**kwargs):
    for key,val in kwargs.items():
        print(key,':',val)

dbd(first_name='John', last_name='Doe')


#%% More examples
def concat(*args, separator='/'):   # all args absorbed by *args thus
    return separator.join(args)     # separator keyword is necessary

concat('red','green','blue','.')    # incorrect usage
concat('red','green','blue', separator='.') # correct

def add(m,n): return m+n
add(2,3)
args = [2,3]
#add(args)                          # TypeError: missing positional arg 'n'
add(*args)

# add any number of values (recursive function!)
def addf(*args):
    return args[0] + addf(*args[1:]) if args else 0
addf(1,2,3,4)


#%% Setting the default value - remember about code evaluation in Python...

da = 5
def dff(arg=da):                    # default set the first time
    print(arg)

dff()
dff(8)
da = 10                             # default not changed - unless the above
dff()                               # def statement is evaluated again!

# note: It is often expected that a function call creates new objects for
# default values. This is not the case. Default values are created exactly
# once, when the function is defined.

def atl(itm, lst=[]):
    lst.append(itm)                 # default value updated/shared
    return lst

print(atl(1)) ; print(atl(2)) ; print(atl(3))

def atll(itm, lst=None):
    if lst is None:
        lst = []
    lst.append(itm)                 # default value not shared
    return lst



################################
##
##  LAMBDA EXPRESSIONS
##


#%% Lambda expressions are anonymous functions i.e., function objects that are
#   not bound to any identifier (reference). λ-expressions come from Lambda
# Calculus, which is the formal logic used in CS to express computation.
#
# λ-expressions are fully supported in Functional Programming languages, and
# partially (yet increasingly) supported in more popular languages such as
# Python 3, Java 8, C++11, C#, JavaScript, etc.
#
# Syntax differences (in Python) include: no parentheses around arguments,
# implicit return statement, alternate if/else syntax...
# The biggest limitation is that λ-expressions in non-FP languages are pretty
# much limited to single line body. (In Functional Programming, there is *no*
# difference between a function and a λ-expression.)

def odd(n): return n % 2 != 0       # using standard function 'def' syntax
type(odd)
odd (5)
oddfun = odd                        # another reference to the same function
oddfun(7)

oddl = lambda n: n % 2 != 0         # same using an anonymous λ-expression
type(oddl)                          # now bound to an identifier (a name)
oddl(5)

# note: since functions are just objects, it makes sense that we can use
# anonymous functions just like we can use anonymous objects (without ref.)

'anonymous str object' [5]          # string object, without any reference

(lambda n: n % 2 != 0) (5)          # function object, without any reference

if pet:
    dg = lambda n: print(n+2)       # prev. example again, with λ-expressions
else:
    dg = lambda n: print(n*2)

# See further below for actual usage examples of lambda expressions, either
# as argument to another function, or returned value from a function.


# note: Functions and lambda expressions are examples of subroutines, where
# all code is executed sequentially / synchronously. Coroutines on the other
# hand are subroutines where code is executed concurrently / asynchronously.
# (See section 13. Threads and Concurrency.)



################################
##
##  FUNCTION OVERLOADING (NOT!)
##

#%% Python has *no* function overloading! Instead it has dynamic reference
#   binding. It follows that every function has a single definition, which
# can be replaced dynamically any time. Default values must used instead to
# provide different versions of a function...

def fol(n): print(n+1)
fol(3)

def fol(n): print(n*5)              # dynamically (re)defines the function
def fol(n,p): print(n*p)            # same, not overloading!

fol(3,4)                            # 12 - as expected
#fol(3)                             # TypeError: missing 1 required arg: 'p'

def fol(n,p=5): print(n*p)
fol(3)                              # 15, since only the second version exists

# The above becomes obvious if using lambda expression syntax: in all cases
# we are just binding the name fol to a function object, e.g.
fol = lambda n: print(n+1)
# etc. Hence each 'def' statement is merely reassigning the reference (name)
# to another λ-expression or function object -- not overloading!

# note that C++ has both overloading and default values, Java has overloading
# but no default values, and Python has default values but no overloading.



################################
##
##  FIRST-CLASS FUNCTIONS
##


#%% In Python, functions and lambda expressions are "first-class entities"
#   just like any other object, and can be passed as function arguments, also
# returned as the value of function calls, stored in variables, lists, etc.

sorted([('john', 'A', 15),('mary', 'C', 12), ('dana', 'B', 10)]) # default
sorted([('john', 'A', 15),('mary', 'C', 12), ('dana', 'B', 10)],
       key=lambda student: student[2])

#sorted([7+2j, 5-10j, 3+4j])        # TypeError: '<' not supported in complex
sorted([7+2j, 5-10j, 3+4j], key=lambda c: c.real)
sorted([7+2j, 5-10j, 3+4j], key=lambda c: c.real**2+c.imag**2) # abs! (square)
sorted([7+2j, 5-10j, 3+4j], key=complex.__abs__) # built-in abs function


def testingf(f, x):                 # function/lambda passed as argument
    print(f, 'applied to', x, 'is', f(x) ) # call f on x !
    if f(x): print('ok')

testingf(odd, 5)                    # <function odd ...> applied to 5
testingf(lambda x: x % 2 != 0, 5)   # <function <lambda> ...>

def execf(command = lambda: None, *args):  # apply given command to args
    return command(*args)           # (cf. Higher-Order Functions section)

execf()                             # default call does nothing
execf(lambda: print('Hi there!'))   # lambda expression with no arg
execf(odd, 5)                       # odd function, defined earlier
execf(lambda x: x%2 != 0, 8)        # lambda with 1 arg (odd)
execf(lambda x,y: x==y, 2,3)        # lambda with 2 args (equal)
execf(sum, [1,2,3,4])               # sum function with list arg


#%% More examples
from math import pi, cos, sin, tan	# apply multiple functions from a list
for f in [cos, sin, tan]: print( f(pi/3) )

# Example of a custom comparator, function passed as argument
def compare(x,y, cmp=(lambda x,y: x==y)): return cmp(x,y)

l1=[1,2,3] ; l2=l1[:]
compare(l1,l2)                      # -> True, using default ==
compare(l1,l2, lambda x,y: x is y)  # -> False
compare(l1,l2, compare)

# note: Normally we create functions that do not already exist - but in this
# case the two lambda expressions are equivalent to '==' and 'is' operators.
# Same as:
import operator                     # standard operators as functions
compare(l1,l2, operator.eq)         # -> True
compare(l1,l2, operator.is_)        # -> False

execf(operator.mul, 3,7)            # because we cannot do: execf(*, 3,7)


# Minimal GUI button demo (cf. Graphics and GUI Extensions for more examples)
# A button click causes the command i.e., given function or lambda expression,
# to be called and its code to be executed. Note the concise, obvious syntax!
# (This shows exactly why Java 8 adopted lambda expressions...)
import tkinter
class tkdemo(tkinter.Frame):
    def __init__(self):
        root = tkinter.Tk()
        tkinter.Frame.__init__(self,root)               # app window, has
        tkinter.Button(root,                            # one button only,
                       text = ' Click me ',             # with a label and
                       command = lambda: print('Hello') # a function command!
                       ).pack()
        root.lift()
#tkdemo().mainloop()


# %%Imperative style vs. functional programming syntax for conditionals
def hilo(n):
    if n > 1000: return n/100       # imperative function style
    else: return n

hilo(12345)

def hilof(n):
    return n/100 if n > 1000 else n # functional programming style
                                    # (using lambda expression syntax)

(lambda n: n/100 if n > 1000 else n)(12345) # same style (cf. Comprehensions)

(lambda n: n > 1000 and n/100 or n) (123)   # logically equivalent alternative


def fact(n):                        # imperative function style
    if n == 1: return 1
    else: return n * fact(n-1)

def fact(n):                        # functional programming [FP] style
    return 1 if n == 1 else n * fact(n-1)


# Can we do the above using a lambda expression? recursion?!? of course not.

# For many more examples, see the Higher-Order Functions section.


#%% Example of a function that returns a function object! This is useful to
#   create new function programmatically, as and when needed.
from math import log

def make_logB(base):
    def logB(x): return log(x) / log(base) # ad hoc function created and
    return logB                            # returned as value

log2 = make_logB(2)                 # create a log base 2 function
log2(1024)                          # then call it

# note that the base variable of make_logB went out of scope, but the value
# was passed with the logB function inside a closure (cf. details earlier),
# and thus it is available later when calling the logB function.

def logB(base):
    return lambda x: log(x) / log(base) # same with a lambda expr. (simpler)
                                    # allows creating and calling anonymous
logB(2) (1048576)                   # functions (e.g. for one-time use)

# note again that the base value from logB was returned inside a closure along
# with the lambda expression, which is why the code works as expected.

# The above is also simple example where using a closure might be preferable
# to defining a class that is creating function objects...



################################
##
##  PYTHON DECORATORS
##


#%% This is also useful when defining a decorator i.e, a function that takes
#   another function and extends its behavior without explicitly modifying it!
# Note that decorators in Python make extensive use of closures as well.
def add_stars(func):
    def stars_wrapper(stars='*'*8):
        print(stars)
        func()                      # the value of func is passed inside a
        print(stars)                # closure so that stars_wrapper can use it
    return stars_wrapper

def func1(): print("boring")        # no decorator here
func1()

add_stars(func1)()                  # call the function directly

@add_stars                          # decorator syntax: @ + function name
def func2(): print("Flashy!")       # the decorated function

func2()                             # call the decorated function

func2.__closure__[0].cell_contents  # func2 is a closure function

# The @ syntax is just a shortcut, equivalent to func2 = add_stars(func2)

def func3(): print("decorated?")
func3 = add_stars(func3)
func3()


# note: A decorator is basically a callable that returns a callable i.e., an
# object that implements the special __call__() method (see details earlier).
# A decorator takes a function object as argument, adds some functionality,
# and returns it. Invoking that function calls the decorated version.



################################
##
##  TYPE ANNOTATIONS [v3.6]
##


#%% Standard version, where no type is specified:
def greeting(name):
    print('Hello', name)
# So the argument passed could be anything:
greeting('Sam')
greeting(1234)

# A better version could rely on some operation to raise an exception if the
# arg type is not supported e.g., string concatenation with a non-string arg
# (note this is better than explicitly using isinstance)
def greeting(name):
    print('Hello ' + name)
greeting('Sam')                     # fine; then a non-string argument will
#greeting(1234)                     # cause a TypeError: must be str, not int
                                    # (-> need to catch the exception)

# Using annotations, the type of function arguments and/or its return values
# can be specified. The syntax is similar to Haskell and other languages [FP]
# i.e., using : type to specify paremeter type and -> for the return type
# e.g.
def greeting(name: str) -> str:
    return 'Hello ' + name
# The argument passed could still be anything; type is NOT checked at runtime!
greeting('Sam')
greeting(1234)

# However, code using type annotations is clearer (shows intent), and it can
# now be checked by a separate (off-line) type checker, such as within an
# editor or IDE (e.g. PyCharm!), or by a compiler, etc.
# Many static type checkers are available e.g., Pyright, Pytype, Pyre, Mypy.


#%% Function type annotations are stored in the __annotations__ attribute:
greeting.__annotations__

# Type annotations are also available for variables [v3.6] e.g.
var = 3
# can now be written as follows
var: int = 3
# Type annotations also allow 'declaring' a variable without initializing it.
surname: str

# This again improves clarity even though NO type checking occurs at runtime.
count: int = 'oops'
surname = 1+2j


#%% Composite types via the typing module (annotations)

# so far we can do
names: list = ['Alan', 'Bart', 'Carl']
# which says names is a reference to a list object; but there is no hint
# about the type of the list elements e.g., names[1]. Same for options.
options: dict = {'title': True, 'center': False}

# So we can use instead the special types defined in the typing module.
from typing import Dict, List, Tuple, Sequence # also Set, Deque, Counter...

names: List[str] = ['Alan', 'Bart', 'Carl']
options: Dict[str, bool] = {'title': True, 'center': False}

# The special Sequence type can be used whenever we just need a sequence and
# it does not matter whether it is a list or a tuple... Note that a Sequence
# is anything that supports len() and .__getitem__(), independently of its
#  actual type. (This is another example of Python "duck typing".)
def enum(elems: Sequence[str], start: int = 0) -> List[Tuple[int, str]]:
    return list(enumerate(elems,start))

enum(('a','b','c','d'))
enum(('J','Q','K','A'),10)

# It is also possible to create custom type annotations, as aliases, e.g.
Pair = Tuple[int, str]
Strings = Sequence[str]
# then the above function can be simplified to
def enum(elems: Strings, start: int = 0) -> List[Pair]:
    return list(enumerate(elems,start))


# Reasons to use type hints/annotations in your Python code:
#   (1) Easier to understand and maintain a code base;
#   (2) Easier to refactor code e.g. to find where a class is used;
#   (3) Easier to use libraries e.g. smarter suggestions from IDE;
#   (4) Easier to verify code e.g. using type linter tools;
#   (5) Easier to validate data at runtime e.g. function parameters;
#
# However, type hints/annotations cannot provide runtime type inference,
# or even performance tuning (e.g. to optimise the generated bytecode).
#
# In short, type hints are designed to improve the developer's experience,
# not to influence how a Python script evaluates or how fast it runs.



##
##  END
##
