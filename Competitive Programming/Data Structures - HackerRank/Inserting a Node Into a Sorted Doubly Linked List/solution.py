def sortedInsert(head, data):
    temp = DoublyLinkedListNode(data)
    if head==None: 
        head=temp
    else:
        cur=head
        if cur.data>=data:  #insert temp to head
            temp.next=cur
            cur.prev=temp
            return temp
        else:  #insert temp to non-head part of list
            while cur.next!=None:
                if cur.data<data and cur.next.data>=data:
                    temp.next=cur.next  
                    cur.next.prev=temp  
                    cur.next=temp
                    temp.prev=cur    
                    break
                else: 
                    cur=cur.next
            else: 
                cur.next=temp
                temp.prev=cur  
    return head
