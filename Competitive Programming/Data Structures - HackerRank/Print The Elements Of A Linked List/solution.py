#*************Our Code ******************************

def printLinkedList(head):
    temp = head
    while(temp.next!=None):
        print(temp.data)
        temp = temp.next
    print(temp.data)



