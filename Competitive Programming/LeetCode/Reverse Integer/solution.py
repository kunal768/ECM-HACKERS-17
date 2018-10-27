class Solution:
    def reverse(self, x):
        if x< 0 :
            rev = int("-"+(str(abs(x))[::-1]))
            if rev in range(-2**31 , 2**31):return rev
            else:return 0
        elif x>=0 :
            rev = int(str(abs(x))[::-1])
            if rev in range(-2**31 , 2**31):return rev
            else: return 0
        
