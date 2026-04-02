# 4. Median of Two Sorted Arrays
nums1 = [1,2,3,4]
nums2 = [100,101,102]

def answer(nums1, nums2):
    a, b = 0, min(len(nums1), len(nums2))
    # Calculating the mid point
    m = (len(nums1) + len(nums2)) // 2
    # determine wheather it is a even or odd
    if ((len(nums1) + len(nums2)) % 2) == 0:
        x = 0
    else:
        x = 1
    while a < b:
        m1 = (a + b) // 2
        m2 = m - m1 - 1
        # Check which side was smaller element.
        if nums1[m1 - 1] < nums2[m2]:
            if m1 == 0 or m1 == len(nums1):
                # Do something
                continue
            
    return 0


print(answer(nums1, nums2))