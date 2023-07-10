"""
Parabola Plot
"""
from sympy import *

x = symbols('x')
f = x**2 + 1


p = plot(f, show=False)  # Use show=False to prevent immediate display

# since I am in GitHub codespaces, the display was not working, 
# so saving the plot image is working
p.save('parabola_plot.png')  # Save the plot as a PNG file
