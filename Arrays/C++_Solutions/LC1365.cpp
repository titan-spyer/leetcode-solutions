#include <vector>
#include <iostream>
using namespace std;

// LC: 1365. How Many Numbers Are Smaller Than the Current Number
class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        // Solved using Frequency Map
        // Three Phase
        // allocate the stack memory for Frequency Map
        int count[102] = {0};

        // Calculate the Nums size
        int n = nums.size();

        // Get the Starting Pointer Data.
        int* ptr = nums.data();

        // Calculate the end pointer Data.
        int* end = ptr + n;  // FIXED: was n + ptr, changed to ptr + n

        // First Phase: Count the Frequency
        while (ptr < end) {
            count[*ptr]++;
            ptr++;
        }

        // For prefix sum initialize the Variable.
        int prefix_sum = 0;  // FIXED: Added missing semicolon

        // Second Phase: Count the prefix Sum
        for (int i = 0; i < 101; i++) {  // FIXED: Changed to 101 to cover values 0-100
            // Initialize a temp variable assign the index value.
            int temp = count[i];
            // Assign the prefix sum to the location to that pointer.
            count[i] = prefix_sum;
            // Increase the prefix sum by it's Temp value
            prefix_sum += temp;
        }

        // PreAllocate the exact memory for Result.
        vector<int> result(n);
        // Get the pointer Data for that Result.
        int* res_ptr = result.data();

        // Third Phase: store the Result
        // Reassign the Pointer location for 3rd loop.
        ptr = nums.data();
        // Run a loop for final result using Fast pointer Traversal.
        while (ptr < end) {
            // Write the answer to the result pointer location.
            *res_ptr = count[*ptr];
            // Increase the result.
            res_ptr++;
            // Increase the Pointer.
            ptr++;
        }

        // Return the Result.
        return result;
    }
};

// Helper function to print vector
void printVector(const vector<int>& vec) {
    cout << "[";
    for (size_t i = 0; i < vec.size(); i++) {
        cout << vec[i];
        if (i < vec.size() - 1) cout << ", ";
    }
    cout << "]";
}

int main() {
    Solution solution;
    
    // Test Case 1
    vector<int> nums1 = {8, 1, 2, 2, 3};
    cout << "Input: ";
    printVector(nums1);
    vector<int> result1 = solution.smallerNumbersThanCurrent(nums1);
    cout << "\nOutput: ";
    printVector(result1);
    cout << "\nExpected: [4, 0, 1, 1, 3]\n\n";
    
    // Test Case 2
    vector<int> nums2 = {6, 5, 4, 8};
    cout << "Input: ";
    printVector(nums2);
    vector<int> result2 = solution.smallerNumbersThanCurrent(nums2);
    cout << "\nOutput: ";
    printVector(result2);
    cout << "\nExpected: [2, 1, 0, 3]\n\n";
    
    // Test Case 3
    vector<int> nums3 = {7, 7, 7, 7};
    cout << "Input: ";
    printVector(nums3);
    vector<int> result3 = solution.smallerNumbersThanCurrent(nums3);
    cout << "\nOutput: ";
    printVector(result3);
    cout << "\nExpected: [0, 0, 0, 0]\n\n";
    
    // Test Case 4
    vector<int> nums4 = {0, 0, 1, 1, 2};
    cout << "Input: ";
    printVector(nums4);
    vector<int> result4 = solution.smallerNumbersThanCurrent(nums4);
    cout << "\nOutput: ";
    printVector(result4);
    cout << "\nExpected: [0, 0, 2, 2, 4]\n";
    
    return 0;
}