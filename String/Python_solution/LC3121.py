# LC3121: Count the Number of Special Characters II : https://leetcode.com/problems/count-the-number-of-special-characters-ii/

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_lower = {}
        first_upper = {}
        
        for i, char in enumerate(word):
            if char.islower():
                last_lower[char] = i
            else:
                if char not in first_upper:
                    first_upper[char] = i
                    
        count = 0
        for char in last_lower:
            upper_char = char.upper()

            if upper_char in first_upper and last_lower[char] < first_upper[upper_char]:
                count += 1
                
        return count
answer = Solution()
qes = "aaAbcBC"
print(answer.numberOfSpecialChars(qes))