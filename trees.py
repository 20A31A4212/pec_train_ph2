'''TREES'''
'''Binary tree
Binary search tree
AVL Tree
->child ,root ,leaf ,intermediate ,parent nodes
Binary tree
->Atmost 2 child
Binary Search Tree
->left child must be less than root
->right child mus be greater than or equal to root
Traversal methods
 Inorder->left,root,right
 Preorder->root,left,right
 Postorder->left,right,root
 level order'''


#Trees
class Node:

  def __init__(self, value):
    self.left = None
    self.right = None
    self.val = value


class BSTree:

  def add_element(self, root, value):
    new_node = Node(value)
    if new_node.val < root.val:
      if root.left != None:
        self.add_element(root.left, value)
      else:
        root.left = new_node
    else:
      if root.right != None:
        self.add_element(root.right, value)
      else:
        root.right = new_node
    pass

  def inorder(self, root):
    if root.left != None:
      self.inorder(root.left)
    print(root.val)
    if root.right != None:
      self.inorder(root.right)

  def preorder(self, root):
    print(root.val)
    if root.left != None:
      self.preorder(root.left)
    if root.right != None:
      self.preorder(root.right)
    pass

  def postorder(self, root):
    if root.left != None:
      self.postorder(root.left)
    if root.right != None:
      self.postorder(root.right)
    print(root.val)
    pass

  def levelorder(self, root):
    q = []
    q.append(root)
    if root.left:
      q.append(root.left)
    if root.right:
      q.append()
    pass


obj = BSTree()
root = Node(10)
obj.add_element(root, 7)
obj.add_element(root, 40)
obj.add_element(root, 5)
obj.add_element(root, 9)
obj.add_element(root, 15)
obj.add_element(root, 60)
print('Inorder:')
obj.inorder(root)
print('Postorder:')
obj.postorder(root)
print('Preorder:')
obj.preorder(root)
