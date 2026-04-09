// LC636: https://leetcode.com/problems/exclusive-time-of-functions/

class Solution {
public:
    vector<int> exclusiveTime(int n, vector<string>& logs) {
        // Define an Int array with the help of n because function is constant to return.
        vector<int> result(n, 0);

        int stack[5000];
        int top = -1;

        int prev_time = 0;
        for (const string& log : logs) {
            int i = 0;
            int id = 0;
            while (log[i] != ':') {
                id = id * 10 + (log[i] - '0');
                i++;
            }

            i++;

            bool isstart = (log[i] == 's');

            while (log[i] != ':')
            {
                i++;
            }

            i++;

            int time = 0;
            while (i < log.size())
            {
                time = time * 10 + (log[i] - '0');
                i++;
            }
            
            if (isstart) {
                if (top >= 0) {
                    result[stack[top]] += time - prev_time;
                }
                stack[++top] = id;
                prev_time = time;
            }
            else
            {
                result[stack[top]] += time - prev_time + 1;
                top--;
                prev_time = time + 1;
            }
            
        }
        return result;
    }
};