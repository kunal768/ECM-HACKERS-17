def compare_lists(llist1, llist2):
    num1 = []
    num2 = []
    temp1 = llist1
    temp2 = llist2
    if llist1 and llist2 is None:
        return 1
    while temp1 is not None:
            num1.append(temp1.data)
            temp1 = temp1.next
    while temp2 is not None:
            num2.append(temp2.data)
            temp2 = temp2.next
    #print(num2,num1)
    if num1 == num2 :
        return 1
    else:
        return 0
            
