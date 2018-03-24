class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        if len(nums) == 4:
            if sum(nums) == target:
                return [nums]
            else:
                return []
        result = []
        nums.sort()
        for i in range(len(nums) - 3):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            for j in range(i + 1, len(nums) - 2):
                if j >= i + 2 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    if left <= right - 1 and right < len(nums) - 1 and nums[right] == nums[right + 1]:
                        right -= 1
                        continue
                    if left + 1 <= right and left > j + 1 and nums[left] == nums[left - 1]:
                        left += 1
                        continue

                    sum4 = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum4 == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                    elif sum4 > target:
                        right -= 1
                    else:
                        left += 1
        return result


s = Solution()
print(s.fourSum([-5,5,4,-3,0,0,4,-2], 4))
# [-5,5,4,-3,0,0,4,-2]
# [-3,-2,-1,0,0,1,2,3]
# [-1, -5, -5, -3, 2, 5, 0, 4]
# [-1,2,2,-5,0,-1,4]
# -2 -1 0 0 1 2
# -5 -1 0 1 2 6
# -5 -5 -3 -1 0 2 4 5
