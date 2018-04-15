class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def travel(s='', left=0, right=0):
            if len(s) == n*2:
                res.append(s)
                return
            if left < n:
                travel(s + '(', left + 1, right)
            if right < left:
                travel(s + ')', left, right + 1)

        travel()
        return res




#                       (
#          ((                    ()
#  (((              (()
#    ((()      (()(      (())
#      ((())      (()()
#        ((()))      (()())