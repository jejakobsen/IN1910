"""
In this exercise, we will build on the example given
in the lectures of implementing 2nd degree polynomials
as objects of a custom defined class. A general 2nd
degree polynomial, aka, quadratic function, can be written
as: $$f(x) = a_2x^2 + a_1x + a_0,$$ where the coefficients,
$a_2$, $a_1$, and $a_0$ uniquely defines the polynomial.
"""
import numpy as np
import matplotlib.pyplot as plt

class Quadratic:
    def __init__(self,a_2,a_1,a_0):
        self.coefficients = a_2, a_1, a_0

    def __call__(self,x):
        a_2, a_1, a_0 = self.coefficients
        return a_2*x**2 + a_1*x + a_0

    def __str__(self):
        a_2, a_1, a_0 = self.coefficients
        return('{}*x**2+({})*x+({})'.format(a_2,a_1,a_0))

    def __add__(self,other):
        a_2, a_1, a_0 = self.coefficients 
        b_2, b_1, b_0 = other.coefficients
        c_2 = a_2 + b_2; c_1 = a_1 + b_1; c_0 = a_0 + b_0
        return Quadratic(c_2,c_1,c_0) 

    def roots(self):
        a,b,c = self.coefficients
        x1 = (-b+np.sqrt((b)**2-4*a*c))/(2*a)
        x2 = (-b-np.sqrt((b)**2-4*a*c))/(2*a)
        return x1,x2

    def intersect(self,other):
        a_2, a_1, a_0 = self.coefficients 
        b_2, b_1, b_0 = other.coefficients
        intersection = Quadratic((a_2-b_2),(a_1-b_1),(a_0-b_0))
        x1, x2 = intersection.roots()
        return x1,x2


# a) created the class and added __init__ and __call__
f = Quadratic(1, -2, 1)
x = np.linspace(-5, 5, 101)
plt.plot(x, f(x))
plt.show()

# b) added __str__
print(f)

# c) added __add__
g = Quadratic(-1,6,-3)
h = f + g
print(h)
x = np.linspace(-5, 5, 101)
plt.plot(x, h(x))
plt.show()

# d) added roots
a = Quadratic(2,-2,2) ;b = Quadratic(1,-2,1); c = Quadratic(1,-3,2)
print(a.roots()); print(b.roots()); print(c.roots())

# e) added intersect
i = Quadratic(1, -2, 1)
j = Quadratic(2, 3, -2)
x = np.linspace(-6,5,101)
print(i.intersect(j))
x1,x2 = i.intersect(j)
plt.plot(x,i(x))
plt.plot(x,j(x))
plt.plot(x1,i(x1),'ro')
plt.plot(x2,j(x2),'ro')
plt.show()

"""
C:\\Users\\jensj\\OneDrive\\Skrivebord\\IN1910\\week2>python e1.py
1*x**2+(-2)*x+(1)
0*x**2+(4)*x+(-2)
(nan, nan)
(1.0, 1.0)
(2.0, 1.0)
(-5.541381265149109, 0.5413812651491097)
"""