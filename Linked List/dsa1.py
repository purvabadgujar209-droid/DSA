class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        
node1=Node(10)
node2=Node(30)
node3=Node(45)
node4=Node(66)
node5=Node(34)
node6=Node(24)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=node6
node6.next=None


current= node1
while current is not None:
    print(current.data,end="--->")
    current= current.next
    
print("None")
    
          
        
