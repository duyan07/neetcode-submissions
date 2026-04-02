class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        open_brackets = []

        for char in s:
            if char not in brackets:
                open_brackets.append(char)
            elif open_brackets and open_brackets[-1] == brackets[char]:
                open_brackets.pop()
            else: 
                return False
        
        return True if not open_brackets else False