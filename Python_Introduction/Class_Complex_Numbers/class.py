#https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem
#For this challenge, you are given two complex numbers, and you have to print the result of their addition, subtraction, multiplication, division and modulus operations.
#The real and imaginary precision part should be correct up to two decimal places.
import math

class Complex(object):
    # construction of the class
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def __add__(self, no):
        real = self.real + no.real
        imaginary = self.imaginary + no.imaginary
        return Complex(real, imaginary)
    def __sub__(self, no):
        real = self.real - no.real
        imaginary = self.imaginary - no.imaginary
        return Complex(real, imaginary)
    def __mul__(self, no):
        real = self.real * no.real
        imaginary = self.imaginary * no.imaginary
        return Complex(real, imaginary)
    def __div__(self, no):
        real = self.real / no.real
        imaginary = self.imaginary / no.imaginary
        return Complex(real, imaginary)
    def mod(self):
        return self.real % self.imaginary
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    c = map(float, raw_input().split())
    d = map(float, raw_input().split())
    x = Complex(*c)
    y = Complex(*d)
    print '\n'.join(map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]))