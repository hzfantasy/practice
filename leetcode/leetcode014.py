class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        common_prefix = strs[0]
        for str in strs:
            if str == '':
                return ''
            common_prefix = self.get_common_prefix(common_prefix, str)
        return common_prefix

    @staticmethod
    def get_common_prefix(common_prefix, str):
        if str == '' or common_prefix == '':
            return ''
        for i in range(len(common_prefix)):
            if len(str) < i + 1 or common_prefix[i] != str[i]:
                return common_prefix[:i]
        return common_prefix


s = Solution()
print(s.longestCommonPrefix([]))

# str st s
# s s s
# st