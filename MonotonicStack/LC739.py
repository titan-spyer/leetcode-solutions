# LC 739 Daily Temperatures
temperatures = [73,74,75,71,69,72,76,73]

def solution(temperatures):
    # •	Implement two set
    r = len(temperatures)
    stack = []
    days = ([0] * r)
    for l in range(r):
        # •	Compare with the last element(stack) of the stack with current element(ip)
        while stack and (temperatures[stack[-1]] < temperatures[l]):
            # •	Calculate the day count with index values
            days[stack[-1]] = ((l) - stack[-1])
            # •	Remove the index value from stack
            stack.pop()
        stack.append(l)
    return days

print(solution(temperatures))