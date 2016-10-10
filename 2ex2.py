byte = input('Enter binary number: ')
while len(byte) != 8:
    byte = input ('Enter correct binary number: ')
for x in byte[:8]:
    while (int(x) != 0 or int(x) != 1):
        print ('this is not a binary number')
        byte = input ('Enter  binary number: ')
sum = 0
for x in byte[:8]:
	if int(x) == 1:
		sum += 1
if sum % 2 == 0:
	print ('Parity check OK.')
else:
    print ('Parity check not OK.')
