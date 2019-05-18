a,n=map(int,input().split(" "))
inlist=[]
addlist=[]
for i in range(n):
    inlist.append(int(input()))

def findlower(num):
    p = addlist.index(num)
    try:
        if p-1<0:
            raise IndexError
        return addlist[p - 1] + 1
    except IndexError:
        return 1

def findupper(num):
    p=addlist.index(num)
    try:
        return addlist[p + 1] - 1
    except IndexError:
        return a


for i in inlist:
    sum = 0
    addlist.append(i)
    addlist.sort()
    for j in addlist:
        lower=findlower(j)
        upper=findupper(j)
        sum+=lower+upper
        print('[',lower,upper,']',end=" ")
    print(sum)
