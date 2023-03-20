#reverse first half of stack
stack = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('originsl stack:', stack)
d = len(stack)
c = 0
#2 stacks
stack2 = []
temp = []
while c < d:
  a = stack.pop()
  if c < d // 2:
    stack2.append(a)
  else:
    temp.append(a)
  c = c + 1
print('last half:', stack2)
print('first half:', temp)
while len(stack2) != 0:
  a = stack2.pop()
  temp.append(a)
print('stack after reversing first half', temp)
