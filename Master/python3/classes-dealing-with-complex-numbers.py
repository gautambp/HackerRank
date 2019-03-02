# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/classes-dealing-with-complex-numbers/problem


class Complex(object):
    def __init__(self, real, imaginary):
        self.r = real
        self.i = imaginary
        
    def __add__(self, no):
        return Complex(self.r + no.r, self.i + no.i)
        
    def __sub__(self, no):
        return Complex(self.r - no.r, self.i - no.i)
        
    def __mul__(self, no):
        return Complex((self.r * no.r - self.i * no.i), (self.r * no.i + self.i * no.r))

    def __truediv__(self, no):
        d = no.r*no.r + no.i*no.i
        c = self * Complex(no.r, -1*no.i)
        c.r /= d
        c.i /= d
        return c
    def mod(self):
        return Complex((self.r*self.r + self.i*self.i) ** 0.5, 0)
    def __str__(self):
        if self.i == 0:
            result = "%.2f+0.00i" % (self.r)
        elif self.r == 0:
            if self.i >= 0:
                result = "0.00+%.2fi" % (self.i)
            else:
                result = "0.00-%.2fi" % (abs(self.i))
        elif self.i > 0:
            result = "%.2f+%.2fi" % (self.r, self.i)
        else:
            result = "%.2f-%.2fi" % (self.r, abs(self.i))
        return result

