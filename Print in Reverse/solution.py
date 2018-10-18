def reversePrint(head):
    rev = []
    if head.next is None:
        print()
    temp = head
    while temp is not None:
        rev.append(temp.data)
        temp = temp.next
    for i in reversed(rev):
        print(i)
    
