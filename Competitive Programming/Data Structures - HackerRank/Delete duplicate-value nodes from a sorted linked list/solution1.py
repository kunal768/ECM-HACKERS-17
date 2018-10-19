def removeDuplicates(head):
    nums = []
    if head is None :
        return head
    temp = head
    while temp is not None:
        nums.append(temp.data)
        temp = temp.next
    nums = list(set(nums))
    new_head = SinglyLinkedListNode(nums[0])
    temp1 = new_head
    for i in range(1,len(nums)):
        newNode = SinglyLinkedListNode(nums[i])
        temp1.next = newNode
        temp1 = newNode
    return new_head
