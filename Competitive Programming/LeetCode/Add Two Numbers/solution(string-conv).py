# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        nums1 = []
        nums2 = []
        temp = l1
        temp2 = l2
        while temp is not None:
            nums1.append(str(temp.val))
            temp = temp.next
        while temp2 is not None:
            nums2.append(str(temp2.val))
            temp2 = temp2.next
        nums1 = ("".join(nums1))[::-1]
        nums2 = ("".join(nums2))[::-1]
        #print(nums1,nums2)
        nums3 = int(nums1)+int(nums2)
        nums3 = [int(i) for i in str(nums3)[::-1]]
        l3 = ListNode(nums3[0])
        temp = l3
        for i in range(1,len(nums3)):
            newNode = ListNode(nums3[i])
            temp.next = newNode
            temp = newNode
        return l3
        #print(nums3)
                 
