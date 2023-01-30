"""data structure use for arranging of data
primitive and non primitive data structure
we use divide and conqure technic rather than kernals because we can use in divide and conqure n number
kernal we can divide only one time

skewed tree
left skewed only right will remain
right skewed only left will remain
"""
"""//program on different inputs and finding the length of it
size=int(input())
max=0
count=0
flag=0
str=input()
arr=list(str)
for i in range(0,size):
    if arr[i]=='1':
        count = count+1;
        flag=1
    elif(arr[i]=='0' and flag==1):
        count=0
        flag=0
    if count>max:
        max=count
print(max)
"""

"""
trees
1.full
2.complete
3.perfect
4.skewed
5.degenerted
6.binarysearch tree--- left child should always less than root node and right node always greater than root node
7. AVL
8. Red-Black
"""
"""
Min- order traversal
max- order traversal

inorder/level order --- left+root+right
pre-order - Root+l+r
post-order--- l+R+root


min-postorder-- the root node should be less than all elements
max-inorder-- the root node should be greated than all elements
"""
"""
#program to calculate the no.of two wheels and four wheels
v=int(input())
w=int(input())
if w&1 == 1 or w<2 or w<=v:
    print("Invalid Input")
else:
   z=((4*v)-w)//2
print("tw",z)  # ---two wheeler
print("fw",v-z) # ---four wheeler #v=200,w=540
"""
"""
class bt:
    def __init__(self, data):
        self.data=data
        self.leftchild=None
        self.Rightchild=None
def insert(root,newvalue):
   if root is None:
      root=bt(newvalue)
      return root
   if newvalue<root.data:
      root.leftchild=insert(root.leftchild,newvalue)
   else:
      root.Rightchild=insert(root.Rightchild,newvalue)
   return root
def inorder(root):
    if root == None:
        return
    inorder(root.leftchild)
    print(root.data)
    inorder(root.Rightchild)
root = insert(None,15)
insert(root,10)
insert(root,24)
insert(root,5)
insert(root,14)
insert(root,21)
insert(root,55)
print("inorder traversal is binarytree is:")
inorder(root)
"""
"""
#preorder
class bt:
    def __init__(self, data):
        self.data=data
        self.leftchild=None
        self.Rightchild=None
def insert(root,newvalue):
   if root is None:
      root=bt(newvalue)
      return root
   if newvalue<root.data:
      root.leftchild=insert(root.leftchild,newvalue)
   else:
      root.Rightchild=insert(root.Rightchild,newvalue)
   return root
def preorder(root):
    if root == None:
        return
    print(root.data)
    preorder(root.leftchild)
    preorder(root.Rightchild)
root = insert(None,15)
insert(root,10)
insert(root,24)
insert(root,5)
insert(root,14)
insert(root,21)
insert(root,55)
print("preorder traversal is binarytree is:")
preorder(root)

#postorder
class bt:
    def __init__(self, data):
        self.data=data
        self.leftchild=None
        self.Rightchild=None
def insert(root,newvalue):
   if root is None:
      root=bt(newvalue)
      return root
   if newvalue<root.data:
      root.leftchild=insert(root.leftchild,newvalue)
   else:
      root.Rightchild=insert(root.Rightchild,newvalue)
   return root
def postorder(root):
    if root == None:
        return
    postorder(root.leftchild)
    postorder(root.Rightchild)
    print(root.data)
root = insert(None,15)
insert(root,10)
insert(root,24)
insert(root,5)
insert(root,14)
insert(root,21)
insert(root,55)
print("postorder traversal is binarytree is:")
postorder(root)

"""

#horizontal distance evaluation with hash function
class Node:
    def __init__(self, key, l=None, r= None):
        self.key=key
        self.l=l
        self.r=r
def vot(node,dist,d):
    if node is None:
        return
    d.setdefault(dist,[]).append(node.key)
    vot(node.l,dist-1,d)
    vot(node.r,dist+1,d)
def pvot(root):
    d={}
    vot(root,0,d)
    for value in d.values():
        print(value)
if __name__=='__main__':
   root = Node(1)
   root.l=Node(2)
   root.r=Node(3)
   root.r.l=Node(4)
   root.r.r=Node(5)
   root.r.l.l=Node(6)
   root.r.l.r=Node(7)
   root.r.l.r.l=Node(8)
   root.r.l.r.r=Node(9)
   root.r.l.r.r.l=Node(10)
   root.r.l.r.r.r=Node(11)
   pvot(root)#pvot is print vertical order traversal
