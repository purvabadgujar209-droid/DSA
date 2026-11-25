class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
class BST:
    def __init__(self):
        self.root=None
        
    def insert(self,new_node):
        if self.root==None:
            self.root=new_node
        else:
            temp=self.root
            while True:
                if new_node.data<temp.data:
                    if temp.left==None:
                        temp.left=new_node
                        return
                    else:
                        temp=temp.left
                else:
                    if temp.right==None:
                        temp.right=new_node
                        return
                    else:
                        temp=temp.right
                        
    def inorder(self,rt):
        if rt==None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data,end=" ")
            self.inorder(rt.right)
            
    def preorder(self,rt):
        if rt==None:
            return
        else:
            print(rt.data, end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)
    def postorder(self,rt):
        if rt==None:
            return
        else:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.data,end=" ")
        
        
    def findmaxmin(self):
        temp=self.root
        while temp.left:
            temp=temp.left
            print("Min",temp.data)
        
        while temp.right:
            temp=temp.right
            print("Max",temp.data)
                
    
b1=BST()
b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(600))
b1.insert(Node(300))
b1.insert(Node(70))
b1.insert(Node(6))
print("inorder")
b1.inorder(b1.root)
print("\npostorder")
b1.postorder(b1.root)
print("\npreorder")
b1.preorder(b1.root)
b1.findmaxmin()
                    
                        
            
                