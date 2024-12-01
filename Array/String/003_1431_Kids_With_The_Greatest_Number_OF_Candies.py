from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        result=[]
        max_candies = max(candies)
        for candy in candies:
            result.append(candy + extraCandies >= max_candies)
    
        return result
        
        
solution = Solution()

result = solution.kidsWithCandies([2,3,5,1,3],3)
result1 = solution.kidsWithCandies([4,2,1,1,2],1)
print(result)
print(result1)