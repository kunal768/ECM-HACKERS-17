def deleteNode(head, position):
    if position is 0:
        head = head.next
        return head
    temp = head
    count = 0
    while count < position:
        count+=1
        prev = temp
        temp = temp.next
    prev.next = temp.next
    return head
