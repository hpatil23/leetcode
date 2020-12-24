class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        temp=0
        sumnums=list()
        for i in range(0,len(nums)):
            temp=temp+nums[i]
            sumnums.append(temp)
        return sumnums