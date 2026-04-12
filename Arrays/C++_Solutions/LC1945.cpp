#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int getLucky(string s, int k) {
        // Step 1: Convert each character to its position in alphabet (a=1, b=2, etc.)
        string resu = "";  // Fixed: changed '' to ""
        
        for (int i = 0; i < s.length(); i++) {
            resu += to_string(s[i] - 'a' + 1);  // Fixed: added to_string() and proper calculation
        }
        
        // Step 2: Apply digit sum transformation k times
        int result = 0;
        
        // First convert string to initial number sum
        for (char c : resu) {
            result += (c - '0');
        }
        
        // Apply remaining k-1 transformations
        for (int i = 1; i < k; i++) {
            int sum = 0;
            while (result > 0) {
                sum += result % 10;
                result /= 10;
            }
            result = sum;
        }
        
        return result;
    }
};

// Main function for testing
int main() {
    Solution solution;
    
    // Test case 1
    string s1 = "iiii";
    int k1 = 1;
    int result1 = solution.getLucky(s1, k1);
    cout << "Input: s = \"" << s1 << "\", k = " << k1 << endl;
    cout << "Output: " << result1 << endl;
    cout << "Expected: 36" << endl << endl;
    
    // Test case 2
    string s2 = "leetcode";
    int k2 = 2;
    int result2 = solution.getLucky(s2, k2);
    cout << "Input: s = \"" << s2 << "\", k = " << k2 << endl;
    cout << "Output: " << result2 << endl;
    cout << "Expected: 6" << endl << endl;
    
    // Test case 3
    string s3 = "zbax";
    int k3 = 2;
    int result3 = solution.getLucky(s3, k3);
    cout << "Input: s = \"" << s3 << "\", k = " << k3 << endl;
    cout << "Output: " << result3 << endl;
    cout << "Expected: 8" << endl;
    
    return 0;
}
