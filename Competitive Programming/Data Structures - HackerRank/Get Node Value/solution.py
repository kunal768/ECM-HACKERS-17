def getNode(head, positionFromTail):
    if head.next is None:
        return head.data
    
    # First calculate the length of the LL
    length = 0
    temp = head
    while temp is not None:
        length += 1
        temp = temp.next
        
    # Now we have the length the positon of the element is length - positionFromTail -1 
    count = 0
    #temp1 = SinglyLinkedListNode(head.data)
    temp1 = head
    while count < (length-positionFromTail-1) :
        temp1 = temp1.next
        count+=1
    return temp1.data
