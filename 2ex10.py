b = input('Enter binary number: ')
for x in b:
    while (int(x) != 0 or int(x) != 1):
        print ('this is not a binary number')
        b = input ('Enter  binary number: ')
bin = []
for x in b:
    bin.append(x)

if bin.count('0') > bin.count('1'): print ('Longest run was zeros with length:', bin.count('0'))
elif bin.count('0') < bin.count('1'):
    print ('Longest run was ones with length:', bin.count('1'))
else: print ('Equal longest run of ones and zeros with length:', bin.count('0'))
    
