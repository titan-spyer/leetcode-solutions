# LC788: Rotate Digits.

# Solution 1 : Math Type.
class Solution:
    def rotatedDigits(self, n: int) -> int:
        # Assigning Invalid Number.
        invalid = {3, 4, 7}
        # Filtering Good Numbers.
        filters = {2, 5, 6, 9}
        # COunter.
        good_count = 0
        # Loop Through the number.
        for i in range(1, n + 1):
            # Assign a validator for each number.
            good = False
            num = i
            # Check the number is Good or not.
            while num > 0:
                # Unary Slicing for each number Validation.
                digit = num % 10
                # Check is Valid.
                if digit in invalid:
                    good = False
                    break
                # Check is a good Number.
                else:
                    if digit in filters:
                        good = True
                # Number Slicing.
                num //= 10
            # IF good count by 1.
            if good:
                good_count += 1
        # Return the number.
        return good_count

# Solution 2 : Pythonic way.
class Solution:
    def rotatedDigits(self, n: int) -> int:
        # Counter.
        good_count = 0
        # Assigning Invalid Number.
        invalid = {'3', '4', '7'}
        # Filtering Good Numbers.
        filters = {'2', '5', '6', '9'}
        # Loop Through the number to calculate the good.
        for i in range(1, n + 1):
            # Convert Number to string.
            num = set(str(i))
            # Check is Valid and a good number.
            if num.isdisjoint(invalid) and not num.isdisjoint(filters):
                good_count += 1
        # Return the number.
        return good_count

sol = Solution()
print(sol.rotatedDigits(10))