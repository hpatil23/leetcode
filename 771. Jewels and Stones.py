class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        data={}
        for j in jewels:
            data[j]=1
        
        count=0
        for s in stones:
            if s in data:
                count+=1
        return count
        