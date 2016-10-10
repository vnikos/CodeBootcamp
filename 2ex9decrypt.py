import string
list = []
s = int(input ('Enter shift: '))
x = input ('Enter phrase: ')
Z = 0
if s > 25:
    s -= 25
for i in x:
    z = ord(i) - s
    if z < 64:
        list.append(chr(z+26))
    else:
        list.append(chr(z))
for i in range (len(list)):
    print (list[i], end='')
