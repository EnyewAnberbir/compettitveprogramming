class Solution(object):
    def longestOnes(self, nums, k):
        i, j=0, 0
        res=float('-inf')
        while j<len(nums) and i<len(nums):
            if nums[j] != 1:   
                if k>0:
                    k-=1
                else:
                    while k<0 or nums[i]==1:
                        if nums[i]==0:
                            k+=1
                        i+=1
                    i+=1
            res=max(res,j-i+1)  
            j+=1
        return res
