class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket = {")":"(", "}":"{", "]":"["}
        for c in s:
            if c in bracket:
                if not stack or stack[-1] != bracket[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0
        