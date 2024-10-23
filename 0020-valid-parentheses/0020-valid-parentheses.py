class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in "[{(":
                stack.append(char)
                pass
            else:
                if not stack or \
                (char == ")" and stack[-1] != "(") or \
                (char == "]" and stack[-1] != "[") or \
                (char == "}" and stack[-1] != "{"):
                    return False
                stack.pop()
        return not stack