class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        global permutation
        if s1 == "" or len(set(s1)) > len(set(s2)):
            return False
        
        if not any([s in s2 for s in s1]):
            return False
        
        if s1 in s2:
            return True
        
        if len(s1) == 2:
            if s1[1]+s1[0] in s2:
                return True
            else:
                return False
        elif len(s1) == 1:
            return False
        permutation = False
        def permutate(n, a):
            global permutation
            if ''.join(a) in s2:
                permutation = True
                # return
            for i in range(n):
                permutate(n - 1, a)
                if n % 2 == 0:
                    a[i], a[n-1] = a[n-1], a[i]
                else:
                    a[0], a[n-1] = a[n-1], a[0]
        
        permutate(len(s1), list(s1))
        return permutation