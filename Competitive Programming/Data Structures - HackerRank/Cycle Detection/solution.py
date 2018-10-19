def has_cycle(head):
    x = []
    while head:
        if head in x:
            return True
        else:
            x.append(head)
        head=head.next
    return False
            
