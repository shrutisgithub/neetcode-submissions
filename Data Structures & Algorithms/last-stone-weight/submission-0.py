class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #brute force approach using sorting
        while len(stones) > 1:
            stones.sort()
            cur = stones.pop() - stones.pop()
            if cur:
                stones.append(cur)
        return stones[0] if stones else 0
        