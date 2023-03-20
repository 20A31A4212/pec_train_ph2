#reverse the first half of linked list
class Node:

  def __init__(self, value):
    self.next = None
    self.value = value


class LinkedList:

  def insert(self, head, value):
    temp = head
    new_node = Node(value)
    while temp.next != None:
      temp = temp.next
    temp.next = new_node

  def print_list(self, head):
    temp = head
    while temp != None:
      if temp.next == None:
        print(temp.value)
        break
      print(temp.value, end=' -> ')
      temp = temp.next

  def reverse_first_half(self, head):
    l = 0
    temp = head
    while temp != None:
      l += 1
      temp = temp.next
    c = 0
    prev = None
    cur = head
    first = head
    while c < (l // 2):
      next = cur.next
      cur.next = prev
      prev = cur
      cur = next
      c = c + 1
    first.next = cur
    return prev


obj = LinkedList()
head = Node(1)
for i in range(2, 11):
  obj.insert(head, i)
obj.print_list(head)
head = obj.reverse_first_half(head)
obj.print_list(head)