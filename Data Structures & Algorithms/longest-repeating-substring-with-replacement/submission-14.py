class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        resp = 0
        ss = set(s)
        for c in ss:
            l = count = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1

                resp = max(resp, r-l+1)
     
        return resp