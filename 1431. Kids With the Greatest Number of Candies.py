class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res=list()
        maxCandy=max(candies)
        for candy in candies:
            if candy+extraCandies >=maxCandy:
                res.append(True)
            else:
                res.append(False)
        return res
        