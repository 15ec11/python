K=int(input())
L=list()
import os
for i in range(0,K):
  G=str(input())
  L.append(str(G))
d=os.path.commonprefix(L)
print(d)
