#stack using QUEUEs
class Queue:

  def __init__(self):
    self.arr = []
    self.a1 = []
    self.size = 3
    self.f = 0

  def push(self, element):
    if len(self.arr) == self.size:
      print('QUEUE IS OVERFLOW')
    else:
      self.arr.append(element)

  def pop(self):
    if len(self.arr) == 0:
      print('QUEUE IS UNDERFLOW')
    else:
      a = self.arr.pop(0)
      self.a1.append(a)

  def peek(self):
    if len(self.arr) == 0:
      print('QUEUE IS UNDERFLOW')
    else:
      return self.arr[0]

  def isEmpty(self):
    if len(self.arr) == 0:
      return True
    else:
      return False

  def display(self):
    print(self.arr)


s = Queue()
s.push(1)
s.push(2)
s.push(3)
s.pop()
s.pop()
s.pop()
print(s.arr)
print(s.a1[::-1])
