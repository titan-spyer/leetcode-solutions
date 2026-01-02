nums = [-1,0,1,2,-1,-4]

def threesum(nums):
    answer = []
    for i in range(len(nums) - 1):
        if nums[i] + nums[i + 1] <= max(nums[i], nums[i + 1]):
            for j in range(i + 2, len(nums) - 2):
                if nums[i] + nums[i + 1] + nums[j] == 0:
                    answer.append([nums[i], nums[i + 1], nums[j]])
                    break
    return answer

# print(threesum(nums))

def thresum(nums):
    nums.sort()
    answer = []
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            if nums[i] + nums[left] + nums[right] == 0:
                answer.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    right -= 1
                while left < right and nums[right] == nums[right - 1]:
                    left += 1
            elif nums[i] + nums[left] + nums[right] > 0:
                right -= 1
            else:
                left+=1
    return answer

print(thresum(nums))