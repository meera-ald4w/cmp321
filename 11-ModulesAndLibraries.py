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
##  11. Modules and Libraries in Python: modules / packages, operating system,
##          locale and time, calendar and date, math and science, programming,
##          performance and profiling, internet and networking, and more...
##  12. Graphics and GUI Extensions
##  13. Threads and Concurrency
##  14. Miscellanies and References
##  15. Scientific Python
##



###############################################################################
###
###   11. PYTHON MODULES AND LIBRARIES
###



################################
##
##  MODULES AND PACKAGES
##


# Every Python file is a module,  equivalent to a package / namespace
# .py file = a collection of functions, classes, "constants"


#%% Importing a module e.g., System module
import sys
sys.argv[0]                         # this script's name
sys.path                            # shell path var (incl. Python dirs)
sys.version                         # Python system description
dir(sys)                            # list all module names (incl. functions)

# from sys import *                 # import everything (not recommended)
from sys import argv
argv[0]                             # now the module name is not needed


# Import and rename
import sys as system                # or
from sys import argv as cmdline_parameters
cmdline_parameters

import __hello__                    # one of Python's Easter eggs
#import antigravity                 # (See Miscellanies section for more...)


# Python offers many useful gems and features "hidden" in utility modules
# e.g. getsizeof:
N = 100_000
size_of_list = sys.getsizeof(   ['' for i in range(100000)])
size_of_dict = sys.getsizeof({i: '' for i in range(100000)})
print('a dictionary can be used instead of a list, but then it is'
      f' about {size_of_dict/size_of_list:.2} times larger')


#%% To create your own module e.g., fractals code/library:
#   - place functions (julia, etc.) and classes in a file: 'fractals.py'
#   - in the interpreter or another script: import fractals
#   - use the desired function: fractals.julia()
#   - rename if used often: julia = fractals.julia
#     alternatively: from fractals import julia as jf


# Packages are a hierarchy of modules / namespaces
# folder/directory = a collection of modules
# Like in Java, the import syntax reflects the folder/file hierarchy
#
# import Py.sci.kdd              for a file myPy/sci/kdd.py
#
# from Py.sci.kdd import *       (bad)
# from Py.sci.kdd import c48           call: c48()
# from Py.sci.kdd import c48 as dt           dt()
# from Py.sci import kdd                     kdd.c48()
# import Py.sci.kdd                          Py.sci.kdd.c48()
# import Py.sci.kdd as DM                    DM.c48()


# Access control: names with leading underscore
# import myPy.sci.kdd            ok, call as: kdd._c36()
# from myPy.sci.kdd import *     not allowed


#%% Main = default module (the interpreter / the executed script)

if __name__ == '__main__':          # executed if run as script
    print('program', sys.argv[0].split('/')[-1], 'starting')

sys.__name__
__name__


# Python comes with "full batteries included" i.e., it is a feature-rich
# language with powerful data structures and functions built-in, *and* it
# has a large collection of libraries for all kind of applications.
# See complete list @ https://wiki.python.org/moin/UsefulModules



################################
##
##  OPERATING SYSTEM MODULES
##


#%% OS and Platform modules

import os, platform

os.name
os.getcwd()                         # current directory
os.listdir('.')                     # list content
# os.system('cmd')                  # run command in system shell
dir(os)                             # list module names

#%% Example: 1-liner (list comprehension with side effect only) to replace all
#   png extensions with jpg in any non-hidden file in the current directory
if os.getcwd()[-7:] == 'png2jpg':
    [os.rename(filename, filename.replace('.png', '.jpg'))
     for filename in os.listdir('.') if not filename.startswith('.')]

platform.system()                   # misc. operating system info
platform.version()
platform.processor()
platform.architecture()

# Also third-party libraries (need download and install first), such as:
# WatchDog: API and shell utilities to monitor file system events


#%% Locale and Time modules

import locale, time

locale.localeconv()                 # dict of local conventions

print(time.strftime('%A, %d %B %Y @ %H:%M:%S'))

if platform.system() == 'Darwin':   # Mac OS X
    locale.setlocale(locale.LC_ALL, 'fr_FR')
elif platform.system() == 'Windows':
    pass # locale.setlocale(locale.LC_ALL, "fr-FR")
else:
    locale.setlocale(locale.LC_ALL, '')
print(time.strftime('%A, %d %B %Y @ %H:%M:%S'))

time.localtime(time.time())         # local current time
time.asctime( time.localtime(time.time()) )


#%% Calendar and Date modules

import calendar
from datetime import date

now = date.today()
now
print(now)

birthday = date(1999, 4, 9)
print(birthday)
print(f'{birthday.day} / {birthday.month} / {birthday.year}')

age = now - birthday                # calendar arithmetic
print('my daughter is', age.days, 'days old\n',
      'her birthday is in', 365-(age.days%365), 'days')

# Also third-party libraries (need download and install first), such as:
# Path: enhanced library for file/path manipulation
# DateUtil: advanced tools for date manipulation
# Sh: allows calling any program as if it were a function!
#     in Python, need: exec(open('01-xTkConverterGUIdemo.py').read())



################################
##
##  MATHS AND SCIENCE MODULES
##


#%% Math and number modules

import math

dir(math)                           # list all available math functions
help(math.trunc)

math.cos(math.pi / 4)
math.log(1024, 2)

from math import log
log(1024, 2)

# watch out (again): from math import log as exp (!) then exp(16,2) is 4
# also: cmath for mathematical functions on complex numbers.


#%% Decimals, fractions, numbers

from decimal import Decimal,getcontext

sum([0.1]*10) == 1.0                # false, because of precision error
sum([Decimal('0.1')]*10) == Decimal('1.0')  # true

getcontext().prec = 50              # 50-digit precision
Decimal(1) / Decimal(7)

from fractions import Fraction
print(Fraction(4,3) + Fraction(7,5))

# Class hierarchy: object > Number > Complex > Real > Rational > Integral

#%% more precision error, due to non-associative operators(!)
a1 = (0.1 + 0.2) + 0.3
a2 = 0.1 + (0.2 + 0.3)
a1 == a2                            # false
print('%.17f != %.17f' % (a1,a2))

a3 = (17 + 1e32) - 1e32
a4 = 17 + (1e32 - 1e32)
a3 == a4                            # false
print('%f != %f' % (a3,a4))


#%% Random module

import random

random.choice(['apple', 'pear', 'banana'])
random.random()                     # random float
random.randrange(6)                 # random integer in given range
random.sample(range(20),10)         # sampling without replacement!

d={1:0,2:0,3:0,4:0,5:0,6:0}
for x in range(10000*len(d)):
    d[random.randint(1,len(d))] += 1
print(d)

d={}
for k in range(16): d[k] = 0
for x in range(1000*len(d)):
    d[int(random.gauss(len(d)//2, 2.0))] += 1 # Gaussian distrib (mu,sigma)
for k in d:
    print('%2d:'%k, '*'*(d[k]*66//max(d.values()))) # plot the distrib


# note: The pseudo-random generators in the random module should not be used
# for security or cryptographic uses; use the 'secrets' module instead.
# Also: cryptography, hashing, and SSL support.
# Also third-party modules (need download and install first), such as:
# M2Crypto and pyOpenSSL: Python interfaces to OpenSSL
# Python Cryptography Toolkit: crypto-related algorithms and protocols


#%% Statistics module
from statistics import mean,stdev,pvariance, fmean,geometric_mean,quantiles

sampledata = [1.0, 2.5, 3.25, 5.75]
mean(sampledata)              # arithmetic mean
geometric_mean(sampledata)    # [v3.8]
stdev(sampledata)
pvariance([Decimal('27.5'), Decimal('30.25'), Decimal('30.25'), Decimal('34.5')])
quantiles(sampledata, n=4)    # [v3.8]


# Scientific and AI modules (need download and install first), such as:
#
# SciPy and NumPy: advanced math functions and algorithms
# Matplotlib: Python 2D and 3D numerical plotting library
# SciKit-Learn and Pandas: machine learning and data mining
# PyMC3: Bayesian statistical modeling and probabilistic machine learning
# Pattern: web mining module, incl. language processing and data mining
# PyX: Postscript and PDF output, (La)TeX integration
# SymPy: algebraic evaluation, symbolic processing
# NLTK: powerful natural language processing toolkit
# Pyke: logic programming
#
# SPARK: Scanning, Parsing, and Rewriting Kit; cf. Aycock's "Compiling Little
#   Languages in Python" @ http://pages.cpsc.ucalgary.ca/~aycock/spark/



################################
##
##  ENTERTAINMENT AND GAMES
##


# Game modules (need download and install first)
# PyGame: rich game development framework
# Pyglet: 3D animation and game creation engine
# Panda3D: library for 3D rendering and game development
# Pyganim: a simple module for sprite animation
# Python-Ogre: a complete environment for game creation

# Multimedia services and audio modules
# aifc, audioop, chunk, wave
#
# Also third-party modules (need download and install first), such as:
# Mutagen: Python module to handle audio metadata
# PyTagger: tag reader and writer implemented purely in Python
# Nsound: C++ library with Python module for audio synthesis
# Pydub: a high-level audio interface for Python



################################
##
##  GRAPHICS AND GUI EXTENSIONS
##

# See dedicated section -- about TKinter and Turtle (built-in Python)
# also third-party GUI modules, such as wxPython, pyQT, PyGTK, PyOpenGL,
# PyGUI, EasyGUI, PyWin32, IronPython, Pillow and PIL, PyQtGraph, VPython.



################################
##
##  PROGRAMMING MODULES
##


# Data structures: array, collections, Queue
# Database modules: anydbm, dbm, dumbdbm, gdbm, sqlite3
# Serialization: pickle

# Also third-party modules (need download and install first), such as:
# SQLAlchemy: OO way of accessing several different database systems
# SQLObject: database library


#%% Formatting (more)
import pprint                       # pretty print

mtx = [[[['black', 'cyan'], 'white', ['green', 'red']],
      [['magenta','yellow'], 'blue']]]
print(mtx)
pprint.pprint(mtx, width=40)
pprint.pprint(mtx, width=30)

import textwrap
doc = '''The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines.'''
print(textwrap.fill(doc, width=30))

# Also third-party modules (need download and install first), such as:
# TabNanny


#%% Measuring performance
from timeit import timeit

# testing code snippets
timeit('t=a; a=b; b=t', 'a=1; b=2', number=10000) # parallel swap is
timeit('a,b = b,a', 'a=1; b=2', number=10000)     # twice as fast

timeit('text.find(ch)', 'text = "sample string"; ch = "g"')
timeit('ch in text',    'text = "sample string"; ch = "g"') #faster


# Comparing the performance of the new statistics.fmean() [v3.8] vs. the
# traditional statistics.mean() function on floating point numbers.
from random import random
from statistics import NormalDist

def mean_perf_test(size=10_000, repeat=100, samples=30):
    # Create 10,000 random numbers
    data = [random() for _ in range(size)]
    # Measure the time it takes to run mean() and fmean()
    t_mean = [timeit('mean(data)', number=repeat, globals=globals())
              for _ in range(samples)]
    t_fmean = [timeit('fmean(data)', number=repeat, globals=globals())
               for _ in range(samples)]
    # Create NormalDist objects based on the sampled timings
    n_mean = NormalDist.from_samples(t_mean)
    n_fmean = NormalDist.from_samples(t_fmean)
    # Compare the sample means and standard deviations
    print((n_mean.mean, n_mean.stdev))
    print((n_fmean.mean, n_fmean.stdev))

#mean_perf_test()           # shows that fmean is about 80 times faster


#%% testing longer code via functions
def ttest(l = [],N=100_000):
    for i in range(N): l.append(i)

timeit('ttest()', 'from __main__ import ttest')

import time
def ttime(func):
    start = time.time();
    func();
    print(time.time()-start)

ttime(ttest)


#%% More tools:
#
# IDLE: interactive development environment, includes a graphical debugger
# pdb: simple but adequate console-mode debugger for Python
# profile, timeit, trace
#
# Also third-party development modules (need download and install first):
# CTypes: package for calling the functions of dlls/shared libraries
# Cython: extension for the CPython runtime, translates Python code to C
# JCC and JPype: accessing the libraries of and integrating with Java
# Jython: seamless integration of Python with the Java platform
# PyChecker: analysis tool to detect bugs, code complexity, and style issues
# PyObjC: bridge between Python and Objective-C, allows Mac/Cocoa GUI
# SWIG and SIP: auto-magically generate Python objects from C++ / C code
# Nose: a testing framework used by millions of Python developers
#
# IPython: interpreter with completion, history, shell, inline graphics, etc.;
#    its (online) Jupyter notebook make your Python experience similar to that
#    of using scientific software such as Matlab or Mathematica...
# Pyzo: can be considered a free alternative to Matlab
#
# Boa Constructor: cross-platform Python IDE and wxPython GUI Builder
# Eric: IDE built on PyQt and the Scintilla editing library
# Komodo IDE, PyCharm (free community edition), Wing IDE
#
# Python software design patterns: cf. https://python-patterns.guide/



################################
##
##  INTERNET AND NETWORKING
##


#%% Internet modules

import urllib; from urllib.request import urlopen

CLOCK_URL = 'http://tycho.usno.navy.mil/cgi-bin/timer.pl' # (a Perl script ;)

def getEasternTime():
    try:
        for line in urlopen(CLOCK_URL):
            line = line.decode('utf-8')        # decoding binary data into text
            if 'EST' in line or 'EDT' in line: # looking for Eastern Time
                print(line.replace('<BR>',''))
    except urllib.error.URLError:
        print("error: cannot access website")

#getEasternTime()


#%% retrieving an image
from urllib.request import urlretrieve
import webbrowser

PUPPY_URL = 'http://www.imgion.com/images/01/White-Cute-Puppy-.jpg' # so cute!

# Download file to disk
urlretrieve(PUPPY_URL, PUPPY_URL.split('/')[-1])


#%% Open file in default web browser!
#webbrowser.open(PUPPY_URL)


# Also: mailbox, smtplib, urlparse
# Web: webbrowser, BaseHTTPServer, Cookie, robotparser
# Network: socket, SocketServer
# Encryption/compression: codecs, gzip, zlib, zipfile



################################
##
##  THIRD-PARTY MODULES
##


# Regex: regular expressions, like RE but with additional features
# 	@ https://pypi.python.org/pypi/regex/
# Requests: HTTP library
# Scrapy: fast, high-level screen scraping and web crawling framework
# PyQuery and BeautifulSoup: XML and HTML parsing libraries
# FuzzyWuzzy: allows to perform fuzzy comparison on text
# Asyncoro: asynchronous, concurrent programming framework
# Twisted: powerful event-driven networking engine written in Python
#     @ https://twistedmatrix.com/trac/
# Scapy: packet sniffer and analyzer for Python made in Python
# GIS Web services: packages to access to Google Maps, Yahoo! Maps
# Django: high-level Web development framework
# Flask: Web development
#
# (See also the Miscellanies and References section for more...)


# More: https://numfocus.org/sponsored-projects



################################
##
##  MODULE METADATA
##


# Python [v3.8] added a metadata module to the standard library, which can
# provide diverse information about the installed packages.

from importlib import metadata

metadata.version('pip')
pip_metadata = metadata.metadata('pip')
list(pip_metadata)
pip_metadata['Home-page']
pip_metadata['Requires-Python']

# One can also check package dependencies:
metadata.requires('matplotlib')


##
##  END
##
