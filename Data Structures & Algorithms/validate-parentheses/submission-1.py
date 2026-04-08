class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for b in s:
            if b == "(" or b == "{" or b == "[":
                stack.append(b)
                continue

            if len(stack) == 0:
                return False
            else:
                last = stack.pop()
                if last == "(" and b == ")":
                    continue
        
                if last == "{" and b == "}":
                    continue

                if last == "[" and b == "]":
                    continue
                
                return False
        
        return True if len(stack) == 0 else False
