x = input ('Enter number sequence :')
while  x.isdigit() != True:
    x = input ('This is not a number sequence. Enter number sequence :')
y = x[len(x) - 1]
z = x[len(x) - 2]
sum = 0
for n in range (0, len(x)-2, 2):
    sum += int (x[n]) * int (x[n+1])

sum
if len(x) % 2 == 0:
    print (sum + (int(y) * int(z)))
else:
    print (sum + int(y))
