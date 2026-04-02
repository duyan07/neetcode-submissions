class Solution:
    def isValid(self, s: str) -> bool:
        opening = []
        closeToOpen = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        for char in s:
            if char not in closeToOpen:
                opening.append(char)
            else:
                if opening and opening[-1] == closeToOpen[char]:
                    opening.pop()
                else:
                    return False

        return not opening
        