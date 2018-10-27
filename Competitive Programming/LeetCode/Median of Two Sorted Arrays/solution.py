from statistics import median
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        return median(sorted(nums1+nums2))
