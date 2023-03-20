#double linked list
class Node:

  def __init__(self, value):
    self.prev = None
    self.next = None
    self.value = value


class DoubleLL:

  def add_element(self, head, value):
    temp = head
    while temp.next != None:
      temp = temp.next
    new_node = Node(value)
    temp.next = new_node
    new_node.prev = temp

  def print_reverse(self, head):
    temp = head
    while temp.next != None:
      temp = temp.next
    while temp != None:
      if temp.prev == None:
        print(temp.value)
        break
      print(temp.value, end=' -> ')
      temp = temp.prev

  def print_list(self, head):
    temp = head
    while temp != None:
      if temp.next == None:
        print(temp.value)
        break
      print(temp.value, end=' -> ')
      temp = temp.next

  def remove(self, head):
    temp = head
    while temp.next.next != None:
      temp = temp.next
    temp.next.prev = None
    temp.next = None


obj = DoubleLL()
head = Node(1)
for i in range(2, 11):
  obj.add_element(head, i)
obj.print_list(head)
obj.print_reverse(head)
obj.remove(head)
obj.print_list(head)
