class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutation = []
        def permutate(n, a):
            if  n == 1:
                permutation.append(a[:])
                return
            for i in range(n):
                permutate(n - 1, a)
                if n % 2 == 0:
                    a[i], a[n-1] = a[n-1], a[i]
                else:
                    a[0], a[n-1] = a[n-1], a[0]

        permutate(len(nums), nums)
        return permutation