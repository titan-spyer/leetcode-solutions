class Solution {
public:
  vector<int> getConcatenation(vector<int> &nums) {
    // Take the initial snapshot of the array.
    int n = nums.size();

    // Tell C++ to allocate enough memory for double the size upfront
    nums.reserve(2 * n);

    // Iterate through the original array and append each element to the end.
    for (int i = 0; i < n; i++) {
      // Append the element at index i to the end of the vector.
      nums.push_back(nums[i]);
    }
    // Return the concatenated vector.
    return nums;
  }
};