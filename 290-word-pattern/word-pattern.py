class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
       
        words = s.split()
        if len(pattern) != len(words):
            return False
        mapping1 = {}
        mapping2 = {}
        for char, word in zip(pattern, words):
        
                if char in mapping1 and mapping1[char] != word:
                    return False
                if word in mapping2 and mapping2[word] != char:
                    return False
                mapping1[char] = word
                mapping2[word] = char

        
        return True