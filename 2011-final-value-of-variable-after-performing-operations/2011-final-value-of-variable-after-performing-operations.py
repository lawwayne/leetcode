class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for e in operations:
            if e == "--X" or e == "X--":
                x-=1
            else:
                x+=1
        return x
            
            
        