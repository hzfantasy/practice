class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        # init
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            start = i + 1
            end = len(nums) - 1
            last = nums[start]
            while start < end:
                if start != i + 1 and nums[start] == last:
                    start += 1
                    continue
                sum = nums[start] + nums[end] + nums[i]
                if sum > 0:
                    end -= 1
                elif sum < 0:
                    start += 1
                else:
                    res.append([nums[i], nums[start], nums[end]])
                    last = nums[start]
                    start += 1
                    end -= 1
        return res

s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))

# -4 -1 -1 0 1 2
# s s s
# st