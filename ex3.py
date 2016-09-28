import math
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
r = (a+b+c)*(-a+b+c)*(a-b+c)*(a+b-c)
A = math.sqrt(r)/4
print ("The triangle area is: ", A)
