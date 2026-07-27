class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(set(s)) == 1:
            return 1
        if s == "":
            return 0
        len_substring = []
        uniq = []
        for i in range(len(s)):
            count = 1
            uniq.append(s[i])
            for j in range(i+1, len(s)):
                if s[j] not in uniq:
                    count += 1
                    uniq.append(s[j])
                else:
                    uniq =[]
                    len_substring.append(count)
                    break
            len_substring.append(count)
        return max(len_substring)

        
            