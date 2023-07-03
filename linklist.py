class Node:
    def __init__(self,data):
        self.data=data
        self.next=None




class LinkList:
    def __init__(self):
        self.head=None
        self.n=0
        
        
    def __len__(self):
        return self.n
    
    
    def insert_head(self,value):
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node
        self.n=self.n+1
        
        
    def traverse(self):
        curr=self.head
        while curr!=None:
            print(curr.data)
            curr=curr.next
            
            
    def __str__(self):
        curr=self.head
        result=''
        while curr!=None:
            result=result+str(curr.data)+'->'
            curr=curr.next
        return result[:-2]
    
    
    
    def append(self,value):
        new_node=Node(value)
        
        if self.head==None:
            self.head=new_node
            self.n=self.n+1
            return
        curr=self.head
        while curr.next!=None:
            curr=curr.next
        curr.next=new_node
        self.n=self.n+1
        
        
    def insert_after(self,after,value):
        new_node=Node(value)
        curr=self.head
        while curr!=None:
            if curr.data==after:
                break
            curr=curr.next
        if curr!=None:
            new_node=curr.next
            curr.next=new_node
            self.n=self.n+1
        else:
            return 'Item not found'
        
    def clear(self):
        self.head=None
        self.n=0
        
    def delete_head(self):
        if self.head==None:
            return 'Empty link list'
        else:
            self.head=self.head.next
            self.n=self.n-1
            
            
    def pop(self):
        curr=self.head
        if self.head==None:
            return 'Empty Link List'
        if curr.next==None:
            self.delete_head()
            return
        while curr.next.next!=None:
            curr=curr.next
        curr.next=None
        self.n=self.n-1
