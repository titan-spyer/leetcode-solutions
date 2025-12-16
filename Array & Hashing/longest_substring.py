s = "pwwkew"

def lswrc(s):
    left = 0
    chunks = set()
    ans = 0

    for r in range(len(s)):
        while s[r] in chunks:
            chunks.discard(s[left])
            left += 1
        chunks.add(s[r])
        ans = max(ans, r - left +1)
    return ans

print(lswrc(s))