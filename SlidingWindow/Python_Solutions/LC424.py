# Longest Repeating Character Replacement
s = "ABAB" 
k = 2

def answer(s, k):
    left = 0
    ans = 0
    max_freq = 0
    freq = {}
    for right in range(len(s)):
        if s[right] in freq:
            freq[s[right]] += 1
        else:
            freq[s[right]] = 1
        max_freq = max(max_freq, freq[s[right]])
        if (right - left + 1) - max_freq <= k:
            ans = right - left + 1
        while (right - left + 1) - max_freq > k:
            left += 1
            freq[s[left]] -= 1
    return ans

print(answer(s, k))