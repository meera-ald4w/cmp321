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
##  13. Threads and Concurrency: simple threads, subclassing, timer threads,
##                          more examples, coroutines, asynchronous generators
##  14. Miscellanies and References
##  15. Scientific Python
##



###############################################################################
###
###   13. THREADS AND CONCURRENCY
###



################################
##
##  SIMPLE THREADS
##


# Recall threads are akin to lightweight processes, running within the same
# application, and normally cooperative. These are provided via the threading
# module. Python similarly includes a multiprocessing module that supports
# spawning processes and offers both local and remote concurrency.
import threading
import time
import random


#%% Threads in Python are very similar to that in Java. This example creates
#   a number of threads, sets simpleTask() as their target/run function,
# then start each, which initializes the thread and calls its run method

def ten_little_threads(number = 10):

    def simple_task(thread_id, waiting_time):
        # do something ...
        print(f" thread {thread_id} sleeping ({waiting_time}) ")
        time.sleep(waiting_time)
        print(f" thread {thread_id} awaking ")

    for num in range(number):
        print(f" thread {num} starting ")
        t = threading.Thread(target=simple_task,     # "run" function
                   args=(num, random.randint(1,10))) # and its parameters
        t.start()

#ten_little_threads()


#%% Thread subclass, overrides the run() method instead
class simple_thread(threading.Thread):

    def __init__(self, target=None, args=()):
        threading.Thread.__init__(self, target=target)
        self.args = args
        return

    def run(self):
        # do something ...
        print(f' thread {self.args[0]} sleeping ')
        time.sleep(self.args[1])
        print(f' thread {self.args[0]} awaking ')
        return

def more_little_threads(number = 10):
    for num in range(number):
        print(f' thread {num} starting ')
        t = simple_thread(args=(num, random.randint(1,10)))
        t.start()

#more_little_threads()



################################
##
##  TIMER THREADS
##


#%% Task to be executed twice in parallel
def delayed_task(task_name):
    print('task', task_name, 'working')
    return

def little_timers(sleep_time=4):
    t1 = threading.Timer(2, delayed_task, args=('t1',))
    t2 = threading.Timer(6, delayed_task, args=('t2',))
    print('starting timers')
    t1.start()
    t2.start()
    time.sleep(sleep_time)      # wait before cancelling task #2
    t2.cancel()                 # if sleep_time > 6, task #2 will never run

#little_timers()



################################
##
##  DINING PHILOSOPHERS EXAMPLE
##


#%% 5 philosophers are hungry. They have only 5 forks (or chopsticks ;).
#   However, anyone needs 2 forks (chopsticks) to eat.
# A classic - cf. https://en.wikipedia.org/wiki/Dining_philosophers_problem
# Code adapted from https://rosettacode.org/wiki/Dining_philosophers#Python

class Philosopher(threading.Thread):
    running = True

    def __init__(self, name, forkOnLeft, forkOnRight):
        threading.Thread.__init__(self)
        self.name = name
        self.forkOnLeft = forkOnLeft
        self.forkOnRight = forkOnRight

    def run(self):
        while(self.running):
            # The philosopher is thinking (in reality he's sleeping)
            time.sleep( random.uniform(3,13))
            print(f'{self.name} is hungry.')
            self.dine()

    def dine(self):
        fork1, fork2 = self.forkOnLeft, self.forkOnRight

        while self.running:
            fork1.acquire(True)
            locked = fork2.acquire(False)
            if locked: break
            fork1.release()
            print(f'{self.name} swaps forks')
            fork1, fork2 = fork2, fork1
        else: return

        self.dining()
        fork2.release()
        fork1.release()

    def dining(self):
        print(f'{self.name} starts eating ')
        time.sleep(random.uniform(1,10))
        print(f'{self.name} finishes eating and leaves to think.')

def DiningPhilosophers():
    forks = [threading.Lock() for n in range(5)]
    philosopherNames = ('Aristotle', 'Kant', 'Plato', 'Marx', 'Russel')

    philosophers= [Philosopher(philosopherNames[i], forks[i%5], forks[(i+1)%5]) \
            for i in range(5)]

    random.seed(507129)
    Philosopher.running = True
    for p in philosophers: p.start()
    time.sleep(100)
    Philosopher.running = False
    print('Now we are finishing.')

#DiningPhilosophers()



#%% Many good tutorials can be found online, starting with Python's own at
#   https://docs.python.org/3/library/threading.html but also
#   https://realpython.com/intro-to-python-threading/ and more.

# See also: https://jeffknupp.com/blog/2012/03/31/pythons-hardest-problem/
# about the Global Interpreter Lock and using multiple processes, not threads.
# (It's a bit dated, but still of interest. The following point still holds.)

# To quote: Thread based programming is hard. There are no two ways about it.
# Every time one thinks he or she understands everything there is to know about
# how threading works, a new wrinkle is uncovered. A number of high-profile
# language designers and researchers have come out against the threading model
# because it is simply too difficult to get right with any reasonable degree
# of consistency. As anyone who has written a multi-threaded application can
# tell you, both developing and debugging are exponentially more difficult
# compared to a single threaded program. The programmer's mental model, while
# well suited for sequential programs, just doesn't match the parallel
# execution model.

# Which leads to:



################################
##
##  COROUTINES
##


# There are three big problems with threads [http://www.effectivepython.com]
# (1) They require special tools to coordinate with each other safely. This
# makes code that uses threads harder to reason about than procedural, single-
# threaded code. This complexity makes threaded code more difficult to extend
# and maintain over time.
# (2) Threads require a lot of memory, about 8MB per executing thread. On many
# computers that amount of memory doesn't matter for a dozen threads or so.
# But what if you want your program to run tens of thousands of functions
# "simultaneously"? It won't work.
# (3) Threads are costly to start. If you want to constantly be creating new
# concurrent functions and finishing them, the overhead of using threads
# becomes large and slows everything down.

# Python can work around all these issues with coroutines. Coroutines let you
# have many seemingly simultaneous functions in your Python programs. They are
# implemented as an extension to generators. The cost of starting a generator
# coroutine is a function call. Once active, they each use less than 1KB of
# memory until they're exhausted.

# Coroutines work by enabling the code consuming a generator to 'send' a value
# back to the generator function after each 'yield' expression. The generator
# function receives the value passed to the 'send' function as the result of
# the corresponding 'yield' expression...
# (See also section 08. Iterators/Generators.)


#%% Example: A generator coroutine that yields the minimum value it has been
#   sent so far. Here the first, bare 'yield' prepares the coroutine with the
# initial minimum value sent in from the outside. Subsequently, the generator
# will repeatedly yield the new minimum in exchange for the next value.

def minimize():
    current = yield
    while True:
        value = yield current
        current = min(value, current)

# The code consuming the generator can run one step at a time and will output
# the minimum value seen after each input.

it = minimize()
next(it)            			# prime the generator
print(it.send(10))
print(it.send(4))
print(it.send(22))
print(it.send(-1))

# The generator function will seemingly run forever, making forward progress
# with each new call to 'send'. Like threads, coroutines are independent
# functions that consume inputs from their environment and produce resulting
# outputs. The difference is that coroutines pause at each 'yield' expression
# in the generator function and resume after each call to 'send' from the
# outside.

# This behavior allows the code consuming the generator to take action after
# each yield expression in the coroutine. The consuming code can use the
# generator's output values to call other functions and update data structures.
# Most importantly, it can advance other generator functions until their next
# yield expressions. By advancing many separate generators in lockstep, they
# will all seem to be running simultaneously, mimicking the concurrent
# behavior of Python threads.


#%% See about streams and coroutines, and the Produced-Filter-Consumer
#   example at http://wla.berkeley.edu/~cs61a/fa11/lectures/streams.html
# and https://jeffknupp.com/blog/2013/04/07/
#     improve-your-python-yield-and-generators-explained/

def get_data():
    '''Return 3 random integers between 0 and 9'''
    return random.sample(range(10), 3)

def consume():
    '''Displays a running average across lists of integers sent to it'''
    running_sum = 0
    data_items_seen = 0
    while True:
        data = yield
        data_items_seen += len(data)
        running_sum += sum(data)
        print(f'The running average is {running_sum / float(data_items_seen)}')

def produce(consumer):
    '''Produces a set of values and forwards them to the pre-defined consumer function'''
    while True:
        data = get_data()
        print(f'Produced {data}')
        consumer.send(data)
        yield

def producer_consumer_demo():
    consumer = consume()
    consumer.send(None)                     # prime the generator
    producer = produce(consumer)
    for _ in range(10):
        print('Producing...')
        next(producer)

#producer_consumer_demo()



################################
##
##  ASYNCHRONOUS GENERATORS [v3.6]
##


#%% Example - see https://www.python.org/dev/peps/pep-0525/
import asyncio

async def ticker(delay, to):
    '''Yield numbers from 0 to *to* every *delay* seconds.'''
    for i in range(to):
        yield i
        await asyncio.sleep(delay)

async def run():
    async for i in ticker(1, 10):
        print(i)

def async_ticker_demo():
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(run())
    finally:
        loop.close()

#async_ticker_demo()



################################
##
##  ASYNCHRONOUS COMPREHENSIONS [v3.6]
##


# Using async for in list/set/dict comprehensions and generator expressions:
#
# result = [i async for i in aiter() if i % 2]

# In addition, await expressions are supported in all kinds of comprehensions:
#
# result = [await fun() for fun in funcs if await condition()]

# See https://www.python.org/dev/peps/pep-0530



################################
##
##  ASYNCHRONOUS PROGRAMMING [V3.7]
##


# The latest concurrent programming model in Python, which extends and aims at
# replacing generator-based co-routines, is asyncio i.e. asynchronous I/O).

# A good overview article that covers (1) Multiple Processes, (2) Threads,
# (3) Coroutines, and (4) Asynchronous Programming is at
# https://medium.com/velotio-perspectives/
#       an-introduction-to-asynchronous-programming-in-python-af0189a88bbb

# A coroutine is a function with an async definition, which can be called with
# the await statement. It means the program will run up to the await statement,
# call the function, and suspend execution until the function completes, so
# that other coroutines get a chance to run.

# Suspension of execution means that control is returned to the event loop.
# When you use asyncio, an event loop runs all the asynchronous tasks and
# performs network IO and runs sub-processes. Writing and running coroutines
# usually means using tasks, which make it all easier.


#%% Below is the canonical example from the official Python documentation:
#   https://docs.python.org/3/library/asyncio-task.html

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def say_demo():
    task1 = asyncio.create_task( say_after(1, 'hello'))

    task2 = asyncio.create_task( say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take less than 2 seconds)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

#asyncio.run(say_demo())

# note: One can call say_after() directly, as follows. But then the calls are
# made sequentially(!) which defeats the purpose (so it takes 3 seconds now).
async def say_all():
    await say_after(1, 'hello') ; await say_after(2, 'world')
# asyncio.run(say_all())


#%% Another excellent, in-depth tutorial about asyncio is from Real Python
#  again at: https://realpython.com/async-io-python/



##
##  END
##
