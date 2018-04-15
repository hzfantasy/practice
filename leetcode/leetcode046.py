class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def get_results(nums):
            n = len(nums)
            if n == 0:
                return []
            if n == 1:
                return [[nums[0]]]
            res = []
            temps = get_results(nums[1:])
            for temp in temps:
                for j in range(len(temp) + 1):
                    t = temp[:]
                    t.insert(j, nums[0])
                    res.append(t)
            return res
        return get_results(nums)


s = Solution()
print(s.permute([1,2,3]))


