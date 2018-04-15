class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ""
        addition = 0
        len_a, len_b = len(a), len(b)
        if len_a > len_b:
            b = '0' * (len_a - len_b) + b
        else:
            a = '0' * (len_b - len_a) + a

        for i in range(len(a) - 1, -1, -1):
            temp_res = int(a[i]) + int(b[i]) + addition
            if temp_res >= 2:
                res = str(temp_res - 2) + res
                addition = 1
            else:
                res = str(temp_res) + res
                addition = 0
        if addition >= 1:
            res = str(addition) + res
        return res


s = Solution()
print(s.addBinary("1", "111"))
