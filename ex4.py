import math
a = float(input("Enter value a: "))
b = float(input("Enter value b: "))
c = float(input("Enter value c: "))
if (b**2 - 4*a*c)<0:
    print ("There are no real-valued solutions")
else:
    x1 = (-1*b + math.sqrt(b**2 - 4*a*c))/2*a
    x2 = (-1*b - math.sqrt(b**2 - 4*a*c))/2*a
    print ("The solutions of the quadratic equation are: ", x1, x2)
