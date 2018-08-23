K1,K2,L=input().split(' ')
L=int(L)
D=0
for i in range(len(K1)):
    if K1[i]!=K2[i]:
        D+=1
if D==L:print("yes")
else:print("no")
