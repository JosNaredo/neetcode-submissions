class Solution:
    def isValid(self, s: str) -> bool:
        # ( must follow )
        # { must follow }
        # [ must follow ]

        open_ = ['(', '{', '[']
        close = [')', '}', ']']
        correspondance = {
            '(':')',
            '{':'}', 
            '[':']'
        }
        need_closure = []
        for i, element in enumerate(s):
            if i == 0 and element in close or len(s) % 2 != 0:
                return False
            
            if element in open_:
                need_closure.append(element)
            elif element in close and need_closure == []:
                return False
            elif element in close and need_closure != []:
                need_to_be_closed_first = need_closure.pop()
                if correspondance[need_to_be_closed_first] != element:
                    return False
            else:
                return False
        if need_closure != []:
            return False
        return True
