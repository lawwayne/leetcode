class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1New = ''.join(word1)
        word2New = ''.join(word2)
        if word1New == word2New:
            return True
        else:
            return False
        