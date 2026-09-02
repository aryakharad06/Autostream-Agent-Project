class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping1 = {}
        mapping2 = {}

        for char1, char2 in zip(s, t):

            if char1 in mapping1 and mapping1[char1] != char2:
                return False

            if char2 in mapping2 and mapping2[char2] != char1:
                return False

            mapping1[char1] = char2
            mapping2[char2] = char1

        return True


