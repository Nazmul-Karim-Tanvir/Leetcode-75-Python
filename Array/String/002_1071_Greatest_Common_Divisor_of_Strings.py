class Solution:
    
    def gcd(self,a:int,b:int)->int:
        while b!=0:
            a, b = b, a % b
        return a
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        result =""
        if str1+str2 != str2+str1:
            return result
        
        gcdLength = self.gcd(len(str1), len(str2))
        result = str1[:gcdLength]
        return result
    

solution = Solution()
str1 = "ABCABC"
str2 = "ABC"
print( solution.gcdOfStrings(str1, str2))

solution = Solution()
str1 = "ABABAB"
str2 = "AB"
print( solution.gcdOfStrings(str1, str2))

solution = Solution()
str1 = "LEET"
str2 = "CODE"
print( solution.gcdOfStrings(str1, str2))