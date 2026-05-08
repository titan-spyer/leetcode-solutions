// LC: 84 https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        // Define an integer to store the Largest.
        int max_area = 0;
        
        // Define a vector stack.
        int stack[100000];
        int top = -1;
        
        // find the size of array.
        int n = heights.size();

        // Loop through the array.
        for (int i = 0; i < n; i++)
        {
            // compare current index with the last index of stack.
            // Run loop while current is less than last index at stack.
            while (pop >= 0 && heights[i] < heights[stack[top]])
            {
                    // pop the last index.
                    int height = heights[stack[top]];
                    top --;

                    // Calculate the width.
                    int w;
                    if (top == -1)
                    {
                        w = i;
                    }
                    else
                    {
                        w = i - stack[top] - 1;
                    }

                    // calculate the area.
                    int area = height * w;
                    // store the max.
                    if (area > max_area) max_area = area;
            }
            
            // push current index to stack.
            stack[++top] = i;
        }

        // Run another loop until stack empty.
        while (pop >= 0)
        {
                // pop the last index.
                int height = heights[stack[top]];
                top --;

                // Calculate the width.
                int w;
                if (top == -1)
                {
                    w = n;
                }
                else
                {
                    w = n - stack[top] - 1;
                }

                // calculate the area.
                int area = height * w;
                // store the max.
                if (area > max_area) max_area = area;
        }
        // return the max.
        return max_area;
    }
};