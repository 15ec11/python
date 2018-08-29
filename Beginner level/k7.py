K=int(input())
print(K)
L=list()
import os
for i in range(0,K):
  G=str(input())
  L.append(str(G))
  print(L)
d=os.path.commonprefix(L)
print(d)
