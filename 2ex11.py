limit = int(input ('Enter limit: '))
a = []
for x in range(1,limit+1):
    y=x
    while x > 1:
        x /= 2
    if x != 1:
       a.append(y)
for i in range(len(a)):
    if (i % 10 == 0 and i>0):
        print ()
    print (a[i], end=' ')
    
           
    
       



