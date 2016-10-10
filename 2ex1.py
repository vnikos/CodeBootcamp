TIN = input ('Enter Tax Identification Number: ')
while len(TIN) != 9:
    TIN = input ('Enter correct Tax Identification Number: ')
sum = 0
i = 1
for x in TIN[-2::-1]:
	sum += int(x) * (2**i)
	i += 1
t = sum % 11
check_digit = t % 10
if check_digit == int (TIN[8]):
    print ('Tax Identification Number valid.')
else:
    print ('Tax Identification Number not valid.')

