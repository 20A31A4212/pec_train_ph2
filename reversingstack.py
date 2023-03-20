#Reversing stack usign temp stack
class Stack1:

  def __init__(self):
    self.arr = []
    self.p = []
    self.size = 3
    self.f = 0

  def push(self, element):
    if len(self.arr) == self.size:
      print('STACK IS OVERFLOW')
    else:
      self.arr.append(element)

  def pop(self):
    if len(self.arr) == 0:
      print('STACK IS UNDERFLOW')
    else:
      self.p.append(self.arr[-1])
      self.arr.pop()

  def peek(self):
    if len(self.arr) == 0:
      print('STACK IS UNDERFLOW')
    else:
      return self.arr[-1]

  def isEmpty(self):
    if len(self.arr) == 0:
      return True
    else:
      return False

  def display(self):
    print(self.arr)


s = Stack1()
s.push(1)
s.push(2)
s.push(3)
s.pop()
s.pop()
s.pop()
print(s.p[::-1])
