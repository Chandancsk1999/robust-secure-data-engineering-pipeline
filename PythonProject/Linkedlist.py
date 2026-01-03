from wsgiref.validate import header_re


class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None


    def insert_at_beg(self,data):
        n = Node(data)
        if (self.head == None):
            self.head = n
            return
        a=self.head
        self.head=n
        self.head.next=a
        return



    def insert_at_pos(self,data,pos):
        n=Node(data)
        temp=self.head
        count=1
        if (self.head == None):
            self.head = n
            return

        while(temp.next!= None):
            if count==pos-1:
                break
            temp=temp.next


            count += 1

        a=temp.next
        temp.next=n
        n.next=a
        return


    def insert_at_end(self,data):
        n=Node(data)
        if(self.head==None):
            self.head = n
            return

        temp=self.head
        while(temp.next!=None):   # This will add at the end
            temp=temp.next

        temp.next=n
        return

    def printLinkedList(self):
        temp=self.head
        while(temp!=None):
            print(temp.data)
            temp=temp.next

a=LinkedList()
# b=LinkedList()
a.insert_at_beg(9)
a.insert_at_beg(8)
a.insert_at_beg(7)
a.insert_at_beg(6)
a.insert_at_end(10)
a.insert_at_pos(15,18)

a.printLinkedList()


