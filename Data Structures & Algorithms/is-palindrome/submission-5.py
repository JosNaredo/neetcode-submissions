class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([s_.lower() for s_ in s if s_.isalnum()])
        if len(s) <= 2:
            if len(set(s)) == 1 or s == '':
                return True
            else:
                return False
        if s.lower() == s[::-1]:
            return True
        else:
            return False 
        