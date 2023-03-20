#reverse last half of queue
queue = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = len(queue)
#one queue and one stack
q1, s1 = [], []
c = 0
while len(queue) != 0:
  a = queue.pop(0)
  if c < l // 2:
    q1.append(a)
  else:
    s1.append(a)
  c = c + 1
print(q1)
print(s1)
while len(s1) != 0:
  a = s1.pop()
  q1.append(a)
print(q1)
