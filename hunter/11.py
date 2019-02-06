def reverse(n):
  str = ""
  for i in n:
    str = i + str
  return str
n = input()
print (reverse(n))
