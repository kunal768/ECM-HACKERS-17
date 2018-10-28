class Solution(object):
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None
    def addTwoNumbers(self, l1, l2):
        root = ListNode((l1.val+l2.val) % 10)
        carry = (l1.val+l2.val) // 10
        node_cur = root
        while 1:
            if l1.next == None and l2.next == None:
                break
            if l1.next != None:
                l1 = l1.next
            else:
                l1 = ListNode(0)
            if l2.next != None:
                l2 = l2.next
            else:
                l2 = ListNode(0)
            node_cur.next = ListNode((l1.val+l2.val+carry) % 10)
            node_cur = node_cur.next
            carry = (l1.val+l2.val+carry) // 10
        if carry:
            node_cur.next = ListNode(carry)
        return root
