num = list(input('Enter a 10-digit number: '))
while len(num) != 10:
    num = input ('Enter a 10-digit number: ')
odd = []
even = []
for x in num:
    if int (x) % 2 == 0:
        even.append(x)
    else:
        odd.append(x)
for x in odd:
    print (int(x), end=' ')
print()
print(end=' ')
for x in even:
    print (int(x), end=' ')


        
    
    
