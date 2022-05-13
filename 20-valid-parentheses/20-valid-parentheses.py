class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closetoOpen={")":"(", "]":"[", "}":"{"}
        
        for c in s:
            if c in closetoOpen:
                if stack and stack[-1] == closetoOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
            
# The Time Complexity is O(n) as for any given string we are taking a linear search approach. 
# The Space Complexity is also O(n) as the stack does take a bit of memory and it is necessary in order to keep track of each parentheses value.
# For the lower bound it would be Ω(1) and that is only if the string itself would be empty. 

            
        

                
        
                
        
