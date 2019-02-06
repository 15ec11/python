def reverse(p):
  str = ""
  for i in p:
    str = i + str
  return str
p = input()
g=reverse(p)
print (g+" ")
