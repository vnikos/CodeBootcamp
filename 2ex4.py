num = input('Enter a 9-digit number: ')
while len(num) != 9 or num.isdigit() != True:
    num = input ('This is not a 9-digit number. Enter a 10-digit number: ')
for x in num[::3]:
    print (int(x), end=' ')
print()
print(end=' ')
for x in num[1::3]:
    print (int(x), end=' ')
print()
print(end='  ')
for x in num[2::3]:
    print (int(x), end=' ')

