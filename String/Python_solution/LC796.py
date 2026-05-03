# LC796: Rotate String.

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Base Case.
        # IF both len doesn't match then it never can't be the same.
        if len(s) != len(goal):
            return False
        # return if it's a subset of s 
        return goal in (s + s)