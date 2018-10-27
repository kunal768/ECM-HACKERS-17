class Solution:
    def isPalindrome(self, x):
        ls = [i for i in x]
        rev = ls.reverse() 
        if ls is rev:
            return True
        else:
            return False
        
