#include <iostream>
#include <vector>
// LC: 448. Find All Numbers Disappeared in an Array

class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        // Initalize the Vector Result.
        vector<int> result;

        // Grab the Memory data.
        int* start = nums.data();
        int* end = start + nums.size();

        // First phase to detect Duplicates.
        // Define the starting adress.
        int* ptr = start;
        // Run the Loop till end.
        while (ptr < end)
        {
            // get the absoulate Value of current.
            int value = abs(*ptr);
    
            // Calculate the physical adress of the target index
            int* target = start + (value - 1);
    
            // if the number is posetive flip the sign bit.
            // if the Number is negative do nothing.
            if (*target > 0)
            {
                // Flip the sign bit.
                *target = -(*target);
            }
            
            ptr++;
        }
        

        // Reinitialize the pointer address.
        ptr = start;
        // Run second loop to store the result.
        while (ptr < end)
        {
            // Find the posetive numbers.
            if (*ptr > 0)
            {
                // Pointer math: (Current Address - Base Address) + 1 gives the missing value.
                result.push_back((ptr - start) + 1);
            }
            ptr++;
        }
        
        // return result.
        return result;

    }
};