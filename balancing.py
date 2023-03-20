#balancing paranthesis
s = '))(('
l = []
f = 0
c, c1 = 0, 0
for i in range(len(s)):
  if s[i] == '(':
    l.append(s[i])
    c = c + 1
  else:
    if len(l) > 0:
      a = l.pop()
      c1 = c1 + 1
    else:
      print('Invalid')
      f = 1
      break
if c == c1:
  if f == 0:
    print('Valid')
if len(l) > 0 and f == 0:
  print('Invalid')