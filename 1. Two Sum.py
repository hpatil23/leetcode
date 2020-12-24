class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data={}
        i=0
        for num in nums:
            if target-num in data:
                return [data[target-num],i]
            else:
                data[num]=i
                i+=1
        
        