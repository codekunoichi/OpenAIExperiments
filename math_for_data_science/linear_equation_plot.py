"""
Linear equation plot.
"""
from sympy import *

# Shows linear plot
x = symbols('x')
f = 2*x + 1
p = plot(f, show=False)  # Use show=False to prevent immediate display

# since I am in GitHub codespaces, the display was not working, 
# so saving the plot image is working
p.save('plot.png')  # Save the plot as a PNG file
