class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}
        for word in strs:
            key = tuple(sorted(word))
            groups.setdefault(key, []).append(word)
        return list(groups.values())


        