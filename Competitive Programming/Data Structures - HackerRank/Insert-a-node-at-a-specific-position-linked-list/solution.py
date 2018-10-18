def insertNodeAtPosition(head, data, position):
    if position == 0:
        return SinglyLinkedListNode(data,head)
    temp = head
    new_node = SinglyLinkedListNode(data)
    count = 0
    while count<position:
        count += 1
        prev = temp
        temp = temp.next
    
    prev.next = new_node
    new_node.next = temp
    return head
