class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last = None
        i = 0
        while i < len(nums):
            if last == nums[i]:
                nums.pop(i)
            else:
                last = nums[i]
                i += 1
        return len(nums)


s = Solution()
print(s.removeDuplicates([1, 1, 1]))
