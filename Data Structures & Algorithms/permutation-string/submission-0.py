class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = {}
        window = {}

        # frequency of s1
        for c in s1:
            need[c] = need.get(c, 0) + 1

        left = 0
        for right in range(len(s2)):
            char = s2[right]
            window[char] = window.get(char, 0) + 1

            # keep window size equal to len(s1)
            if right - left + 1 > len(s1):
                left_char = s2[left]
                window[left_char] -= 1
                if window[left_char] == 0:
                    del window[left_char]
                left += 1

            # compare maps
            if window == need:
                return True

        return False
