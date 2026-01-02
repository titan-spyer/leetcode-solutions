# 20. Valid Parentheses
s = "(([]){})"



def answer(s):
    a = []
    match = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    for i in s:
        if i in match.values():
            a.append(i)
        elif i in match:
            if not a:
                return False
            if a.pop() != match[i]:
                return False
    if not a:
        return True
    else:
        return False

print(answer(s))