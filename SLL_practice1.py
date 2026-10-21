
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            return
        last=self.head
        while last.next:
            last=last.next
            
        last.next=new_node
        
    def print_node(self):
        current=self.head
        while current:
            print(current.data,end="--->")
            current=current.next
        print("None")
        
    def delete(self):
        current=self.head
        while current and current.next:
    
            current.next=current.next.next
            current=current.next
ll=LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.delete()
ll.print_node()
    
        

      