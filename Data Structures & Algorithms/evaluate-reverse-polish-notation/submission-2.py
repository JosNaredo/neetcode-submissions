class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = ["+", "-", "*", "/"]
        for token in tokens:
            if token not in operator:
                stack.append(int(token))
            else:
                # count = eval(f' {token} '.join(stack))
                two = stack.pop()
                one = stack.pop()
                count_str = '{} {} {}'.format(str(one), token, str(two))
                stack.append(int(eval(count_str)))
                
        
        return int(stack[0])

