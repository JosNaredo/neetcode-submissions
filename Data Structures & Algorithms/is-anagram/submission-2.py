class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        new_s = {}
        new_t = {}
        for s_, t_ in zip(s, t):
            if new_s.get(s_) != None:
                new_s[s_] += 1
            else:
                new_s[s_] = 1
            if new_t.get(t_) != None:
                new_t[t_] += 1
            else:
                new_t[t_] = 1

        if dict(sorted(new_s.items())) == dict(sorted(new_t.items())):
            return True
        else:
            return False
        