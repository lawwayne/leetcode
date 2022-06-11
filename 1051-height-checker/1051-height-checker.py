class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        expected = sorted(heights)
        for e in range(len(heights)):
            if expected[e] != heights[e]:
                count+=1
            
        return count
            