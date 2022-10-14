class Solution:
    def romanToInt(self, s: str) -> int:
        romanNums = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        
        n = len(s)
        
        result = 0
        
        for i in range(n):
            if i + 1 < n and romanNums[s[i]] < romanNums[s[i+1]]:
                result -= romanNums[s[i]]
            else:
                result += romanNums[s[i]]
        return result