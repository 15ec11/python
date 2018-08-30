g=int(input())
p=[]
for i in range(1,g+1):
  n=int(input())
  p.append(n)
m=p[0]
for x in p:
  if (m+x==0):
    print (m,x)
