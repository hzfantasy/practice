class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []




s = Solution()
print(s.generateParenthesis(3))

# (((0)1)2)
# (()())
# (())()
# ()  ( ())
# ()  ()()

# ( ( ( ( ) ) ) )
# ( ( ( )     ( ) ) )
# ( ( ( ) )   ( ) )
# ( ( ( ) ) ) ( )

# ( ( )      ( ( ) ) )
# ( ( ) )    ( ( ) )


# n