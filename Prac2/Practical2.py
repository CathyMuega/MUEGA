class Quadratic:

    #constructor
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    #methods
    def getA(self):
        return self.a

    def getB(self):
        return self.b

    def getC(self):
        return self.c

    def evaluate(self, x):
        return self.a * (x ** 2) + self.b * x + self.c

    def discriminant(self):
        return (self.b * self.b) - 4 * (self.a * self.c)

    def isImaginaryRoots(self): #negative
        if self.discriminant() < 0:
            return bool(True)

    def isRealRoots(self): #positive/real/zero
        if self.discriminant() >= 0:
                return bool(True)

    def firstRoot(self):
        if self.isImaginaryRoots() != bool(True):
            x1 = ((-1 * self.b) + self.discriminant() ** 0.5) / (2 * self.a)
            return x1

    def secondRoot(self):
        if self.isImaginaryRoots() != bool(True):
            x2 = ((-1 * self.b) - self.discriminant() ** 0.5) / (2 * self.a)
            return x2

    def isPerfectSquare(self):
        if self.firstRoot() == self.secondRoot():
            return bool(True)

a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))
print()

q = Quadratic(a, b, c)
print(f"Quadratic expression: {q.getA()}x2 + {q.getB()}x + {q.getC()}")
if q.isRealRoots():
    print(f"The roots are real: x1 = {q.firstRoot()} ; x2 = {q.secondRoot()}")
    if q.isPerfectSquare():
        print("It is a perfect square")
    else:
        print("It is not a perfect square")
elif q.isImaginaryRoots():
    print("The roots are imaginary")
print()

print("Evaluating the expression:")
x = int(input("Enter x: "))
print(f"Result: {q.evaluate(x)}")