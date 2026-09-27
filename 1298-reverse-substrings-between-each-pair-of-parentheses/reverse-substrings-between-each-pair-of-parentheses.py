class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
      
        for char in s:
            if char == ")":
               
                temp_chars = []
              
                
                while stack[-1] != "(":
                    temp_chars.append(stack.pop())
              
                stack.pop()
              
                stack.extend(temp_chars)
            else:
                stack.append(char)

        return "".join(stack)
