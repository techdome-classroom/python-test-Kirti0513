class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
         stack = []
        bracket_mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_mapping.values():
                stack.append(char)
            elif char in bracket_mapping.keys():
                if stack == [] or bracket_mapping[char] != stack.pop():
                    return False
            else:
                return False

        return stack == []

sol = Solution()
print(sol.isValid("()"))        
print(sol.isValid("()[]{}"))   
print(sol.isValid("(]")) 
    



  

