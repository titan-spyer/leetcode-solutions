// LC1441: Build an Array With Stack Operations

#include <vector>
#include <string>

class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
        // Define a String Vector.
        vector<string> result;

        // Pre allocate the memory so won't get heap memory aloocation problem.
        int exact_size = (2 * target.back()) - target.size();
        result.reserve(exact_size);

        // Get the Pointer Data.
        int* ptr = target.data();
        int* end = ptr + target.size();

        int steam = 1;

        // Loop through the n and end of the target.
        while (steam <= n && ptr < end)
        {
            // Match with target each time.
            if (steam == *ptr)
            {
                // if match found add push to vector.
                result.emplace_back("Push");
                // Increase the pointer value.
                ptr++;
            }
            // else add push then pop to vector.
            else
            {
                result.emplace_back("Push");
                result.emplace_back("Pop");
            }
            // Increase the loop itration value.
            steam++;
        }
        
        // return the vector.
        return result;
    }
};