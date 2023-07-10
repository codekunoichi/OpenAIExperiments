"""
3d plot of a function
"""
from sympy import *
from sympy.plotting import plot3d

x, y = symbols('x y')
f = 2*x + 3*y


p = plot3d(f, show=False)  # Use show=False to prevent immediate display

# since I am in GitHub codespaces, the display was not working, 
# so saving the plot image is working
p.save('plot3d.png')  # Save the plot as a PNG file