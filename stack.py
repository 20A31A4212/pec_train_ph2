#implement linear search on stack
s = [1, 2, 3, 4, 5]
a = 3
l = []
f = 0
while len(s) != 0:
  b = s.pop()
  if a == b:
    print('Element found')
    f = 1
  l.append(b)
if f == 0:
  print('Element not found')