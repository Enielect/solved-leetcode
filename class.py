print((32).__add__(35))

class Fraction:
    def __init__(self,top, bottom):
        self.num = top
        self.den = bottom
    def __str__(self):
        return str(self.num) + '/' + str(self.den)
    def __add__(self, second_frac):
        #The product rile (a/b) + (c/d) = (ad + cb) / bd
        final_num = self.num * second_frac.den + second_frac.num * self.den
        final_den = self.den * second_frac.den
        common = gcd(final_num, final_den)
        return Fraction(final_num // common, final_den // common)
        
new_frac = Fraction(3,4)

#print(new_frac)

#The best known algorithm for finding a greates common divisor is Euclid's Algorithm

def gcd(m,n) :
    if(m % n == 0):
        return n
    else:
        return gcd(n, m % n)

#write a method to the Fraction class to add two fractions together.

f1 = Fraction(1,4)
f2 = Fraction(1,2)
f3 = f1 + f2
print(f3)