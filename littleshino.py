import math
num=list(map(int,input().split(" ")))
a=num[0]
b=num[1]

def gcd(m,n):
    if m<n:
        (m,n)=(n,m)

    if (m%n)!=0:
        return gcd(n,m%n)

    return n

n=gcd(a,b)
counter=0
p=int(math.sqrt(n))
for i in range(1,p+1):
    if n%i==0:
        if n/i==i:
            counter+=1
        else:
            counter+=2

print(counter,end="")