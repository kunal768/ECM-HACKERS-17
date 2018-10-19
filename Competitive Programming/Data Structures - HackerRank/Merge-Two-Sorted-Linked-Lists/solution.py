def mergeLists(head1, head2):
    num1 =[]
    num2 = []
    temp1 = head1
    temp2 = head2
    if head1 and head2 is None:
        return 1
    while temp1 is not None:
            num1.append(temp1.data)
            temp1 = temp1.next
    while temp2 is not None:
            num2.append(temp2.data)
            temp2 = temp2.next
    #print(num2,num1)
    num3 = sorted(num1+num2)
    head3 = SinglyLinkedListNode(num3[0])
    temp = head3
    count = 1
    while count < len(num3):
        newNode = SinglyLinkedListNode(num3[count])
        prev = temp
        temp.next = newNode
        temp = newNode
        count+=1
    return head3
        
