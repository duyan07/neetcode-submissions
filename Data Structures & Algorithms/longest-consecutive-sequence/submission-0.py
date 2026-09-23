class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        nums = set(nums)

        for num in nums:
            if num - 1 not in nums:
                curr_len = 1
                curr_num = num + 1
                while curr_num in nums:
                    curr_len += 1
                    curr_num += 1
                max_len = max(max_len, curr_len)
        
        return max_len