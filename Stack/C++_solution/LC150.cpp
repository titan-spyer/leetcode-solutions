// LC150: https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        // define a Vector int stack.
        vector<int> stack;

        // Loop through the Tokens.
        for (string& token : tokens) {
            // check for arthimetic opearations. (i.e +, -, *, /)
            // If found.
            if (token == "+" || token == "-" || token == "*" || token == "/") {
                // Grab the last two values from the tokens.
                int b = stack.back(); stack.pop_back();
                int a = stack.back(); stack.pop_back();

                // Perform the arthmetic operations.
                // Store the data to result.
                if (token == "+") stack.push_back(a + b);
                else if (token == "-") stack.push_back(a - b);
                else if (token == "*") stack.push_back(a * b);
                else if (token == "/") stack.push_back(a / b);
            }
            // Push the number into stack.
            else
            {
                stack.push_back(stoi(token));
            }
        }
        // Return the result.
        return stack.back();
    }
};

// Solution 2.
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        // Initalize an array for pre allocate memory.
        int stack[10000];
        // Define a physical pointer.
        int top = -1;

        for (const string& token : tokens) {
            // Check for arithmetic value.
            if (token.size() == 1 && token[0] < '0')
            {
                // Grab the last two value.
                int b = stakc[top--];
                int a = stack[top--];

                // Implement a switch statement for calculation.
                switch (token[0])
                {
                case '+': stack[++top] = a + b; break;
                case '-': stack[++top] = a - b; break;
                case '*': stack[++top] = a * b; break;
                case '/': stack[++top] = a / b; break;
                }
            }
            // Else add the number to stack.
            else
            {
                stack[++top] = stoi(token);
            }
        }
        return stack[top];
    }
};