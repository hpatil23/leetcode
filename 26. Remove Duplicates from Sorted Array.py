class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        else:
            tempnum=nums[0]
            length=1
            for i in range(1,len(nums)):
                if(nums[i]>tempnum):
                    nums[length]=nums[i]
                    length+=1
                    tempnum=nums[i]
            return length
                