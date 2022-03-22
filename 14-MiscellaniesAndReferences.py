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
##  08. Iterators/Generators and Lazy Data Types
##  09. Regular Expressions and Pattern Matching
##  10. Reflection and Meta-programming
##  11. Modules and Libraries in Python
##  12. Graphics and GUI Extensions
##  13. Threads and Concurrency
##  14. Miscellanies and References: more code / applications, performance,
##                        further readings, future developments, misc misc
##  15. Scientific Python
##



###############################################################################
###
###   14. PROGRAMMING MISCELLANIES
###



################################
##
##  STUFF AND MORE STUFF
##

#%% Code and examples that didn't fit in any earlier section


# Finding the IDLE settings directory .idlerc which should be in the user's
# home directory. Code adapted from idlelib/configHandler.py.
import os, sys
def GetUserCfgDir():
    '''Return a directory for storing user config files (creates it if needed).
    '''
    cfgDir = '.idlerc'
    userDir = os.path.expanduser('~')
    if userDir != '~':              # expanduser() found user home dir
        if not os.path.exists(userDir):
            warn = ('\n Warning: os.path.expanduser("~") points to\n ' +
                    userDir + ',\n but the path does not exist.')
            try:
                print(warn, file=sys.stderr)
            except OSError:
                pass
            userDir = '~'
    if userDir == '~':              # still no path to home!
        userDir = os.getcwd()       # traditionally IDLE has defaulted to
    userDir = os.path.join(userDir, cfgDir) # os.getcwd(), is this adequate?
    if not os.path.exists(userDir):
        try:
            os.mkdir(userDir)
        except OSError:
            warn = ('\n Warning: unable to create user config directory\n' +
                    userDir + '\n Check path and permissions.\n Exiting!\n')
            print(warn, file=sys.stderr)
            raise SystemExit
    # TODO continue without userDIr instead of exit
    return userDir

#print(GetUserCfgDir())             # e.g. 'U:\.idlerc' (shared Nasfiler1)



################################
##
##  IMPROVING PERFORMANCE
##


#%% General guidelines (from the Python FAQ):
#
# Make your algorithms faster (or change to faster ones). This will yield much
# larger benefits than trying to sprinkle micro-optimization tricks all over
# your Python code.
# Use the right data structures. Study documentation for built-in types and
# collections module.
# When the standard library provides a primitive for doing something, it is
# likely (although not guaranteed) to be faster than any alternative you may
# come up with. This is doubly true for primitives written in C, such as all
# built-ins and some extension types. For example, use either the list.sort()
# built-in function or the related sorted() function to do sorting.
# Abstractions tend to create indirections and force the interpreter to work
# more. If the levels of indirection outweigh the amount of useful work done,
# your program will be slower. You should thus avoid excessive abstraction,
# especially under the form of tiny functions or methods (which are also often
# detrimental to readability).
#
# Performance can vary across Python implementations (default is CPython).
# Behaviour can vary across operating systems, especially when talking about
# I/O or multi-threading.
# Always find the hot spots in your program before attempting to optimize any
# code (see the profile module).
# Writing benchmark scripts will allow you to iterate quickly when searching
# for improvements (see the timeit module).
# It is highly recommended to have good code coverage (through unit testing
# or other technique) before potentially introducing regressions hidden in
# sophisticated optimizations.



################################
##
##  FURTHER READING
##


#%% Tutorials
#
# Python.org Official website @ http://www.python.org/
# Python Wiki @ http://wiki.python.org/moin/
# Python Tutorial @ http://docs.python.org/3/tutorial/
# Python Bibliotheca @ http://openbookproject.net/pybiblio/
# Learn Python (v2) Interactive Tutorial @ http://www.learnpython.org/
#


#%% Books
#
# Dive into Python (Oilgrim) free d/l @ http://www.diveintopython3.net/
# Think Python (Downey) free d/l @ http://www.greenteapress.com/thinkpython/
# Start Programming with Python (Jackson) online and free d/l
#       @ http://python-ebook.blogspot.com/
# Learning Python the Hard Way (Shaw) online
#       @ http://learnpythonthehardway.org/book/
# Python introductory books @ http://wiki.python.org/moin/IntroductoryBooks
# Invent Your Own Computer Game With Python (online), also using Graphics,
#       Learn Coding for Automation, Encrypt Messages and Hack Ciphers
#       @ http://inventwithpython.com/
# Data Structures and Algorithms with OO Design Patterns in Python (Preiss)
#       @ http://www.brpreiss.com/books/opus7/
#


#%% Software and libraries
#
# Active Python (free, Win)
#       @ http://www.activestate.com/Products/ActivePython/
# IDLE (open source, Mac/Win) @ http://www.python.org/ftp/python/
# PyCharm IDE (free/pro, Mac/Win/Linux)
#       @ http://www.jetbrains.com/pycharm/index.html
# Python Turtle demo -- built-in(!) cf. "Help" menu -> Turtle Demo; also
#       @ https://code.google.com/p/python-turtle-demo/downloads/list
# wxPython GUI toolkit @ http://www.wxpython.org/
# PyFLTK GUI project @ http://www.fltk.org/
# Useful modules @ http://wiki.python.org/moin/UsefulModules
# Python Game Development Library @ http://www.pygame.org/
# Popular Python Recipes @ http://code.activestate.com/recipes/langs/python/
# Scientific modules (also numpy) @ http://www.scipy.org
#     tutorial @ http://wiki.scipy.org/Tentative_NumPy_Tutorial
# Python Scientific Lecture Notes @ http://scipy-lectures.github.io/
# Machine learning module @ http://www.scikit-learn.org
# Logic programming @ http://www.pyke.sourceforge.net
# Text processing @ http://www.crummy.com/software/BeautifulSoup/
# !!! useful d/l @  http://www.lfd.uci.edu/~gohlke/pythonlibs/
#
# (See also Modules and Libraries section)
#


#%% Python code engineering and module/package management
#
# PIP @ https://pypi.python.org/pypi/pip
# Pylint code checking and error detection @ http://www.pylint.org/
# Pyreverse UML Diagrams for Python @ http://www.logilab.org/blogentry/6883
#


#%% Python examples and programming problems
#
# ActiveState Popular Python recipes
#       @ http://code.activestate.com/recipes/langs/python/
#
# Python for Fun @ http://www.openbookproject.net/py4fun/
# Programming practice @ http://codingbat.com/python
# Challenging math/computer problems @ http://projecteuler.net/
#



################################
##
##  IDLE INFORMATION AND TIPS
##


#%% IDLE official doc @ https://docs.python.org/3.3/library/idle.html
#
# IDLE Themes @ http://www.roguecode.net/2011/09/python-idle-themes.html
#
# IDLE settings -- Custom Highlighting (see in this tutorial)
# Python keywords: 222,0,0 (reddish)
# Python definitions: 0,0,255 (blue, default)
# Python builtins: 144,0,144 (purple, default)
# Python comments: 0,128,0 (dark green)
# Python strings: 0,128,128 (turquoise) or 255,128,0 (orange)
# Normal text /code: 0,0,0 (black, default)
# All other text: R,G,B (default)



################################
##
##  FUTURE DEVELOPMENTS
##


#%% Forthcoming features can be seen in the __future__ module
import __future__
dir(__future__ )

from __future__ import barry_as_FLUFL
0 <> 1                                  # actually works
# 0 != 1
#-> SyntaxError: with Barry as BDFL, use '<>' instead of '!='


# What about C/C++ style curly braces? (another "Easter egg") try:
#from __future__ import braces



################################
##
##  LAST WORDS
##


#%% More Python fun

print('_'*73,'''

# Python's most famous Easter egg:
import this

''')
import this

print('_'*73,'\n\n')
#print(this.s)                          # ROT13 version of the above


# Misc fun and Easter eggs
love = this
this is love
love is True
love is not all
love is not True or False; love is love


# The hash value of infinity and NaN
hash(float('inf'))                      #-> 314159 (PI? makes sense...)
hash(float('nan'))                      #-> 0 (but of course!)


# Hello, world!
import __hello__

#import antigravity                     # flying with Python (cf. XKCD
                                        #     @ http://xkcd.com/353/ )


##
##  END
##
