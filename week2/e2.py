"""
We want to make a class that represents such a polynomial, and can take any number of coefficients in.
The constructor of such a class could for example take in a list of the coefficients: [a0, a1, ..., aN].
However, this list will always have to be of length $N$, and say we want to specify the polynomial
 $x^{1000} + 1$, it is highly inefficient to pass in such a long list, as most coefficients are actually 0.

A better approach is to use a dictionary, where we use the index as the key and the coefficient as the value.
Doing this, we can then specify only the non-zero coefficients, and simply skip those that are 0. 
So defining $x^{1000} + 1$ would simply be: Polynomial({0: 1, 1000: 1}).
"""
import operator
import numpy as np
import matplotlib.pyplot as plt

class AddableDict(dict):
    def __add__(self, other):
        d1 = self; d2 = other
        for key2 in d2:
            if key2 in d1:
                d1[key2] = d1[key2] + d2[key2]
                if d1[key2] == 0:
                    del d1[key2]
            else:
                d1.update({key2: d2[key2]})
        return(d1)

class MultiplyDict(dict):
      def __mul__(self,other):
          d1 = self; d2 = other
          d = {}
          for key1 in d1:
              for key2 in d2: 
                  d.update({key1+key2:d1[key1]*d2[key2]})
          return d                  

class Polynomial: 
    def __init__(self,coeffs):
        self.coeffs = coeffs

    def __str__(self):
        coeffs = self.coeffs
        coeffs = sorted(coeffs.items(), key = operator.itemgetter(0), reverse = True)
        for key in coeffs:
            if key[0] > 1:
                print('({})x**{}+'.format(key[1],key[0]), end ="",flush =True)
            elif key[0] == 1:
                print('({})x+'.format(key[1]))
            elif key[0] == 0: 
                print('{}'.format(key[1]))   
        return('')            
    
    def __call__(self,x):
        coeffs = self.coeffs
        s = np.zeros(len(x))
        for key in coeffs:
            s = s + (coeffs[key]*x**key)
        return s   

    def __add__(self,other):
        coeffs1 = self.coeffs
        coeffs2 = other.coeffs
        return(AddableDict(coeffs1) + AddableDict(coeffs2))   

    def derivative(self):
        coeffs = self.coeffs
        coeffs_new = {}
        for key in coeffs:
            if key == 0:
                continue
            else:
                coeffs_new.update({key-1 : coeffs[key]*key})  
        return coeffs_new

    def __mul__(self,other):
        coeffs1 = self.coeffs
        coeffs2 = other.coeffs
        return(MultiplyDict(coeffs1)*MultiplyDict(coeffs2))


# a) 
coeffs = {0: 1, 5:-1, 10:1}
f = Polynomial(coeffs)
print(f)

x = np.linspace(-1, 1, 101)
plt.plot(x, f(x))
plt.show()        

# b)
i = Polynomial({0:1, 5:-7, 10:1})
j = Polynomial({5:7, 10:1, 15:-3})
print(i+j) 

# c)         
a = AddableDict({0: 2, 1: 3, 2: 4})
b = AddableDict({0: -1, 1:3, 2: 3, 3: 2})
print(a + b)

# d) 
c = Polynomial({2:2, 6:3, 10:1})
print(c.derivative())

# e) 
o = Polynomial({2:4,1:1})
u = Polynomial({3:3,0:1})
print(o*u)

"""
C:\\Users\\jensj\\OneDrive\\Skrivebord\\IN1910\\week2>python e2.py
(1)x**10+(-1)x**5+1

{0: 1, 10: 2, 15: -3}
{0: 1, 1: 6, 2: 7, 3: 2}
{1: 4, 5: 18, 9: 10}
{5: 12, 2: 4, 4: 3, 1: 1}
"""