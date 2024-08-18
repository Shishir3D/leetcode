class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Initialize the stack with the initial state
        stack = [("", 0, 0)]
        result = []

        # Perform DFS using the stack
        while stack:
            current_string, open_count, close_count = stack.pop()

            # If the current string is a valid combination, add it to the result
            if open_count == n and close_count == n:
                result.append(current_string)

            # If we can add an opening parenthesis, do it
            if open_count < n:
                stack.append((current_string + "(", open_count + 1, close_count))

            # If we can add a closing parenthesis, do it
            if close_count < open_count:
                stack.append((current_string + ")", open_count, close_count + 1))

        return result
            
