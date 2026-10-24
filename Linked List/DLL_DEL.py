
class Node:
    def __init__(self, value):
        self.prev = None
        self.data = value
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        temp = self.head

        if temp:
            while temp.next:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp
        else:
            self.head = new_node

    def insert(self, new_node, pos):
        if pos < 1:
            print("Invalid position")
            return

    def delete(self,value):
        temp = self.head
        if temp.data== value:
            self.head=self.head.next
            self.head.prev=None
        else:
            while(temp.data!=value and temp):
                temp=temp.next
                if temp== None :
                    print("value is not present in the list")
                    return

                temp.prev .next=temp.next
                if temp.next:
                    temp.next.prev=temp.prev
                temp.None
               


        if pos == 1:
            new_node.next = self.head

            if self.head:
                self.head.prev = new_node

            self.head = new_node
            return

        p = 1

        while temp and p < pos - 1:
            temp = temp.next
            p += 1

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next:
            temp.next.prev = new_node

        temp.next = new_node

    def print(self):
        temp = self.head
        print("List elements:")

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()
        
    def count_occ(self,num):
        temp=self.headcnt=0
        whike temp:
            if temp.data== num:
                count+=1
            temp=temp.next
            print("The occurence of number ",count)
            
    def swap(self):
        temp=node1=self.head     #node1 is first node
        while temp.next:            #temp is last node
            
            temp=temp.next
        temp.next=node1.next
        node1.next=None
        node1.prev=temp.prev
        temp.prev.next=node1
        temp.prev=None
        self.head=temp
        
        
        

    def print_reverse(self):
        temp = self.head

        if temp is None:
            print("List is empty")
            return

        while temp.next:
            temp = temp.next

        print("Reverse list elements:")

        while temp:
            print(temp.data, end=" ")
            temp = temp.prev

        print()


list1 = Linkedlist()

list1.append(Node(12))
list1.append(Node(52))
list1.append(Node(12))
list1.append(Node(56))
list1.append(Node(12))

list1.insert(Node(99), 3)
list1.swap()


list1.print()
list1.print_reverse()


# write a function to count occurrence of a number in the doubly linked list 
# Write a program to swap first and last node in DLL







