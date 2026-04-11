// LC: 739 https://leetcode.com/problems/daily-temperatures/

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int r = temperatures.size();
        vector<int> days(r, 0);
        
        // Raw array on the Stack
        int stack[100000]; 
        int top = -1; // Our physical pointer
        
        for (int l = 0; l < r; l++) {
            
            // While stack has items AND current temp > temp at waiting index
            while (top >= 0 && temperatures[stack[top]] < temperatures[l]) {
                
                // Grab the waiting index
                int waiting_index = stack[top];
                
                // Calculate and store the difference in days
                days[waiting_index] = l - waiting_index;
                
                // Pop the pointer
                top--;
            }
            
            // Push current index into the waiting room
            stack[++top] = l;
        }
        
        return days;
    }
};