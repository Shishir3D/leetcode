class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = ['+', '-', '*', '/']
        stack = []

        for item in tokens:
            if item in operands:
                secondItem = int(stack.pop())
                firstItem = int(stack.pop())
                if item == "+":
                    newItem = firstItem + secondItem
                elif item == "-":
                    newItem = firstItem - secondItem
                elif item == "*":
                    newItem = firstItem * secondItem
                elif item == "/":
                    newItem = int(firstItem / secondItem)
                stack.append(newItem)
            else:
                stack.append(int(item))            

        return stack[0]

