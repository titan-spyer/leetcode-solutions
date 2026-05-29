# LC3120: Count the number of special characters I : https://leetcode.com/problems/count-the-number-of-special-characters-i/

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        for i in word:
            if i.upper() in word and i.lower() in word:
                word = word.replace(i, "")
                count += 1
        return count

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        char_set = set(word)
        return sum(c in char_set and c.upper() in char_set for c in string.ascii_lowercase)

answer = Solution()
word = "aaAbcBC"
print(answer.numberOfSpecialChars(word))