// The Basic Solution. 
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        // Define Two Integers.
        // One for the Largest Value.
        int largest = 0;
        // One for the current Value.
        int current = 0;
        // Run a Loop through the nums.
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            // if the current value is 0.
            if (nums[i] == 1) {
                // current count increase by 1
                current++;
            }
            else {
                largest = max(largest, current);
                current = 0;
            }
        }
        // return the largest value by comparing
        return max(largest, current)

    }
};

// The c++ way solution.
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        // Define Two Integers.
        // One for the Largest Value.
        int largest = 0;
        // One for the current Value.
        int current = 0;

        // Define pointer for c++ fast solution
        // To find the locations of the numbers
        int* ptr = nums.data();
        // Just add the size of the nums because it works like (2000h, 2001h, 2002h)
        int* end = ptr + nums.size();

        // Run a Loop through the nums.
        while (ptr < end) {
            // Played with the data if (current=2  + 1) * 1 = 3 while in 0 (current=2  + 0) * 0 = 0 
            current = (current + *ptr) * (*ptr);

            // Find the largest
            largest = max(largest, current);

            ptr++;
        }
        return largest
    }
};