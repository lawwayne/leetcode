class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        new = string.split()
        for e in new:
            if e[::-1] == e:
                return True
        return False
        