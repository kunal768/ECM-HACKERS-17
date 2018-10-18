
#*************Our Code ******************************

def insertNodeAtHead(llist_head,data):
    temp = SinglyLinkedListNode(data)
    temp.next = llist_head
    llist_head = temp
    return llist_head

