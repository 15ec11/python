a=int(input())
new=[]
list=[int(x) for x in input().split()]
for i in range(0,a):
	if(i==list[i]):
		new.append(i)
	elif((new==[]) and (i==(a-1))):
		print('-1')
s=sorted(new)
k=len(s)
for i in range(0,k):
	print (s[i]),
