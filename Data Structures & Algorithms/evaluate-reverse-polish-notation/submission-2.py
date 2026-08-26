class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operator = ('+', '-', '*', '/')

        for char in tokens:

            if char not in operator:
                stack.append(int(char))
                continue

            right = stack.pop()
            left = stack.pop()

            match char:
                case '+':
                    result = left + right

                case '-':
                    result = left - right

                case '*':
                    result = left * right

                case '/':
                    result = int(left / right)

            stack.append(result)

        return stack[-1]
                
            