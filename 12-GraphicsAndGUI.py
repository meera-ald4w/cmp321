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
##  12. Graphics and GUI Extensions: Turtle graphics, Tkinter GUI library,
##                          others e.g. wxPython, PyGUI, pyQT, matplotlib...
##  13. Threads and Concurrency
##  14. Miscellanies and References
##  15. Scientific Python
##



###############################################################################
###
###   12. GRAPHICS AND GUI
###



################################
##
##  TURTLE GRAPHICS
##


#%% Turtle is graphic library for teaching programming and using graphics
#   (originated with Logo, now available in many programming languages).
import turtle as tt

# Examples of turtle drawing
def turtle_show(speed=1):
    tt.shape('turtle')
    tt.speed(speed)
    tt.color('blue')
    for count in range(6):
        tt.forward(100)
        tt.left(60)
    tt.exitonclick()

#!! 2016-09 Python 3.5.x bug, documented @ https://bugs.python.org/issue21823
# Every turtle demo in this file works fine, but right now running the same
# demo a second time raises a turtle.Terminator exception; third time works
# fine again... It's a cosmetic bug only, but annoying still. One fix is to
# catch the exception of course e.g., as follows:
def turtle_show_fixed(speed=1):
    try:
        tt.shape('turtle')
        tt.speed(speed)
        tt.color('blue')
        for count in range(6):
            tt.forward(100)
            tt.left(60)
        tt.exitonclick()
    except tt.Terminator:
        print('Python 3.5 bug 21823: turtle.Terminator exception is raised\n',
              'Just ignore the issue and run your code again as normal...')

#%% Some classic examples
def coords_system():
    tt.hideturtle()
    tt.speed(0)
    tt.penup() ; tt.goto(-10,0)
    tt.pendown()
    tt.color('red') ; tt.write('O')
    tt.color('blue') ; tt.goto(200,0) ; tt.write('X')
    tt.penup() ; tt.goto(0,-10)
    tt.pendown()
    tt.color('green') ; tt.goto(0,200) ; tt.write('Y')
    tt.exitonclick()

def turtle_star(speed=3,hidden=False):
    tt.speed(speed)
    if hidden: tt.hideturtle()
    for x in range(1,19):
        tt.forward(100)
        if x % 2 == 0:
            tt.left(175)
        else:
            tt.left(225)
    tt.exitonclick()

def turtle_spiralstar(speed=5,size=2):
    tt.speed(speed)
    tt.hideturtle()
    tt.pensize(size)
    for i in range(20):
        tt.forward(i * 10)
        tt.right(144)
    tt.exitonclick()


#%% More examples
def turtle_spiro():
    tt.speed(20)
    tt.hideturtle()
    tt.pencolor('blue')
    for i in range(50):
        tt.forward(100)
        tt.left(123)
    tt.pencolor('red')
    for i in range(50):
        tt.forward(200)
        tt.left(123)
    tt.exitonclick()

def turtle_moire(speed=20):
    tt.speed(speed)
    tt.hideturtle()
    for i in range(180):
        tt.forward(100)
        tt.right(30)
        tt.forward(20)
        tt.left(60)
        tt.forward(50)
        tt.right(30)
        tt.penup()
        tt.setposition(0, 0)
        tt.pendown()
        tt.right(2)
    tt.exitonclick()


#%% Example of Dragon fractals
def turtle_dragon(level=6,color='red',hidden=True):

    def dragon(level=4, size=200, zig=tt.right, zag=tt.left):
        if level <= 0:
            tt.forward(size)
            return
        size /= 1.41421
        zig(45)
        dragon(level-1, size, tt.right, tt.left)
        zag(90)
        dragon(level-1, size, tt.left, tt.right)
        zig(45)

    tt.color(color)
    tt.speed(0)
    tt.hideturtle()
    dragon(level)
    tt.exitonclick()

#todo - Fractal tree example [check! and update other demos?]
def fractal_tree():

    def tree(branchLen,t):
        if branchLen > 5:
            t.forward(branchLen)
            t.right(20)
            tree(branchLen-15,t)
            t.left(40)
            tree(branchLen-15,t)
            t.right(20)
            t.backward(branchLen)

    t = tt.Turtle()
    screen = tt.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color('green')
    tree(75,t)
    screen.exitonclick()

# See also https://www.cs.swarthmore.edu/~knerr/cs21/s15/Labs/lab10.php
# and https://stackoverflow.com/questions/46565729/turtle-graphics-with-recursion
# https://www.google.ae/search?ei=sRbSWuqzE4XjUeKei5AM&q=recursive+pattern+programming

#%%
 Hilbert curve [2DO: check! and update other demos?]
def hilbert_curve(depth=1):

    def hilbert_draw(n, turtle, angle=90):
        if n <= 0: return
        turtle.left(angle)
        hilbert_draw(n-1, turtle, -angle)
        turtle.forward(1)
        turtle.right(angle)
        hilbert_draw(n-1, turtle, angle)
        turtle.forward(1)
        hilbert_draw(n-1, turtle, angle)
        turtle.right(angle)
        turtle.forward(1)
        hilbert_draw(n-1, turtle, -angle)
        turtle.left(angle)

    size = 2**depth
    screen = tt.Screen()
    screen.setworldcoordinates(0, 0, size, size)
    yertle = tt.Turtle('turtle')
    yertle.speed('fastest')
    yertle.penup()
    yertle.goto(0.5, 0.5)
    yertle.pendown()
    hilbert_draw(depth, yertle)
    yertle.hideturtle()
    screen.exitonclick()


#%% Turtle graphics example
def turtle_graphics1():
    def cshape(ne, sz):
        for i in range(ne):
            tt.right(360./ne)
            for i in range(ne):
                tt.right(360./ne)
                tt.forward(sz)
    tt.speed(0)
    tt.hideturtle()
    tt.bgcolor('black')
    tt.pencolor('red')
    tt.pensize(3)
    tt.tracer(36,0)
    cshape(36,20)
    tt.exitonclick()

def turtle_illusion():
    tt.mode('logo')
    tt.shape('triangle')
    # determine shriking factor and angle of rotation
    tt.speed(1)
    tt.forward(100)
    tt.right(150)
    tt.forward(20)
    tt.setheading(tt.towards(0,0))
    tt.right(180)
    # now the turtle is at the tip of the inscribed triangle
    # and heading in direction of its axis
    f = tt.distance(0,0)/100     # 0.83282...
    phi = tt.heading()           # 6.89636...
    tt.back(100*f)
    tt.left(phi)
    #time.sleep(2)
    tt.clear()
    # stamp nested triangles
    s, c = 20, 1
    for i in range(20):
        tt.shapesize(s)
        tt.fillcolor(c, 0.5, 1-c)
        tt.stamp()
        s *= f
        c *= f
        tt.right(phi)


#%% Turtle function plot example
def turtle_plot(N=80):

    def line(x1, y1, x2, y2):
        tt.penup()
        tt.goto(x1, y1)
        tt.pendown()
        tt.goto(x2, y2)

    def plot(func, start, color):
        tt.pencolor(color)
        x = start
        tt.penup()
        tt.goto(0, x)
        tt.pendown()
        tt.dot(5)
        for i in range(N):
            x=func(x)
            tt.goto(i+1,x)
            tt.dot(5)

    tt.setworldcoordinates(-1.0,-0.1, N+1, 1.1)
    tt.speed(0)
    tt.hideturtle()
    tt.write('Python Turtle Plot Demo',
             align='left', font=('Courier',14,'bold'))
    line(-1, 0, N+1, 0)
    line(0, -0.1, 0, 1.1)
    plot(lambda x: 3.9*x*(1-x),   0.35, 'blue')
    plot(lambda x: 3.9*(x-x**2),  0.35, 'green')
    plot(lambda x: 3.9*x-3.9*x*x, 0.35, 'red')
    # now zoom in!
    for s in range(100):
        tt.setworldcoordinates(0.5*s,-0.1, N+1, 1.1)
    tt.exitonclick()



################################
##
##  TKINTER GUI PROGRAMMING
##


#%% TKinter is a simple built-in GUI toolkit for Python (it relies on the well-
# known TK library, which provides a GUI layer to many programming languages).
# Note that IDLE is coded in 100% pure Python, using the tkinter GUI toolkit.

import tkinter as tk
#from tkinter import font

# Run the demos hereafter as: tk_demo(1) ... tk_demo(N)
def tk_demo(num = 0):
    demoApp=eval('tk_app' + str(num))   # build function name
    demoApp().mainloop()                # then run it

# "Hello, world" label demo
class tk_app0(tk.Frame):
    def __init__(self):
        root = tk.Tk()
        tk.Frame.__init__(self,root)
        tk.Label(root, text='Hello, world!').pack()

# Simple alert label demo
class tk_app1(tk.Frame):
    def __init__(self):
        root = tk.Tk()
        af = tk.font.Font(family='Helvetica', size=48, weight='bold')
        tk.Frame.__init__(self,root)
        tk.Label(root, text='Attention!', font=af, fg='red').grid()

# Button and callback demo
class tk_app2(tk.Frame):
    def __init__(self):
        root = tk.Tk()
        tk.Frame.__init__(self,root)
        tk.Button(root, text='Click me', command=self.say_hello).pack()
        # all widgets are inserted in the graphic hierarchy -> no GC
        hb = tk.Button(root, text='Hi!', command=lambda: print('Hi!'))
        hb.pack(side='left')
        qb = tk.Button(root, text='Quit', command=root.destroy)
        qb.pack(side='right')
    def say_hello(self):
        print('Hello, everyone!')


#%% Counter demo w/ dynamic label and button
class tk_app3(tk.Frame):
    counter = 0
    def counter_label(label):
        def count():
            tk_app3.counter += 1
            label.config(text=str(tk_app3.counter))
            label.after(1000, count)
        count()
    def __init__(self):
        root = tk.Tk()
        tk.Frame.__init__(self,root)
        root.title('Counting Seconds')
        label = tk.Label(root, fg='blue')
        label.pack()
        tk_app3.counter_label(label)
        button = tk.Button(root, text='Stop', width=20, command=root.destroy)
        button.pack()

# Mouse event binding demo
class tk_app4(tk.Frame):
    def __init__(self):
        root = tk.Tk()
        tk.Frame.__init__(self,root)
        l=tk.Label(root, text='Starting - please move the mouse')
        l.grid()
        l.bind('<Enter>', lambda e: l.configure(text='Mouse inside'))
        l.bind('<Leave>', lambda e: l.configure(text='Mouse outside'))
        l.bind('<1>', lambda e: l.configure(text='Left button clicked '))
        l.bind('<Double-1>', lambda e: l.configure(text='Double clicked'))
        l.bind('<Button2-Motion>', lambda e: l.configure(
            text='Right button dragged to %d,%d' % (e.x, e.y)))

# Feet-meter unit conversion calculator, using a geometry manager
class tk_app5(tk.Frame):
    def __init__(self):
        root = tk.Tk()
        root.title('Feet to Meters')
        tk.Frame.__init__(self,root)
        tk.Button(root, text='Calculate',
                  command=self.calculate).grid(row=0,column=0,sticky=tk.W)
        self.feet = tk.StringVar()
        self.feet.set('1')
        feet_entry = tk.Entry(textvariable=self.feet, width=8)
        feet_entry.grid(row=0,column=1,sticky=(tk.W,tk.E))
        feet_entry.bind('<Key-Return>',self.calculate)
        tk.Label(root, text='feet').grid(row=0,column=2,sticky=tk.W)
        tk.Label(root, text='is equivalent to').grid(row=1,column=0,
                                                     sticky=tk.E)
        self.meters = tk.StringVar()
        tk.Label(root, textvariable=self.meters).grid(row=1,column=1,
                                                      sticky=(tk.W,tk.E))
        tk.Label(root, text='meters').grid(row=1,column=2,sticky=tk.W)
    def calculate(self,*args):
        try:
            value = float(self.feet.get())
            self.meters.set(round((3048.0 * value + 0.5)/10000.0,6))
        except ValueError:
            print('Please enter a number and press calculate / return')


#%% Theme selector demo using a Combobox
from tkinter import ttk
import random
class tk_app6(tk.Frame):
    def __init__(self):
        self.root = tk.Tk()
        tk.Frame.__init__(self,self.root)
        self.style = ttk.Style()
        available_themes = self.style.theme_names()
        random_theme = random.choice(available_themes)
        self.style.theme_use(random_theme)
        self.root.title(random_theme)
        frm = ttk.Frame(self.root)
        frm.pack(expand=True, fill='both')
        # create a Combobox with themes to choose from
        self.combo = ttk.Combobox(frm, values=available_themes)
        self.combo.pack(padx=32, pady=8)
        # make the Enter key change the style
        self.combo.bind('<Return>', self.change_style)
        # make a Button to change the style
        button = ttk.Button(frm, text='OK')
        button['command'] = self.change_style
        button.pack(pady=8)
    def change_style(self, event=None):
        '''set the Style to the content of the Combobox'''
        content = self.combo.get()
        try:
            self.style.theme_use(content)
        except tk.TclError as err:
            tk.messagebox.showerror('Error', err)
        else:
            self.root.title(content)

# Simple color chooser demo
from tkinter import colorchooser
class tk_app7(tk.Frame):
    def __init__(self):
        root = tk.Tk()
        tk.Frame.__init__(self,root)
        tk.Button(text='Select Color', command=self.getColor).pack()
    def getColor(self):
        print(colorchooser.askcolor())

# Directory tree view demo
class tk_app8(tk.Frame):
    def __init__(self):
        root = tk.Tk()
        tk.Frame.__init__(self,root)
        tree = ttk.Treeview(root)
        tree['columns']=('size','date')
        tree.column('size', width=100 )
        tree.column('date', width=100)
        tree.heading('size', text='size col')
        tree.heading('date', text='date col')
        tree.insert('', 0, text='some file', values=('123','3/14/15'))
        id2 = tree.insert('', 1, 'dir1', text='First Dir', values=('20','12/25/14'))
        tree.insert(id2, 'end', 'dir2', text='Sub Dir 1', values=('400','12/25/14'))
        # alternatively:
        tree.insert('', 2, 'dir3', text='Second Dir', values=('40','9/5/14'))
        tree.insert('dir3', 2, text='Sub Dir 2',values=('750','9/12/14'))
        tree.pack()

#%% Image viewer demo (only for GIF/PPM -- install PIL for other image types)
from tkinter import PhotoImage
import urllib, urllib.error, urllib.request
class tk_app9(tk.Frame):
    def __init__(self):
        root = tk.Tk()
        tk.Frame.__init__(self,root)
        url = 'https://neteasy.us/img/python-logo.gif'
        try:
            imgdata = urllib.request.urlopen(url).read()
            # note: we need to keep a reference to the image to avoid GC!
            #       (i.e. *in* the object; using a local var will not work)
            self.img = PhotoImage(data=imgdata)
        except urllib.error.URLError:
            print('error: cannot read image from website')
        tk.Label(root, image=self.img).pack()


# Tkinter @ http://www.tkdocs.com/tutorial/index.html
# Thinking Tkinter @ http://thinkingtkinter.sourceforge.net/
# Tkinter tour @ http://tkinter.unpythonic.net/wiki/A_tour_of_Tkinter_widgets



################################
##
##  MORE GRAPHICS/GUI MODULES
##

# Other than the built-in TKinter and Turtle (above), many modules exist that
# bind Python to various third-party graphic libraries and tookits (as such,
# one needs to download and install them first). A non-exhaustive list is:
#
# wxPython: rich, cross-platform GUI toolkit with Python interface
#                                        @ http://wiki.wxpython.org/
# pyQT: very good GUI toolkit for python @ https://wiki.python.org/moin/PyQt
#       w/ excellent, free, old textbook @ http://www.qtrac.eu/pyqtbook.html
# PySide: another Qt binding for Python  @ http://wiki.qt.io/PySide
# PyGTK: another Python GUI library      @ http://www.pygtk.org
# PyOpenGL: support for OpenGL and Togl  @ http://pyopengl.sourceforge.net/
# EasyGUI: very simple GUI programming   @ http://easygui.sourceforge.net
# PyGUI: abstract, cross-platform, pythonic API for GUI development
#       (gotta love the name, really ;)  @ https://github.com/stonewell/pygui
# PyWin32: Python library for interacting with Windows OS
# IronPython: Python for (originally MS') .NET platform
# Pillow and PIL (Python Imaging Library): image processing
# Matplotlib: Python 2D plotting library @ https://matplotlib.org/
#       cf. 12-xMatplotlibExamples.py and 12-xMatplotlibExamples-figs.pdf
# PyQtGraph: graphic library for scientific applications
# VPython: Visual Python for 3D graphic programming @ http://vpython.org/



##
##  END
##
