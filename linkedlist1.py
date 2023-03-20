class LinkedList:

  def add_element(self, head, ele):
    temp = head
    new_node = Node(ele)
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
    pass


a = list(map(int, input().split(',')))
obj = LinkedList()
head = Node(a[0])
a = a[1:]
for i in a:
  obj.add_element(head, i)
obj.print_list(head)