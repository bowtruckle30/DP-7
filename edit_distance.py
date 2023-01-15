class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        ## T.C = O(m.n)
        ## S.C = O(m.n)
        
        m = len(word1) + 1
        n = len(word2) + 1

        if m > n:
            return self.minDistance(word2, word1)
        
        dp = [[0]*n for i in range(m)]

        ## first row
        for i in range(n):
            dp[0][i] = i

        ## first col
        for i in range(m):
            dp[i][0] = i

        for i in range(1, m):
            for j in range(1, n):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

        #print(dp)
        return dp[-1][-1]






