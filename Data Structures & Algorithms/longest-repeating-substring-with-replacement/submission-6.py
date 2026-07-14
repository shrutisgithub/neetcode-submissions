class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #neetcode wale bhaiya suggested this as a main solution, the other one that ive written is the more optimal version of this and is hard to brainstorm
        count = defaultdict(int)
        res = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] += 1
            if (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res        