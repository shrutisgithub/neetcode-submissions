class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2): #bc we are concatenating nums two times 
            for num in nums:
                ans.append(num)
        return ans        
        