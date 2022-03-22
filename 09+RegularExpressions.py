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
##  09. Regular Expressions and Pattern Matching: power of regex, syntax and
##              metacharacters, compiling patterns, functions, applications
##  10. Reflection and Meta-programming
##  11. Modules and Libraries in Python
##  12. Graphics and GUI Extensions
##  13. Threads and Concurrency
##  14. Miscellanies and References
##  15. Scientific Python
##



###############################################################################
###
###   09. REGULAR EXPRESSIONS
###



################################
##
##  THE POWER OF RE / REGEX
##


# Very powerful pattern matching tool! e.g., in text editors, incl. IDLE(!)
# Example: searching for "using" in this tutorial file will give 12 matches.
# But how to find the lines that contains "using" followed by "expression"
# and only those? This is a pattern! "using.*expression" -> 4 matches.
#
# Note that the pattern "reg.*exp" greedily matches anything that includes
# this pattern, incl. "regexp" and "regular expression", while the pattern
# "[a-z][0-9]" matches any lowercase letter followed by a digit, etc.
#
# Simplified regex are used everywhere(!) e.g., in Google search, Excel...
import webbrowser
print(webbrowser.__doc__)
#webbrowser.open('http://www.googleguide.com/category/query-input/')


#%% Regular Expression (RE) module. There is also another, third-party module
#   called regex, which is compatible with RE and provides additional features.
import re

# Example: the goal is to abbreviate 'ROAD'as 'RD.' in a street address.
# Yes, string functions can be used... but only so far e.g.
addr = '100 NORTH MAIN ROAD, LONDON NW1, UK'
addr.replace('ROAD', 'RD.')         # works fine

adr = '100 NORTH BROAD ROAD, LONDON NW1, UK'
adr.replace('ROAD', 'RD.')          # oops!

adr.replace('ROAD,', 'RD.,')        # OK, but what if . or ; instead of , ?
									# need to repeat many ad hoc replacements

# We need to use patterns! find and return matches, perform substitutions

re.sub('\bROAD\b', 'RD.', adr)      # matches ROAD when it's a word by itsef

re.sub('ROAD([.,;!])', 'RD.\\1', adr) # matches any punctuation! (cf. groups)

re.sub('[.,;!?:]', '', 'Hello? cheers, uh? bye.') # strip any punctuation


# search(), findall(), match() take 2 args: a search pattern and a string;
# sub() take 3 args: a search pattern, a replacement pattern, and a string.

# note: all characters appearing in a regex match literally, unless they are
#       meta-characters or part of a pattern expression.



################################
##
##  METACHARACTERS AND SYNTAX
##


#%% Any character is matched literally unless it is a metacharacter or a
#   regex pattern -- as elaborated hereafter.

#[ ] specify a character class
fstr = 'which foot or hand fell fastest'
re.findall('[aeiou]', fstr)         # find all vowels

# also by range, using '-'
re.findall('[a-d]', fstr)           # find all chars from 'a' to 'd'
re.findall('[a-d][mnp]', fstr)      # same, followed by m, n, or p

# ^ means negation if within brackets
re.findall('[^e-z]', fstr)          # find all chars except from 'e' to 'z'
re.findall('[^e-z ]', fstr)         # same, ignoring space chars as well
re.findall('[^aeiou ]', fstr)       # find all consonants

# metacharacters are matched literally within brackets
re.findall('[o.]', 'pi is 3.1415 approximately')

# | matches either of the given alternatives (using parentheses for grouping)
re.findall('ha|st', fstr)
astr = '1 cat, 2 dogs, 3 more cats, 4 hamsters, 7 small dogs, 9 cats'
re.findall('(cat|dog)s', astr)
re.findall('[0-9] (cat|dog)s', astr)

re.findall('a|e|i|o|u', fstr)       # better use [aeiou]


#%% . matches anything except a newline character (use DOTALL flag for that)
#   e.g. 'f..t' matches a 'f' followed by any 2 chars followed by a 't'.
re.findall('f..t', fstr)
re.findall('f..t ', fstr)

# * is a wildcard that matches zero or more instances of the previous char
#   e.g. 's*t' matches zero or more 's' followed by a 't'
sstr = fstr + ' ssssstupid'
re.findall('s*t', sstr)

# .* is a common pattern that finds any character zero or more times,
#    but it is GREEDY, meaning it captures as many characters as possible!
#    e.g., everything from the first 'f'to the last 't'
re.findall('f.*t', sstr)

# .*? with the added ? makes the pattern NOT greedy, so it captures as
#     few characters as possible e.g., everything between 'f' and 't'
re.findall('f.*?t', sstr)           # parsing/matching is left-to-right


#%% + is a wildcard that matches one or more instances of the previous char
#   e.g. 's+t' matches one or more 's' followed by a 't'
re.findall('s+t', sstr)

# ? is a wildcard that matches zero or one instance of the previous char
#   e.g. 'fo?' matches 'f' followed by zero or one 'o' (thus not greedy)
lstr = fstr + ' foooool ?'
re.findall('fo?', lstr)

#   whereas 'fo*' matches 'f' followed by zero or more 'o' (greedily!)
re.findall('fo*', lstr)
#   and 'fo+' matches 'f' followed by one or more 'o' (greedily!)
re.findall('fo+', lstr)

re.findall('fo+?', lstr)
#   of course 'fo' matches 'f' followed by one 'o' (ignoring everything else)
re.findall('fo', lstr)

re.findall('fo.*?l ?', lstr)        # ends with an optional space char
re.findall('fo.*?l \?', lstr)       # ends with escaped ? taken literally

# note: the syntax of regex is similar to EBNF w.r.t. the metacharacters
#       denoting the number of occurences ? * + as well as [] and ().


#%% \ escapes string literals e.g., use '\[' to find the bracket char

# \  also defines special sequences:
# \b word boundary
# \d matches any digit character, same as [0-9]
# \D matches any non-digit character, same as [^0-9]
# \s matches any whitespace character, same as [ \t\n\r\f\v]
#    (space, tab, newline, carriage return, formfeed, vertical tab)
# \S matches any non-whitespace character, same as [^ \t\n\r\f\v]
# \w matches any alphanumeric character, same as [a-zA-Z0-9_]
# \W matches any non-alphanumeric character, same as [^a-zA-Z0-9_]

re.findall('\s[^aeiouy]', fstr)
re.findall('\w+', fstr)             # find words

txt = 'He was carefully disguised yet he was quickly found (polyonymy).'
re.findall('\w+ly', txt)            # find all 'adverbs' in the text
re.findall(r'\w+ly\b', txt)         # need stop at 'ly': use word boundary

# Caution: backslash is used both by strings and by regex; we need to prevent
# regex metacharacters to be interpreted as string metacharacters! e.g.
print('hello,\tworld\b!\n--\s\w--') #-> 3 out of 5 are interpreted
# Use r or R (for "raw") before the string. Or use \ as escape char.

re.findall('\w+ly\b', txt)          # looking for \b the backspace char!
re.findall('\w+ly\\b', txt)         # need escape \b only (\w  is not special)
re.findall(r'\w+ly\b', txt)         # raw string (not string interpreted)


#%% ^ matches the start of a line or string (different from ^ inside brackets)
#   $ matches the end of a line or string if multiline search is used.
re.findall('^s\S+ \S+', 'she sells sea shells on the sea shore')

# { } specify a min/max number of instances: x{m,n} means 'x' at least
#     m times and at most n times (inclusive); similar to EBNF. Thus {,} is
#     the same as * and {1,} is the same as + and {0,1} is the same as ?
# e.g.
re.findall('fo{1,3}', lstr)         # 'f' followed by 1,2, or 3 'o'
re.findall('fo{1,3}[^o]', lstr)     # and only 3 - but ...
re.findall('(fo{1,3})[^o]', lstr)   # need to exclude the extra char



################################
##
##  GROUPS AND BACK-REFERENCES
##


#%% ( ) specify the matching results to be extracted (grouping)
#   i.e., which part(s) of the pattern is returned.
re.findall('[0-9] (cat|dog)s', astr)   # logical OR, but also grouping
re.findall('([0-9]) (cat|dog)s', astr) # now returning the digit as well
re.findall('([0-9] (cat|dog)s)', astr) # () for grouping alternatives

# ?: specify non-grouping parentheses
re.findall('([0-9] (?:cat|dog)s)', astr)
re.findall('[0-9] (?:cat|dog)s', astr) # whole match returned by default

re.findall(r'\w+ly\b', txt)
re.findall(r'(\w+)ly\b', txt)       # extract adverb's root only

wstr = 'he came, looked, called, then left, wondering'
re.findall('\w+(ed|ing)', wstr)     # verb ending only
re.findall('(\w+)(ed|ing)', wstr)   # both root and ending
re.findall('\w+(?:ed|ing)', wstr)   # root only

htm = '<html><head><title>Tutorial</title>(3/14/15)</head><body>etc.'
re.findall('<title>.*</title>', htm)# extract all (default)
re.findall('<title>(.*)</title>', htm) # extract title string only


#%% \1 \2 ... \n back-references refer to the contents of the matching groups,
#   in the same order: \1 is the first group, \2 is the second group, etc.
# note: This feature does not exist in EBNF; it requires an attribute grammar.
# e.g. to find matching HTML tags:
re.findall('<(.+)>', htm)           # oops again (greedy match)
re.findall('<(.+?)>', htm)          # non-greedy match!
re.findall('<([^>]+)>', htm)        # same but faster (no backtracking)

html = htm + '<h1>Section</h1><p>bla bla bla</p>'
re.findall('<([^>]+)>.*</[^>]+>', html) # find open/close tags (wrong way)
re.findall('<([^>]+)>.*</\\1>', html) # matching tags using a back-reference
re.findall(r'<([^>]+)>.*</\1>', html) # same, using raw string (no \ escape)

# Using back-references to replace a matched string
re.sub('<title>(.*)</title>', 'Bibliography', htm) # wrong: replaces tags too
re.sub('(<title>)(.*)(</title>)', r'\1Bibliography\3', htm) # correct

re.sub('ROAD([.,;!])', r'RD.\1', adr) # keeping the punctuation (earlier ex)


#%% Example of parsing a URL to get the domain extension (again)
url = 'http://docs.python.org/3/tutorial/interpreter.html'

# this example can be done using string functions and slicing (earlier) i.e.
url.split('://')[-1].split('/')[0].split('.')[-1]
# now using a regular expression (which can be compiled, to run even faster)
re.findall('://.*\.(.*?)/', url)[0]

# step by step:
re.findall('://', url)              # find '://'
re.findall('://(.*)', url)          # find '://', keep right part only
re.findall('://(.*/)', url)         # stop at '/', but search is greedy!
re.findall('://(.*?/)', url)        # non-greedy, keep the first match only
re.findall('://(.*?)/', url)        # same except / is not returned
re.findall('://(.*?)\.(.*?)/', url) # grabs one only, leaves too many
re.findall('://(.*)\.(.*?)/', url)  # greedy! grabs all '.' before last
re.findall('://.*\.(.*?)/', url)

print(*re.findall('://.*\.(.*?)/', url))

re.findall('://(.*?/){3}', url)     # ex. to keep the third match only



################################
##
##  COMPILING REGEX PATTERNS
##

#%% Python can compile regular expressions, for increased performance! (Just
#   like it can compile functions and files to bytecode; cf. Section 10.)

pat = re.compile('://.*\.(.*?)/')
print(pat)
pat.findall(url)[0]                 # same as above, but much faster!

p = re.compile('f[a-z]*')
p.findall(fstr)

print(p)                            # compiled regex (object)
print(p.pattern)                    # regex pattern (string)

for m in p.findall(fstr): print(m)


# but, findall() explicitly generates the list: better use an iterator!
fit = p.finditer(fstr)

for m in fit: print(m.group())      # for each match, print the string

for m in p.finditer(fstr):          # new/reset iterator
    print(m.span())                 # for each match, print start/end pos



################################
##
##  MORE FUNCTIONS AND EXAMPLES
##


#%% String split can only use a single delimiter throughout; regex split can
#   break a string apart using some regular expression as delimiter!
p = re.compile(r'f...\b')
p.split(fstr)

p1 = re.compile(r'\W+')             # one or more non-alphanumeric character
p1.split(fstr)
p1.split(fstr + ' | with punctuation')


# Substitute the matched regular expression with another string
p.sub('f---', fstr)
p.subn('f---', lstr)
p.sub('f---', lstr, count=2)

# Greedy vs. not-greedy matching
re.match('<.*>', htm).group()       # matches all from first < to last >
re.match('<.*?>', htm).group()      # matches from first < to first >
re.match('<.*?>', htm).span()


#%% Matching vs. searching
re.match('<title>(.*)</title>', htm)           # None - no match
re.search('<title>(.*)</title>', htm)
re.search('<title>(.*)</title>', htm).group()  # what is matched
re.search('<title>(.*)</title>', htm).groups() # what is found
re.search('<title>(.*)</title>', htm).span()   # where it is found

re.search('<([^>]+)>(.*)</\\1>', htm).groups() # 1st group for back-reference
re.search(r'<([^>]+)>(.*)</\1>', htm).groups() # 2nd group for extraction

re.search(r'<([^>]+)>(.*)</\1>', htm).group(2) # get second group by index
re.search(r'<([^>]+)>(?P<string>.*)</\1>', htm).group('string') # by name!

re.search('<(head|title)>(.*)</', htm).groups() # first group for OR
re.search('<(?:head|title)>(.*)</', htm).groups() # non-grouping


# note: HTML and XML have a very complex syntax; one should use the html
#      and xml modules, and esp. the html.parser submodule.


#%% Because regex can become rather complex, it is possible to format them on
#   multiple lines, and also to add some comments! This is the 'verbose' mode,
# that uses triple quotes syntax (just like for function docs). Example:

name_pattern = '(\w+)\s+(?:([\w.]+)\s+)?(\w+)' # compact but cryptic
# can be written more clearly:
name_pattern = '''
    (\w+)               # first name
    \s+                 # space(s) separator
    (?:([\w.]+)\s+)?    # optional middle name or initial, and space(s)
    (\w+)               # last name
    '''
re.search(name_pattern, 'John M. Coetzee', re.VERBOSE)

# In verbose mode, whitespace chars (spaces, tabs, linefeeds) are ignored.
# (So to match a space, it needs to be escaped with a backslash.)
# Comments are also ignored (obviously!) They're just like Python comments.
# Lastly, the re.VERBOSE flag must be added as arg for the regex to work.

compiled_name_pattern = re.compile(name_pattern, re.VERBOSE)
re.search(compiled_name_pattern, 'John M. Coetzee').groups()


#%% See also tutorial slides about Regular Expressions syntax and usage.
#   Many online tools are available e.g. @ https://regex101.com/#python
# also many reference sites e.g. @ http://www.regular-expressions.info



################################
##
##  APPLICATIONS OF REGEX
##


# Applications of regular expressions include:
# - Parsing: identifying pieces of text that match certain criteria
# - Searching: locating substrings that can have more than one form, for
#   example, finding any of “pet.png”, “pet.jpg”, “pet.jpeg”, or “pet.svg”
#   while avoiding “carpet.png” and similar
# - Replacing: for example, finding "bicycle" or "human powered vehicle"
#   and replacing either with "bike"
# - Splitting: breaking a string into multiple substrings everywhere a
#   certain delimiter appears (a space, colon, slash...)
# - Validating: checking whether a piece of text meets some criteria, for
#   example, if it contains a currency symbol followed by digits


# The following examples are related to the concept of language grammar,
# where a regex is used instead of the more conventional E/BNF notation.
# Included are two grammars for roman numerals and US phone numbers.


#%% Here is an example for validating roman numerals
roman_numeral_pattern = '''
    ^                   # beginning of string
    M{0,4}              # thousands - 0 to 4 M's
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
                        #            or 500-800 (D, followed by 0 to 3 C's)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
                        #        or 50-80 (L, followed by 0 to 3 X's)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
                        #        or 5-8 (V, followed by 0 to 3 I's)
    $                   # end of string
    '''

re.search(roman_numeral_pattern, 'MCMLXXXIX', re.VERBOSE)  # succeeds
re.search(roman_numeral_pattern, 'MCMLXXXXIX', re.VERBOSE) # fails


#%% This example shows how to parse US phone numbers
phone_pattern = re.compile(r'''
                # don't match beginning of string, number can start anywhere
    (\d{3})     # area code is 3 digits (e.g. '800')
    \D*         # optional separator is any number of non-digits
    (\d{3})     # trunk is 3 digits (e.g. '555')
    \D*         # optional separator
    (\d{4})     # rest of number is 4 digits (e.g. '1212')
    \D*         # optional separator
    (\d*)       # extension is optional and can be any number of digits
    $           # end of string
    ''', re.VERBOSE)

phone_pattern.search('800-555-1212')
phone_pattern.search('work 1-(800) 555.1212 #1234').groups()


#%% Also: simulating 'scanf' and 'sscanf' in Python (because there aren't any).
#   Regular expressions can serve the same purpose, and are more powerful.
#
# E.g., to extract both filename and numbers from the following input string
#     /usr/sbin/sendmail - 0 errors, 4 warnings
# one could use a scanf/sscanf format such as
#     "%s - %d errors, %d warnings"
# The equivalent regular expression would be
#     (\S+) - (\d+) errors, (\d+) warnings

# In simple cases we can use zip and list comprehensions, e.g.:
input_str = '1 3.0 false hello'
[t(s) for t,s in zip((int,float,bool,str), input_str.split())]

# but for more complex cases we need regular expressions:
input_str2 = '1:3.0 false,hello'
[t(s) for t,s in zip((int,float,bool,str),
 re.search('^(\d+):([\d.]+) (\w+),(\w+)$', input_str2).groups())]



##
##  END
##
