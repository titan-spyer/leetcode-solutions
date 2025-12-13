s = "pwwkew"

def lswrc(s):
    left = 0
    ans = 0
    chunks = ''
    for i in range(len(s)):
        if s[i] not in chunks:
            chunks += s[i]
            if chunks in s:
                ans = len(chunks)
        else:
            ans = 0
            chunks = s[i]
    return ans

print(lswrc(s))