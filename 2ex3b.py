num = input('Enter a 10-digit number: ')
while len(num) != 10 or num.isdigit() != True:
    num = input ('This is not a 10-digit number. Enter a 10-digit number: ')
for x in num:
    if int (x) % 2 != 0:
        print (int(x), end=' ')
print()
print(end=' ')
for x in num:
    if int (x) % 2 == 0:
        print (int(x), end=' ')

        
