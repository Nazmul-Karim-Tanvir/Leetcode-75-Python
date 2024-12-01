class Solution(object):
    def margeAlternately(self,word1,word2):
        result = ""
        
        maxString = max(len(word1), len(word2))
        
        for i in range(maxString):
            if i < len(word1):
                result += word1[i]
            if i < len(word2):
                result += word2[i]
        
        return result
        
solution = Solution()
result1 = solution.margeAlternately("abc","pqrst")
result2 = solution.margeAlternately("ab","pqrs")
result3 = solution.margeAlternately("abcd","pq")

# print statements
print((True, result1) if result1 == "apbqcrst" else (False, "Expected result is 'apbqcrst' but found " + result1))
print((True, result2) if result2 == "apbqrs" else (False, "Expected result is 'apbqrs' but found " + result2))
print((True, result3) if result3 == "apbqcd" else (False, "Expected result is 'apbqcd' but found " + result3))