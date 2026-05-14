class Solution:
    def isValid(self, s: str) -> bool:
        stack = [0] * len(s)
        top = 0

        for c in s:
            if c == '(':
                stack[top] = '('
                top += 1
            elif c == '[':
                stack[top] = '['
                top += 1
            elif c == '{':
                stack[top] = '{'
                top += 1
            elif c == ')':
                if top == 0 or stack[top - 1] != '(':
                    return False
                top -= 1
            elif c == ']':
                if top == 0 or stack[top - 1] != '[':
                    return False
                top -= 1
            elif c == '}':
                if top == 0 or stack[top - 1] != '{':
                    return False
                top -= 1

        return top == 0