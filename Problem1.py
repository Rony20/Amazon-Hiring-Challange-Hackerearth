a,n=map(int,input().split(" "))
inlist=[]
addlist=[]
for i in range(n):
    inlist.append(int(input()))

def findlower(num,actualnum):
    d_num=actualnum
    if num in addlist:
        if num==d_num:
            pass
        else:
            return num+1
    if mainlist.index(num)==0:
        return 1
    num-=1
    return findlower(num,d_num)

def findupper(num,actualnum):
    d_num=actualnum
    if num in addlist:
        if num==d_num:
            pass
        else:
            return num-1
    if mainlist.index(num)==a-1:
        return a
    num+=1
    return findupper(num,d_num)

for i in inlist:
    sum = 0
    addlist.append(i)

    for j in addlist:
        lower=findlower(j,j)
        upper=findupper(j,j)
        sum+=lower+upper
        print('[',lower,upper,']',end=" ")
    print(sum)
<<<<<<< HEAD

=======
>>>>>>> b1c6e75eb2ccd033e930e448e5c191c5f10c325b
