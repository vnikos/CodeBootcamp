y = int(input("Enter a Year between 1900 and 2099: "))
if y not in range(1901,3000):
    y = int(input("Enter a Year between 1900 and 2099: "))

a = y % 4
b = y % 7
c = y % 19
d = (19*c + 15) % 30
e = (2*a +4*b - d + 34) % 7
month = ((d + e + 114)//31)
day = ((d + e + 114) %31) + 1
day = day + 13
m1 = 3
m2 = 4


if month == 3:
    if day > 31:
        day -= 31
        month +=1
elif month == 4:
    if day > 30:
        day -= 30
        month +=1

print ('Day: ', day, 'Month: ', month)

    
