#QUEUE
class Queue:

  def __init__(self):
    self.arr = []
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
      self.arr.pop(0)

  def peek(self):
    if len(self.arr) == 0:
      print('STACK IS UNDERFLOW')
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
print(s.arr)
