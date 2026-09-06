class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = "+-*/"
        stack = []
        for token in tokens:
            if token in operators:
                a = stack.pop()
                b = stack.pop()
                res = 0
                match token:
                    case "+":
                        res = a + b 
                    case "-":
                        res = b - a
                    case "*":
                        res = a * b
                    case "/":
                        res = int(float(b) / a)
                stack.append(res)
            else:
                stack.append(int(token))
        
        return stack[-1]
        