class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
            else:
                n2 = stack.pop()
                n1 = stack.pop()

                if token == "+":
                    stack.append(n1 + n2)

                elif token == "-":
                    stack.append(n1 - n2)

                elif token == "*":
                    stack.append(n1 * n2)

                elif token == "/":
                    stack.append(int(n1 / n2))

        return stack[0]