class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for token in tokens:
            if token not in ("+", "-", "*", "/"):
                nums.append(int(token))
            else:
                val = nums.pop()
                if token == "+":
                    nums[-1] += val
                elif token == "-":
                    nums[-1] -= val
                elif token == "*":
                    nums[-1] *= val
                else:
                    nums[-1] = int(nums[-1] / val)
        
        return nums[0]