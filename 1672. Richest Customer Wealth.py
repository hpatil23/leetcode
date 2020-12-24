class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        if not accounts:
            return 0
        maxSum=0
        for i in range(0,len(accounts)):
            temp=sum(accounts[i])
            if(maxSum<temp):
                maxSum=temp
        return maxSum