def insertNodeAtTail(head, data):
    newNode = SinglyLinkedListNode(data)
    if head is None :
        head = newNode
        return head
    temp = head
    while temp.next is not None:
        temp = temp.next
    temp.next = newNode
    return head
