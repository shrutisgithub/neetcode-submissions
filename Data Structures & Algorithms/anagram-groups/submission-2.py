class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for elem in strs:
            char = [0] * 26
            for ch in elem:
                char[ord(ch) - ord("a")]+=1
            res[tuple(char)].append(elem)
        return list(res.values())

        