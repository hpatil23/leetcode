class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first=0
        second=0
        if nums[0]>nums[1]:
            first=nums[0]
            second=nums[1]
        else:
            first=nums[1]
            second=nums[0]
        
        for i in range(2,len(nums)):
            if(nums[i]>first):
                second=first
                first=nums[i]
            elif(nums[i]>second):
                second=nums[i]
        return (first-1)*(second-1)
        