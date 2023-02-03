class Solution(object):
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        maxSum = 0
        i, j = 0, 0
        high1, high2 = 0, 0
        while i < len(nums) - firstLen + 1:
            high1 = sum(nums[i:i + firstLen])
            if secondLen <= i:
                j = 0
                while j + secondLen <= i:
                    high2 = sum(nums[j:j + secondLen])
                    maxSum = max(maxSum, high1 + high2)
                    j += 1

            if len(nums) - (i + 1) >= secondLen:
                j = 0
                while j + i + secondLen <= len(nums):
                    high2 = sum(nums[i + j + firstLen:i + j + firstLen + secondLen])
                    maxSum = max(maxSum, high1 + high2)
                    j += 1
            i += 1
        return maxSum
