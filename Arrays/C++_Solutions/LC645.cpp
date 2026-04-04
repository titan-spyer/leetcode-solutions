class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int duplicate = -1, missing = -1;
        
        // Find the pointer value to itrate
        int* start = nums.data();
        int* end = start + nums.size();

        int* ptr = start;
        while (ptr < end) {
            int val = abs(*ptr);

            int* target = start + (val - 1);

            if (*target < 0) {
                duplicate = val;
            }
            else {
                *target = -(*target);
            }
            ptr++;
        }

        ptr = start;
        while (ptr < end)
        {
            if (*ptr > 0) {
                missing = (ptr - start) + 1;
                break;
            }
            ptr++;
        }
        
        return {duplicate, missing};
    }
};