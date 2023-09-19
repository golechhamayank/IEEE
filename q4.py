import math
lst = []
for i in range(0,5):
    n = int(input('Number:'))
    lst.append(n)

for i in range(0,len(lst)-1):
    gcd = math.gcd(lst[i],lst[i+1])

print('The greatest common divisor is',gcd)
