// LC1470 : Shuffle the Array.

class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        
        // STEP 1: Pack both halves into the first half of the array
        for (int i = 0; i < n; i++) {
            // nums[i] is 'x', nums[i+n] is 'y'
            nums[i] = nums[i] | (nums[i + n] << 10);
        }
        
        // STEP 2: Unpack from right to left to avoid overwriting our packed data
        for (int i = n - 1; i >= 0; i--) {
            
            // Extract 'y' by shifting right, and place it in the odd index
            nums[2 * i + 1] = nums[i] >> 10;
            
            // Extract 'x' using the 1023 mask, and place it in the even index
            nums[2 * i] = nums[i] & 1023; 
        }
        
        return nums;
    }
};