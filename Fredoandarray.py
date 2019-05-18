n=int(input())
numlist=list(map(int,input().split()))

sumlist=sum(numlist)

div=sumlist//n

print(div+1,end="")