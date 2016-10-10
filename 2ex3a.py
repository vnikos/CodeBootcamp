num = input('Enter a 10-digit number: ')
while len(num) != 10 or num.isdigit() != True:
    num = input ('This is not a 10-digit number. Enter a 10-digit number: ')
odd = []
even = []
for x in num:
    if int (x) % 2 == 0:
        even.append(x)
    else:
        odd.append(x)
for i in range (len(odd)):
    print (odd[i], end=' ')
print()
print(end=' ')
for i in range(len(even)):
    print (even[i], end=' ')

        
    
    
