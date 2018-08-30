n=int(input())
a=[]
for i in range (n):
    x=int(input())
    a.append(x)
for i in range(n):
    for j in range (n):
        for k in range (n):
            if a[i]+a[j]==a[k] and i<j<k:
                print (a[i],a[j],a[k])
