class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def traverse(i, curr):
            if i >= len(nums):
                res.append(curr[:])
                return
            
            traverse(i + 1, curr)
            curr.append(nums[i])
            traverse(i + 1, curr)
            curr.pop()

        traverse(0, [])
        return res