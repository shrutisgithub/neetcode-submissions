class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for elem in strs:
            count = [0]*26
            for c in elem:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(elem)  
        return list(res.values())    