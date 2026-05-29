#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minElement(vector<int>& nums) {
        int n = nums.size();
        int* ptr = nums.data();
        int* end = ptr + n;
        while (ptr<end)
        {
            int sum = 0;
            while (*ptr != 0)
            {
                sum += *ptr % 10;
                *ptr /= 10;
            }
            *ptr = sum;
            ptr++;
        }
        return *min_element(nums.begin(), nums.end());
    }
};