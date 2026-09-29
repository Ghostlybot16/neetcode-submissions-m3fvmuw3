class Solution:
    def isValid(self, s: str) -> bool:
        
        my_dict = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        
        stack = []

        for bracket in s: # Iterate through all the brackets in the string s 
            if bracket in my_dict: # Check if the current bracket is a closing one and if it exists in the dict
                if stack and stack[-1] == my_dict[bracket]:
                    stack.pop() # Remove bracket from stack if stack is not empty and the last element in stack is the closing bracket
                else:
                    return False # Brackets don't match
            else:
                stack.append(bracket) # Add bracket since it'll be an open bracket
        
        return True if not stack else False # Return true if stack is empty, else False


                


