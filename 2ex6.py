x = input ('Enter numbers: ').split()
n=2
for f in range (3):
    for i in x[f::3]:
        print (n*' ', i, '| ', end='')
    print()
    n -= 1

