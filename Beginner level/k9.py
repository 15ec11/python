n=int(input())
l1=[]
l2=[]
count=0
for i in range(0,n):
    r=int(input())
    if(type(r)==int):
        l1.append(r)
for j in range(0,n):
    c=l1.count(l1[j])
    if(c>1):
        count=count+1
    else:
        l2.append(l1[j])
else:
    sorted(l2)
    for x in range(len(l2)):
        print(l2[x],end=' ')
