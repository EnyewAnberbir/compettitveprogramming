class Solution(object):
    def maxScore(self, cardPoints, k):
        dis = 0
        for i in range(k):
            dis += cardPoints[i]
         
        high = dis
        for i in range(k):
            dis = dis - cardPoints[k-i-1] + cardPoints[-i-1]
            high = max(dis, high)
                         
        return high
