class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        buf = []
        res = 0

        for token in tokens:
            if self._is_arithmetric(token):
                buf.append(token)
            else:
                l = int(buf.pop())
                f = int(buf.pop())
                if token == "+":
                    res = f + l
                elif token == "-":
                    res = f - l
                elif token == "*":
                    res = f * l
                else:
                    res = int(f / l)
                buf.append(res)
            
        return int(buf[0])
        
    def _is_arithmetric(self, token: str) -> bool:
        if token == "+" or token == "-" or token == "*" or token == "/":
            return False
        return True