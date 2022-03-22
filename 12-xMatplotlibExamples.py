###############################################################################
##
##  PYTHON MATPLOTLIB DEMO -- Copyright © 2013-2021 Michel Pasquier
##


## This demo using MatplotLib is part of section 12 (Python Graphics and GUI).
## While the code and examples in all the other sections only require Python,
## this file needs the numpy and matplotlib modules to be installed.
## If not available, all resulting plots can be found (for convenience) in
## the PDF file: 12-xMatplotlibExamples-figs.pdf
##
## These examples are borrowed or adapted from the MatplotLib online tutorial
## latest version is always @ https://matplotlib.org/tutorials/index.html
## and https://matplotlib.org/tutorials/introductory/sample_plots.html


import numpy as np
import matplotlib.pyplot as plt


#%% Plot Y axis values given as a single list/array, with the X axis values
#   automatically generated (starting at 0 i.e., [0,1,2,3])

plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()                          # 12-xMatplotlibExamples-figs: 01


#%% Plot X versus Y, given as 2 lists

plt.plot([1,2,3,4], [1,4,9,16])
plt.show()


#%% Plot specifying an (optional) format string (using Matlab notation).
#   Default is 'b-' i.e., a solid blue line; 'ro' means red circles.
# axis() specifies the viewport of the axes: [xmin, xmax, ymin, ymax]

plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()                          # 12-xMatplotlibExamples-figs: 02


#%% Use numpy arrays e.g., evenly sampled time at 200ms intervals.
#   Plot using red dashes, blue squares, and green triangles.

t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()                          # 12-xMatplotlibExamples-figs: 03


#%% "Mexican hat" - simple 2D version

from scipy import signal

points = 100
a = 4.0
vec2 = signal.ricker(points, a)
print(len(vec2))
100
plt.plot(vec2)
plt.show()


#%% Working with multiple figures and axes: script to create two subplots

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()                          # 12-xMatplotlibExamples-figs: 04


#%% Working with text: plot title, axis labels, arbitrary text

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# Histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)

plt.title('Histogram of IQ', fontsize=14, color='red')
plt.xlabel('Smarts')
plt.ylabel('Probability')

# Using mathematical expressions in text, as TeX equations (e.g., sigma)
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()                          # 12-xMatplotlibExamples-figs: 05


#%% Annotating text

ax = plt.subplot(111)
t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

# Specify label, location being annotated, location of the label (both
# are x,y tuples), and pointing arrow.
plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05),)
plt.ylim(-2,2)
plt.show()                          # 12-xMatplotlibExamples-figs: 06


###
###  More Matplotlib examples
###  @ http://matplotlib.org/1.3.1/gallery.html
###


#%% Horizontal bar chart demo

people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

plt.barh(y_pos, performance, xerr=error, align='center', alpha=0.4)
plt.yticks(y_pos, people)
plt.xlabel('Performance')
plt.title('How fast do you want to go today?')
plt.show()                          # 12-xMatplotlibExamples-figs: 07


#%% Table demo

data = [[ 66386, 174296,  75131, 577908,  32015],
        [ 58230, 381139,  78045,  99308, 160454],
        [ 89135,  80552, 152558, 497981, 603535],
        [ 78415,  81858, 150656, 193263,  69638],
        [139361, 331509, 343164, 781380,  52269]]

columns = ('Freeze', 'Wind', 'Flood', 'Quake', 'Hail')
rows = ['%d year' % x for x in (100, 50, 20, 10, 5)]

values = np.arange(0, 2500, 500)
value_increment = 1000

# Get some pastel shades for the colors
colors = plt.cm.BuPu(np.linspace(0, 0.5, len(rows)))
n_rows = len(data)

index = np.arange(len(columns)) + 0.3
bar_width = 0.4

# Initialize the vertical-offset for the stacked bar chart
y_offset = np.zeros(len(columns))

# Plot bars and create text labels for the table
cell_text = []
for row in range(n_rows):
    plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
    y_offset = y_offset + data[row]
    cell_text.append(['%1.1f' % (x / 1000.0) for x in y_offset])

# Reverse colors and text labels to display the last value at the top.
colors = colors[::-1]
cell_text.reverse()

# Add a table at the bottom of the axes
the_table = plt.table(cellText=cell_text,
                      rowLabels=rows,
                      rowColours=colors,
                      colLabels=columns,
                      loc='bottom')

# Adjust layout to make room for the table:
plt.subplots_adjust(left=0.2, bottom=0.2)

plt.ylabel("Loss in ${0}'s".format(value_increment))
plt.yticks(values * value_increment, ['%d' % val for val in values])
plt.xticks([])
plt.title('Loss by Disaster')

plt.show()


#%% Scatter plot demo

N = 50
x, y = np.random.rand(N), np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radiuses
plt.scatter(x, y, s=area, alpha=0.5)
plt.show()                          # 12-xMatplotlibExamples-figs: 08


#%% Scatter plot demo 2

import numpy as np
np.random.seed(19680801)
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
for color in ['tab:blue', 'tab:orange', 'tab:green']:
    n = 750
    x, y = np.random.rand(2, n)
    scale = 200.0 * np.random.rand(n)
    ax.scatter(x, y, c=color, s=scale, label=color,
               alpha=0.3, edgecolors='none')

ax.legend()
ax.grid(True)

plt.show()


#%% Demo of the "streamplot" function -- A streamplot, or streamline plot,
#   is used to display 2D vector fields. This example shows a few features
# of the stream plot function i.e., varying the color along a streamline,
# the density of streamlines, and the line width along a stream line.

Y, X = np.mgrid[-3:3:100j, -3:3:100j]
U, V = -1 - X**2 + Y, 1 + X - Y**2
speed = np.sqrt(U*U + V*V)
plt.streamplot(X, Y, U, V, color=U, linewidth=2, cmap=plt.cm.autumn)
plt.colorbar()
#f, (ax1, ax2) = plt.subplots(ncols=2)
#ax1.streamplot(X, Y, U, V, density=[0.5, 1])
#lw = 5*speed/speed.max()
#ax2.streamplot(X, Y, U, V, density=0.6, color='k', linewidth=lw)
plt.show()                          # 12-xMatplotlibExamples-figs: 09


#%% Demo of a basic pie chart, plus a few additional features: slice labels,
#   auto-labeling percentage, offsetting a slice with "explode", drop-shadow,
# and custom start angle.
# Note about the custom start angle: The default "startangle" is 0, which
# would start the "Frogs" slice on the positive x-axis. This example sets
# "startangle = 90" such that everything is rotated counter-clockwise by 90
# degrees, and the frog slice starts on the positive y-axis.

# slices will be ordered and plotted counter-clockwise.
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
explode = (0, 0.1, 0, 0) # only "explode" the 2nd slice ('Hogs')
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)

# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
plt.show()                          # 12-xMatplotlibExamples-figs: 10


#%% Demo of bar plot on a polar axis

N = 20
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)
ax = plt.subplot(111, polar=True)
bars = ax.bar(theta, radii, width=width, bottom=0.0)
for r, bar in zip(radii, bars): # use custom colors and opacity
    bar.set_facecolor(plt.cm.jet(r / 10.))
    bar.set_alpha(0.5)
plt.show()                          # 12-xMatplotlibExamples-figs: 11


#%% Shaded relief plots demo (like Mathematica)
#   cf. http://reference.wolfram.com/mathematica/ref/ReliefPlot.html

from matplotlib.colors import LightSource

X,Y = np.mgrid[-5:5:0.05,-5:5:0.05]
Z = np.sqrt(X**2+Y**2)+np.sin(X**2+Y**2)
ls = LightSource(azdeg=0,altdeg=65) # create light source object
rgb = ls.shade(Z,plt.cm.copper)     # shade data creating an RGB array
plt.figure(figsize=(12,5))          # plot un-shaded and shaded images
plt.subplot(121)
plt.imshow(Z,cmap=plt.cm.copper)
plt.title('imshow')
plt.xticks([]); plt.yticks([])
plt.subplot(122)
plt.imshow(rgb)
plt.title('imshow with shading')
plt.xticks([]); plt.yticks([])
plt.show()                          # 12-xMatplotlibExamples-figs: 12


#%% Pylab example: fill spiral

from pylab import arange, pi, cos, sin, exp, concatenate, fill, show

theta = arange(0,8*pi,0.1)
a, b = 1, 0.2

for dt in arange( 0,2*pi,pi/2.0 ):
    x = a*cos( theta+dt )*exp( b*theta )
    y = a*sin( theta+dt )*exp( b*theta )
    dt = dt+pi/4.0
    x2 = a*cos( theta+dt )*exp( b*theta )
    y2 = a*sin( theta+dt )*exp( b*theta )
    xf = concatenate( (x,x2[::-1]) )
    yf = concatenate( (y,y2[::-1]) )
    p1 = fill( xf,yf )

show()                              # 12-xMatplotlibExamples-figs: 13


#%% Filled surface demo, using the (recursive) Koch snowflake

def koch_snowflake(order, scale=10):
    '''
    Return two lists x, y of point coordinates of the Koch snowflake.

    Arguments
    ---------
    order : int
        The recursion depth.
    scale : float
        The extent of the snowflake (edge length of the base triangle).
    '''
    def _koch_snowflake_complex(order):
        if order == 0:
            # initial triangle
            angles = np.array([0, 120, 240]) + 90
            return scale / np.sqrt(3) * np.exp(np.deg2rad(angles) * 1j)
        else:
            ZR = 0.5 - 0.5j * np.sqrt(3) / 3

            p1 = _koch_snowflake_complex(order - 1)  # start points
            p2 = np.roll(p1, shift=-1)  # end points
            dp = p2 - p1  # connection vectors

            new_points = np.empty(len(p1) * 4, dtype=np.complex128)
            new_points[::4] = p1
            new_points[1::4] = p1 + dp / 3
            new_points[2::4] = p1 + dp * ZR
            new_points[3::4] = p1 + dp / 3 * 2
            return new_points

    points = _koch_snowflake_complex(order)
    x, y = points.real, points.imag
    return x, y

x, y = koch_snowflake(order=5)
plt.figure(figsize=(8, 8))
plt.axis('equal')
plt.fill(x, y)
plt.show()


#%% Mandelbrot fractal set using shaded and power normalized rendering

import numpy as np

def mandelbrot_set(xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon=2.0):
    X = np.linspace(xmin, xmax, xn).astype(np.float32)
    Y = np.linspace(ymin, ymax, yn).astype(np.float32)
    C = X + Y[:, None] * 1j
    N = np.zeros_like(C, dtype=int)
    Z = np.zeros_like(C)
    for n in range(maxiter):
        I = abs(Z) < horizon
        N[I] = n
        Z[I] = Z[I]**2 + C[I]
    N[N == maxiter-1] = 0
    return Z, N

import time
import matplotlib
from matplotlib import colors
import matplotlib.pyplot as plt

xmin, xmax, xn = -2.25, +0.75, 3000 // 2
ymin, ymax, yn = -1.25, +1.25, 2500 // 2
maxiter = 200
horizon = 2.0 ** 40
log_horizon = np.log2(np.log(horizon))
Z, N = mandelbrot_set(xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon)

# Normalized recount as explained in:
# https://linas.org/art-gallery/escape/smooth.html

# This line will generate warnings for null values but it is faster to
# process them afterwards using the nan_to_num
with np.errstate(invalid='ignore'):
    M = np.nan_to_num(N + 1 - np.log2(np.log(abs(Z))) + log_horizon)

dpi = 72
width = 10
height = 10*yn/xn
fig = plt.figure(figsize=(width, height), dpi=dpi)
ax = fig.add_axes([0, 0, 1, 1], frameon=False, aspect=1)

# Shaded rendering
light = colors.LightSource(azdeg=315, altdeg=10)
M = light.shade(M, cmap=plt.cm.hot, vert_exag=1.5,
                norm=colors.PowerNorm(0.3), blend_mode='hsv')
ax.imshow(M, extent=[xmin, xmax, ymin, ymax], interpolation='bicubic')
ax.set_xticks([])
ax.set_yticks([])

# Some advertisement for matplotlib
year = time.strftime('%Y')
text = ('The Mandelbrot fractal set\n'
        'Rendered with matplotlib %s, %s - https://matplotlib.org'
        % (matplotlib.__version__, year))
ax.text(xmin+.025, ymin+.025, text, color='white', fontsize=12, alpha=0.5)

plt.show()


#%% 3D surface demo

from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()                          # 12-xMatplotlibExamples-figs: 14


#%% 3D contour with 2D projections demo

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

fig = plt.figure()
ax = fig.gca(projection='3d')
X, Y, Z = axes3d.get_test_data(0.05)
ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)
cset = ax.contourf(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
cset = ax.contourf(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
cset = ax.contourf(X, Y, Z, zdir='y', offset=40, cmap=cm.coolwarm)
ax.set_xlabel('X')
ax.set_xlim(-40, 40)
ax.set_ylabel('Y')
ax.set_ylim(-40, 40)
ax.set_zlabel('Z')
ax.set_zlim(-100, 100)
plt.show()                          # 12-xMatplotlibExamples-figs: 15


#%% This demo shows how to create an XKCD-like plot. Example based on
#   "The Data So Far" from XKCD by Randall Munroe @ https://xkcd.com/373/
# See: http://jakevdp.github.io/blog/2013/07/10/XKCD-plots-in-matplotlib/

with plt.xkcd():
    fig = plt.figure()
    ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
    ax.bar([0, 1], [0, 100], 0.25)
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['CONFIRMED BY\nEXPERIMENT', 'REFUTED BY\nEXPERIMENT'])
    ax.set_xlim([-0.5, 1.5])
    ax.set_yticks([])
    ax.set_ylim([0, 110])
    ax.set_title('CLAIMS OF SUPERNATURAL POWERS')
    fig.text(0.5, 0.0,
             '"The Data So Far" from xkcd by Randall Munroe',
             ha='center')

plt.show()


#%% Creating a timeline with lines, dates, and text
#   Example of a (not so) simple timeline using the dates for recent releases
#   of Matplotlib (pulling first the data from GitHub).

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime

try:
    # Try to fetch a list of Matplotlib releases and their dates
    # from https://api.github.com/repos/matplotlib/matplotlib/releases
    import urllib.request
    import json

    url = 'https://api.github.com/repos/matplotlib/matplotlib/releases'
    url += '?per_page=100'
    data = json.loads(urllib.request.urlopen(url, timeout=.4).read().decode())

    dates = []
    names = []
    for item in data:
        if 'rc' not in item['tag_name'] and 'b' not in item['tag_name']:
            dates.append(item['published_at'].split('T')[0])
            names.append(item['tag_name'])
    # Convert date strings (e.g. 2014-10-18) to datetime
    dates = [datetime.strptime(d, '%Y-%m-%d') for d in dates]

except Exception:
    # In case the above fails, e.g. because of missing internet connection
    # use the following lists as fallback.
    names = ['v2.2.4', 'v3.0.3', 'v3.0.2', 'v3.0.1', 'v3.0.0', 'v2.2.3',
             'v2.2.2', 'v2.2.1', 'v2.2.0', 'v2.1.2', 'v2.1.1', 'v2.1.0',
             'v2.0.2', 'v2.0.1', 'v2.0.0', 'v1.5.3', 'v1.5.2', 'v1.5.1',
             'v1.5.0', 'v1.4.3', 'v1.4.2', 'v1.4.1', 'v1.4.0']

    dates = ['2019-02-26', '2019-02-26', '2018-11-10', '2018-11-10',
             '2018-09-18', '2018-08-10', '2018-03-17', '2018-03-16',
             '2018-03-06', '2018-01-18', '2017-12-10', '2017-10-07',
             '2017-05-10', '2017-05-02', '2017-01-17', '2016-09-09',
             '2016-07-03', '2016-01-10', '2015-10-29', '2015-02-16',
             '2014-10-26', '2014-10-18', '2014-08-26']

    # Convert date strings (e.g. 2014-10-18) to datetime
    dates = [datetime.strptime(d, '%Y-%m-%d') for d in dates]

# Next, we'll create a stem plot with some variation in levels as to
# distinguish even close-by events. We add markers on the baseline for visual
# emphasis on the one-dimensional nature of the time line.
# For each event, we add a text label via `~.Axes.annotate`, which is offset
# in units of points from the tip of the event line.
# Note that Matplotlib will automatically plot datetime inputs.

# Choose some nice levels
levels = np.tile([-5, 5, -3, 3, -1, 1],
                 int(np.ceil(len(dates)/6)))[:len(dates)]

# Create figure and plot a stem plot with the date
fig, ax = plt.subplots(figsize=(8.8, 4), constrained_layout=True)
ax.set(title='Matplotlib release dates')

ax.vlines(dates, 0, levels, color='tab:red')  # The vertical stems.
ax.plot(dates, np.zeros_like(dates), '-o',
        color='k', markerfacecolor='w')  # Baseline and markers on it.

# annotate lines
for d, l, r in zip(dates, levels, names):
    ax.annotate(r, xy=(d, l),
                xytext=(-3, np.sign(l)*3), textcoords='offset points',
                horizontalalignment='right',
                verticalalignment='bottom' if l > 0 else 'top')

# format xaxis with 4 month intervals
ax.get_xaxis().set_major_locator(mdates.MonthLocator(interval=4))
ax.get_xaxis().set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.setp(ax.get_xticklabels(), rotation=30, ha='right')

# remove y axis and spines
ax.get_yaxis().set_visible(False)
for spine in ['left', 'top', 'right']:
    ax.spines[spine].set_visible(False)

ax.margins(y=0.1)
plt.show()


#%% Dolphins demo from MatplotLib
#   This example shows how to draw, and manipulate shapes given vertices
# and nodes using the `~.path.Path`, `~.patches.PathPatch` and
# `~matplotlib.transforms` classes.

import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, PathPatch
from matplotlib.path import Path
from matplotlib.transforms import Affine2D
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

r = np.random.rand(50)
t = np.random.rand(50) * np.pi * 2.0
x = r * np.cos(t)
y = r * np.sin(t)

fig, ax = plt.subplots(figsize=(6, 6))
circle = Circle((0, 0), 1, facecolor='none',
                edgecolor=(0, 0.8, 0.8), linewidth=3, alpha=0.5)
ax.add_patch(circle)

im = plt.imshow(np.random.random((100, 100)),
                origin='lower', cmap=cm.winter,
                interpolation='spline36',
                extent=([-1, 1, -1, 1]))
im.set_clip_path(circle)

plt.plot(x, y, 'o', color=(0.9, 0.9, 1.0), alpha=0.8)

dolphin = '''
M -0.59739425,160.18173 C -0.62740401,160.18885 -0.57867129,160.11183
-0.57867129,160.11183 C -0.57867129,160.11183 -0.5438361,159.89315
-0.39514638,159.81496 C -0.24645668,159.73678 -0.18316813,159.71981
-0.18316813,159.71981 C -0.18316813,159.71981 -0.10322971,159.58124
-0.057804323,159.58725 C -0.029723983,159.58913 -0.061841603,159.60356
-0.071265813,159.62815 C -0.080250183,159.65325 -0.082918513,159.70554
-0.061841203,159.71248 C -0.040763903,159.7194 -0.0066711426,159.71091
0.077336307,159.73612 C 0.16879567,159.76377 0.28380306,159.86448
0.31516668,159.91533 C 0.3465303,159.96618 0.5011127,160.1771
0.5011127,160.1771 C 0.63668998,160.19238 0.67763022,160.31259
0.66556395,160.32668 C 0.65339985,160.34212 0.66350443,160.33642
0.64907098,160.33088 C 0.63463742,160.32533 0.61309688,160.297
0.5789627,160.29339 C 0.54348657,160.28968 0.52329693,160.27674
0.50728856,160.27737 C 0.49060916,160.27795 0.48965803,160.31565
0.46114204,160.33673 C 0.43329696,160.35786 0.4570711,160.39871
0.43309565,160.40685 C 0.4105108,160.41442 0.39416631,160.33027
0.3954995,160.2935 C 0.39683269,160.25672 0.43807996,160.21522
0.44567915,160.19734 C 0.45327833,160.17946 0.27946869,159.9424
-0.061852613,159.99845 C -0.083965233,160.0427 -0.26176109,160.06683
-0.26176109,160.06683 C -0.30127962,160.07028 -0.21167141,160.09731
-0.24649368,160.1011 C -0.32642366,160.11569 -0.34521187,160.06895
-0.40622293,160.0819 C -0.467234,160.09485 -0.56738444,160.17461
-0.59739425,160.18173
'''

vertices = []
codes = []
parts = dolphin.split()
i = 0
code_map = {
    'M': Path.MOVETO,
    'C': Path.CURVE4,
    'L': Path.LINETO,
}

while i < len(parts):
    path_code = code_map[parts[i]]
    npoints = Path.NUM_VERTICES_FOR_CODE[path_code]
    codes.extend([path_code] * npoints)
    vertices.extend([[*map(float, y.split(','))]
                     for y in parts[i + 1:][:npoints]])
    i += npoints + 1
vertices = np.array(vertices)
vertices[:, 1] -= 160

dolphin_path = Path(vertices, codes)
dolphin_patch = PathPatch(dolphin_path, facecolor=(0.6, 0.6, 0.6),
                          edgecolor=(0.0, 0.0, 0.0))
ax.add_patch(dolphin_patch)

vertices = Affine2D().rotate_deg(60).transform(vertices)
dolphin_path2 = Path(vertices, codes)
dolphin_patch2 = PathPatch(dolphin_path2, facecolor=(0.5, 0.5, 0.5),
                           edgecolor=(0.0, 0.0, 0.0))
ax.add_patch(dolphin_patch2)

plt.show()


##
##  END
##
