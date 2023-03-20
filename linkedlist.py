'''LINKED LIST'''
#Node
#Value
#create linked list node


class Node:

  def __init__(self, value):
    self.value = value
    self.next = None


#creating linked list
class LinkedList:

  def add_element(self, head, value):
    #creating new node
    new_node = Node(value)
    #inserting at last position
    temp = head
    while temp.next != None:
      temp = temp.next
    #assigning new node to linked list
    temp.next = new_node

  def add_at_first_position(self, head, value):
    new_node = Node(value)
    new_node.next = head
    head = new_node
    return head

  def add_at_specific_position(self, head, value, pos):
    prev = None
    cur = head
    while pos != 0:
      prev = cur
      cur = cur.next
      pos -= 1
    new_node = Node(value)
    new_node.next = cur
    prev.next = new_node

  def remove_element(self):
    temp = head
    while temp.next.next != None:
      temp = temp.next
    temp.next = None
    pass

  def print_list(self):
    temp = head
    while temp != None:
      if temp.next == None:
        print(temp.value)
        break
      print(temp.value, end=' -> ')
      temp = temp.next

  def search_element(self, value):
    temp = head
    ind = 0
    while temp != None:
      if temp.value == value:
        print('Value found at', ind)
        break
      ind += 1
      temp = temp.next

  def reverse(self, head):
    cur = head
    prev = None
    while cur != None:
      next = cur.next
      cur.next = prev
      prev = cur
      cur = next
    return prev


obj = LinkedList()
head = Node(10)
obj.add_element(head, 20)
obj.add_element(head, 30)
obj.add_element(head, 40)
obj.add_element(head, 50)
obj.print_list()
obj.search_element(30)
obj.remove_element()
print('List after removed:')
obj.print_list()
print('Inserting ele at beginning:')
a = obj.add_at_first_position(head, 50)
head = a
obj.print_list()
obj.add_at_specific_position(head, 60, 2)
print('Inserting ele at middle:')
obj.print_list()
head = obj.reverse(head)
print('After reversing:')
obj.print_list()
