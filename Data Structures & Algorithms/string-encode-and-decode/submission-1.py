class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs != []:
            return '*sep*'.join(strs)
        else:
            return 'empty'
    def decode(self, s: str) -> List[str]:
        if s == 'empty':
            return []
        else:
            return s.split('*sep*')