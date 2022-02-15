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
##  01. Introduction to Python: shell, variables, print, types; for, range,
##                              if/else; numbers; string, slicing, format...
##  02. Sequences and Collections
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
###   01. INTRODUCTION TO PYTHON
###


# Python 3 vs. 2: syntax/implementation differences e.g., print(), range().
# Also fixes and improvements e.g., integer division, increment, iterators.
# Many additions e.g., Unicode (UTF-8), generators, lazy structures, etc.
# Use Python 2 only if legacy code/libraries are needed. Otherwise, don't.



################################
##
##  INTERACTIVE SHELL
##


#%% Allows all kinds of calculations ...
#   Instructions / code are executed immediately (no compilation!)
print('Welcome to Python!')

x = 10                              # variable created (virtual machine!)
x = x * x                           # then updated

                           # and printed

# or just "inspect" the variable (interpreter only)
x
#y                                  # error: variable not defined


# Using the shell as a calculator, interactively! no GUI, but natural syntax
print(25*7 - 13*4)

# Last expression/result available via _ character (can print too...)
# _ * 2


#%% The following is also a Python script / program!
price = 1200
vat = 0.15                          # note: no type! (but see later)
price += price * vat
print(price)                        # no semi-colon: EOL = end of statement
print(vat);                         # (legal but useless semi-colon)

price *= 1.2 ; print(price)         # semi-colon as separator (alt. to EOL)

# Allows all kinds of calculations e.g., to estimate someone's final grade,
# trying many scenarios, programmatically. Example with a range 'for' loop
# (cf. section 3 Flow Control and section 8 about Generators and Iterators).
gradeSoFar = 80
for finalExamGrade in range(40, 100, 5):
    print(finalExamGrade, '->', 0.70 * gradeSoFar + 0.30 * finalExamGrade)

# All the way to powerful computing e.g., series: 1 + 1/2 + 1/3 + ... + 1/10
sum(1/x for x in range(1,11))

# using Higher-Order Functions and Comprehensions (cf. later sections) [FP]
sum(x**3 for x in range(1, 11) if x % 2 == 0)


#%% Python script / program = Python code in a text file e.g., test.py
# To run a script, either (1) open in IDLE and run it (via F5 'Run Module'),
# (2) run it directly in a terminal: python test.py, (3) select test.py and
# 'open with' python.exe (In the last two cases a shell window will open and
# then close quickly, unless user input is required or some GUI is started.)

# One can also open a script and interpret its content programmatically e.g.:
script = "print('hello')"
exec(script)
#exec(open('01-xTkConverterGUIdemo.py').read())

# Single expressions can be interpreted and evaluated instead e.g.:
eval('1 + 2')
# which means one can generate code on the fly and execute it! [FP]
eval('print(8 /' + str(x) + ')')


#%% Experimenting ... typing and evaluating at once e.g., factorial function
# (cf. Flow Control and Functions sections for full details and examples)

def fact(n):                        # function declaration
    if n == 1:                      # function body
        return 1                    # if/else block - indented for syntax!
    else:                           # (1 indent = 4 spaces, exactly)
        return n * fact(n-1)        # note: no parentheses, no brackets

fact(20)
#fact(1024)                         # a very large number, still fast enough
#len(str(fact(1024)))               # -> 2640 = number of digits! [FP]

#fact(1025)                         # RuntimeError: max recursion depth
                                    # exceeded (cf. section 6 Exceptions)

# note: The above limit is when using IDLE. In Anaconda + Snyder one can run
#len(str(fact(2958)))               # so fact(2958) has 8985 digits

# Same factorial function, using functional programming style [FP]
def ffact(n): return 1 if n==1 else n * fact(n-1)


#%% Importing from a module
import math
print(math.pi)                      # need specify scope

# importing selectively
from math import factorial          # import function as is
from math import factorial as fac   # or with a custom name
fac(4321)                           # (squeezed output? click to see)

from math import tan, cos, sin, pi  # multiple import
print( tan(pi) )
print(cos(0)) ; print(sin(0))       # semi-colon now used as separator

from math import cos as sin         # warning: no check - be careful!!!
sin(0)                              # may yield some unexpected result!



################################
##
##  OBJECTS AND TYPES
##


#%% Dynamic typing! Variables defined as and when declared and initialized.
# Type inference! Variable type is automatically determined. So Python is
# neither strongly typed like C++/Java nor typeless like Lisp/Scheme...
x = 5
type(x)                             # 'x' is an object of integer class
x = 'hi!'
type(x)                             # now 'x' is a string object
x = True
type(x)                             # and now it's a Boolean

# Python is strongly typed in the sense that operations incompatible with the
# data type are not allowed (will raise an exception); but it is not static.
# e.g. 2+3 is fine, "two"+"three" is fine, but 2+"three" is not (TypeError!)


# Warning: Everything is a 'variable'! even functions, classes, modules...
# Be careful not to override names e.g., str = "hello" or type = 4


#%% References! (similar to Java) - x above is a reference, not an object
a = 1
type(a)                             # reference to 'int' object (value 1)
b = a                               # another reference to the same object
a = a + 1
a                                   # now refers to another 'int' object (2)
b                                   # refers to the same old 'int' object (1)

# Everything in Python is an object! [pure OOP] incl. functions, classes,
# modules, etc. (and almost everything has attributes and methods). Therefore
# every name / variable is merely a reference to an object! Note also that
# many are immutable [FP] e.g., bool, int, float, str... list, and many more!
print(b, fact, 'hi', str)


# One can 'undefine' a variable but it only deletes the name/reference; it
# does not free the memory. For that, Python has garbage collection!
del x
#print(x)                           # NameError: name 'x' is not defined

del a                               # not like C++ pointers!
print(b)                            # the (int) object is still in memory


#%% Interactive help, about functions, classes, etc. Call help() for prompt.
help
help(print)

# List all instance attributes, functions/methods, and attributes of a class
dir(str)
'find' in dir(str)                  # is 'find' defined for the str class?
dir('a string')
dir()                               # shows all symbols defined in scope



################################
###
###   NUMBER TYPES
###


#%% Definition / assignment
n = 11                              # 'int' variable - only integral type
n = 'Hello'                         # redefined as a string, of type 'str'

m = n = 123                         # sequential assignment
m,n = 17,19                         # parallel assignment!

m,n = n,m                           # parallel swap! elegant and fast
                                    # (good readability and writability)
alist = [1, 2, 3, 4]
m,n,p,q = a,b,c,d = alist           # unpacking: parallel list extraction
                                    # (note: there is no array in Python!)

# note: To appreciate a language feature, it is often best to try and code
# the equivalent in another language! (e.g., try implement the above examples
# of parallel assignment/swap and unpacking in C++/Java...)


#%% More numbers and functions
abs(-11)                            # absolute value
print( 12**2 )                      # exponent - same as math.pow(12,2)
5*2**3                              # careful about operator precedence

15129 ** 0.5                        # square root (et al)
from math import sqrt               # sqrt function only in math module
sqrt(15129)                         # (cf. section 11 Modules and Libraries)

factorial(100)                      # arbitrary precision, hence only two num
2**10000                            # types are needed: 'int' and 'float'

3.1415e-10 / 100                    # floating point number - only real type

print(0xFF)                         # hexadecimal literal (base 16)
print(0o10)                         # octal literal
print(0b101010)                     # binary literal
type(0xFF)                          # (all are still int objects)

print( hex(19) )                    # string representation, also bin/oct


#%% Usual operators... plus integer division
n, d = 7, 3
print(n/d)                          # no type 'declared' so 2.333 is expected

5 / 2                               # correct, intuitive result! (float)
5 // 2                              # floor division (int)

round(9/5)                          # rounding up or down (int)
from math import floor              # ceil and floor in the math module
floor(9/5)                          # same as 9//5

print( --n )                        # no increment or decrement operator!


#%% Complex numbers (immutable)
z = 1+2j                            # notation for 1+2i (better readability)
print(z)
type(z)                             # 'complex' object

z.real                              # real and imaginary parts (attributes)
z.imag                              # accessed directly - eq. to 'getter'
#z.real = 4                         # -> AttributeError: readonly attribute

# No 'setter' needed when the object is immutable [FP]
#z.real = 4                         # AttributeError: readonly attribute

z * (3j)                            # complex number arithmetic
1/z
z**-1
abs(z)
z = 1/z + 7j                        # How many object? references? GC?


#%% Underscores can be used as visual separators for digit grouping purposes
# in int, float, and complex number literals [v3.6+] (better readability).
# This feature was created long ago in ADA; now it's in C# and Java 8!
amount = 10_000_000.0
print(amount)			    # written as regular float (no underscore)

flags = 0b_0011_1111_0100_1110
phone = +971_50_123_4567            # pretty, eh? (yet it is a valid int!)
print(phone)



################################
##
##  STRING TYPE AND SLICING
##


#%% String definition, using single or double quotes (or triple quotes, later)
'hi!'
s = "abcdefghij"
print(s)
type(s)                             # 'string' object

'hello,' + ' world'                 # concatenation (new string object)
'hello,' ' world'

# Parentheses are needed to group multiple lines
txt = ('If a string is too long, break it into a sequence of smaller strings,'
       'each placed on a single line as shown in this example. The sequence'
       'of strings must be surrounded by a pair of grouping parentheses,'
       'so that they will be automatically concatenated back into one.')
# which is easier and clearer than using the escape character \
txtx = 'Yet another line of text ... bla bla bla\
        followed by more text and so on so forth'

'hello, ' * 3                       # repetition! (better orthogonality)
'=' * 40

n = 4                               # allows handing options easily e.g.
print(n, 'piece' + (n>1)*'s')       # '4 pieces' vs. '1 piece' [FP] style!
True * 4                            # because True is 1 and False is 0


#%% String indexing
'hi!' [0]                           # spaces are optional (readability?)
s[1]
s[-1]                               # last item! same as: s[len(s)-1]
s[3]
#s[3] = 'x'                         # not allowed - strings are immutable
                                    # (LHS slicing works for lists et al)

c = 'x'                             # no char type in Python! (not needed)
type(c)                             # same as a string object with 1 element


#%% String slicing
s[2:6]                              # substring from index 2 till before 6
s[4:]                               # substring from index 4 till end
s[:4]                               # substring from start till index 3
'J' + 'Python'[1:]
s[:]                                # substring from start to end: a copy!

sh = 'Hello'
sh = sh[0:3] + 'p!'                 #  =>  0   1   2   3   4   5
                                    #      +---+---+---+---+---+
sh[-3:]                             #      | H | e | l | p | ! |
sh[-3:-1]                           #      +---+---+---+---+---+
                                    #     -5  -4  -3  -2  -1      <=
s[1:7]
s[1:7:2]                            # scanning by interval of 2
s[5:2:-1]                           # scanning backward

#s[100]                             # -> IndexError exception
s[4:100]                            # smart bounds: no out-of-bound exception!


for k in range(len(s)+1):           # s[:k] + s[k:] is invariant
    print(s[:k] + ' ' + s[k:])      # (same as 's' itself, for any k)

for k in range(len(s)):             # C-like code(!) using an index
    print(s[k])                     # (ugly, not Pythonic - don't do that!)

for c in s: print(c)                # Python-style iteration - no index!
                                    # (like C++/Java range loop)


# note: slicing works for many sequential data structures e.g., list, tuple,
# etc. and custom classes (cf. islice in section 8 about Iterators).


#%% Comparison and search
'hello' < 'jello'
'hello' >= 'hi'
if 1 <= n and n <= 10: print(n)     # Boolean connectives (now in C++ etc.)

if 1 <= n <= 10:                    # allows math-like syntax (readability
    print('valid range')            #                       and writability)

'Python' > 'Java' > 'C++' > 'C#'> 'C'# True (alphabetically, but not only ;)

if 'Hel' in sh:                     # check for substring (member, subset...)
    print('yes')

'hello'.find('l')                   # index of first occurence
'hello'.rfind('l')                  # index of last occurence

st = 'two for tea and tea for two'
st.count('tea')                     # number of occurences

st.replace('tea', 'coffee')         # substitution (creates a new string)
st.replace(' ','/')

# Also: search using wildcards and Regular Expressions! (cf. section 9)


#%% More string operations (methods)
len(st)                             # string length - a function [FP]
type(len)                           # but also a class method
st.__len__()                        # (cf. section 5 Classes and OOP)

st.isalpha()                        # checking - 'is' denotes a predicate
'1234'.isnumeric()
'john doe'.istitle()
'abc'.upper()                       # converting
'john doe'.title()
'john doe'.title().istitle()
#"john doe".title().istitle().isalpha()  # ?


'/'.join(['dir','subdir','file'])   # joining strings, with separator
'dir/subdir/file'.split('/')        # splitting, based on separator

# note: String objects are immutable hence concatenating many strings together
# is very inefficient (as each concatenation creates a new object). The best
# approach is to place all strings into a list and call join() at the end.


#%% Splitting and partitioning
'john henry doe'.split()            # N-split (default: space separator)
'john henry doe'.split('h')

'john henry doe'.partition(' ')     # 2-way split, forward or backward
'john henry doe'.rpartition(' ')

# Simple code, thanks to string split, unpacking, and parallel assignment [FP]
address = 'monty@python.org'
username, domain = address.split('@')   # isn't that beautiful?

# Example of parsing an(y) URL to get the domain extension! (com,edu,org...)
url = 'http://docs.python.org/3/tutorial/interpreter.html'
url.split('://')[-1].split('/')[0].split('.')[-1] # OO-style cascading [FP]

def split(s,y): return s.split(y)
split(split(split(url,'://')[-1],'/')[0],'.')[-1] # functional prog. style

str.split(url,'://')
print(split)
print(str.split)

len(str(0.1234567).split('.')[-1])  # number of decimals [FP]


# note: The str class is quite powerful as is. There is also a string module,
# which offers even more functionality. Then, there are regular expressions!
# (cf. string and re and regex modules, in later sections...)



################################
##
##  QUOTES AND COMMENTS
##


#%% A string appearing on one line is in effect a comment. (A string object is
# created by the interpreter but since there is no reference to it...)
'Python is the "most powerful language you can still read". -- Paul Dubois'


# Single and double quotes for strings
'it does not'
'it doesn\'t'                       # escaping characters (old way)
"it doesn't"                        # having ' and " allows mixing easily
print('Then I said "Welcome!" to them.')  # for better read/writ-ability

# Raw strings, where everything is taken literally
print(' one \n two')
print(' one \\n two')               # print \n 'as is' (C++/Java style)
print(r' one \n two')               # raw string - better read/writ-ability



#%% Triple quotes for formatting 'as is'
menu = """
Sessions:
   a) Basic
   b) Advanced
   c) Optional
"""
menu                                # print triple-quoted string 'as is'
print(menu)                         # print as formatted
                                    # (cf. later __str__ vs. __repr__)

"""options:
   a) pizza
   b) pasta
   c) other"""

print("""

    Everything should be made as simple as possible, but not simpler.
        -- Albert Einstein

""")

# Triple quotes can be used for (multi-line) block commenting
"""
def unwanted():
    some code
    to be written
    later
"""

"""                                                 # This is Python !
    _____________________________________________________________________
   |                                                                     |
   |                  /^\/^\                                             |
   |                _|__|  O|                                            |
   |       \/     /~     \_/ \                                           |
   |        \____|__________/  \                                         |
   |               \_______      \                                       |
   |                       `\     \                 \                    |
   |                         |     |                  \                  |
   |                        /      /                    \                |
   |                       /     /                       \\              |
   |                     /      /                         \ \            |
   |                    /     /                            \  \          |
   |                  /     /             _----_            \   \        |
   |                 /     /           _-~      ~-_         |   |        |
   |                (      (        _-~    _--_    ~-_     _/   |        |
   |                 \      ~-____-~    _-~    ~-_    ~-_-~    /         |
   |                   ~-_           _-~          ~-_       _-~          |
   |                      ~--______-~                ~-___-~             |
   |                                                                     |
   |_____________________________________________________________________|

"""



################################
##
##  STRING FORMAT AND OLD %
##


#%% Old 'printf'/'scanf' style (only int, str, and double are supported):

from math import pi                 # pi in math module (48 decimals)
print(pi)                           # default prints only 15 decimals

print('The value of PI is approximately %.4f' % pi)   # 4 decimals

for n in range(1,60):
    print(('%'+str(n+6)+'.'+str(n)+'f') % pi) # varying number of decimals


# Be careful (again), this is Python:
pi = 'apple'                        # destroys original pi value!
from math import pi                 # (only way to restore it)


#%% String format, using {} as placeholder
'1 plus 2 equals {}'.format(3)
'1: {}, 2: {}, 3: {}'.format('A', 0xFFFF, 3+2j) # default order
'3: {2}, 2: {1}, 1: {0}'.format('a', 'b', 'c')  # custom order

# Using positional arguments as references!
'complex {0} has a real part {0.real}\
 and imaginary part {0.imag}'.format(3+2j)
'1: {0[0]}, 2: {0[1]}, 3: {0[2]}'.format(['a', 'b', 'c'])
'2-1: {0[1][0]}, 2-2: {0[1][1]}'.format(['a', ['b','c'],'d'])

# Using (more flexible) keyword arguments instead (cf. Function args)
'Coords: {lat}, {lon}'.format(lon='-115.8W', lat='37.2N')


#%% Like Java, Python supports Unicode (UTF-8 by default! not UTF-16)
print( 'Hello, \u0057\u006F\u0072\u006C\u0064!')    # interpreted code
print(r'Hello, \u0057\u006F\u0072\u006C\u0064!')    # raw string ('as is')

print('\u0645\u0631\u062d\u0628\u0627',       # "Hello, good morning"
      '\u0635\u0628\u0627\u062d \u0627\u0644\u062e\u064a\u0631') # Arabic
print('你好早上好')          # "Nǐ hǎo zǎoshang hǎo" in Chinese characters
print('\u4f60\u597d\u65e9\u4e0a\u597d')       # equivalent Unicode
print('(\u2665) in Chinese "love" is \u611B')

print("Don't use \u221E as a number.  \u03c0 = {}".format(pi)) # ∞ / π
π = 3.14
print ( π )


# Left/right/center justification
'{:<30}'.format('left aligned')
'{:>30}'.format('right aligned')
'{:_^30}'.format('centered')        # replacing filler (default is space)

# Table-like formatting
for n in range(1, 13):
    print('{:3d} {:4d} {:5d}'.format(n, n*n, n*n*n))

# Scientific formatting  with units (as Unicode symbols)
volume, decimals = 7.12345, 2
print('The volume is {0:.{1}f} cm\u00b3'.format(volume, decimals))
print('Current temperature is 12\u00b0 to 25\u2103')

# Printing again, changing the default separator (no space)
print('There are <', 2**32, '> possibilities!', sep='')  # also end=''



################################
##
##  STRING LITERALS [v3.6+]
##


#%% F-strings are more concise and readable than using string format

import datetime                     # (using the powerful datetime module)
name, bday, value = 'Fred', datetime.date(1991, 10, 12), 421
bday
print(bday)                         # custom print function (string repr.
                                    # is not the object - cf. Classes)

# For example, the formatting string and directive
'The value is {}.'.format(value)
# can be written more concisely using an f-string:
f'The value is {value}.'

# Previous example with two variables for data and format:
print(f'The volume is {volume:.{decimals}f} cm\u00b3')

# Provides additional formats not available with %-formatting or string format
f'input={value:#06x}'
f'{bday} was on a {bday:%A}'        # date and week day

age = datetime.date.today().year - bday.year
f"My name is {name}. I am {age}. I'm born on {bday:%A, %B %d, %Y}."


#%% Type conversion may be specified (similar to string format): '!s' calls
# str() on the expression, '!r' calls repr(), and '!a' calls ascii().
# Compare e.g.:
f'He said his name is {name}.'      # string representation
f'He said his name is {name!r}.'    # printable representation

# Backslashes may not appear inside a f-string; so the correct way to have a
# literal brace appear in the resulting string value is to double the brace:
f'{{ {4*10} }}'

# Yes, f-strings are evaluated! Another example:
f'result={factorial(5)}'

# The above is equivalent to:
'result={}'.format(factorial(5))
'result=' + str(factorial(5))

for n in range(2,16):
    print(f'{pi:{n+6}.{n}}') 	    # varying number of decimals (more concise)


#%% F-strings for debugging!

# Add the = symbol at the end of an expression to print both the expression
# and its value (with or without spaces):
from sys import version
version_number = version.split()[0]

print(f'Python {version_number}') # vs.
print(f'Python {version_number=}')

# Previous example again
print(f'The result is {volume=:.{decimals}f} cm\u00b3')



################################
##
##  PYTHON CODING STYLE
##


#%% Use 4-space indentation, and no tabs.
# Wrap lines so that they don't exceed 79 characters.
# Use blank lines to separate functions, classes, and large blocks of code.
# When possible, put comments on a line of their own.
# Use doc strings.
# Use spaces around operators and after commas, but not directly inside
#     bracketing constructs: a = f(1, 2) + g(3, 4); not f( 1, 2 )...
# Name your classes and functions consistently; the convention is to use
#     CamelCase for classes and lower_case_with_underscores for functions
#     and methods. Use self as the name for the first method argument.
# Don't use fancy encodings if your code is meant to be used in
#     international environments. Python's default UTF-8 works best.
#
# Style Guide for Python Code @ http://legacy.python.org/dev/peps/pep-0008/



################################
##
##  THE ZEN OF PYTHON
##


print("""

Python's most famous programming "Easter egg":

>>> import this

""")
import this                         # (cf. Misc section for more Easter eggs)

print(this)



##
##  END
##
