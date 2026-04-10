// LC: 1475 https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

class Solution {
public:
    vector<int> finalPrices(vector<int>& prices) {
        // Define an array of size of the prices.
        vector<int> result = prices;

        // Define a monotonic stack.
        int stack[500];
        int top = -1;

        // Grab the memory Data.
        int n = prices.size();

        // Run a loop to itrate through each element.
        for (int i=0;i<n;i++){
            // Run another Loop to check if current element is less than last element at stack.
            while (top >= 0 && prices[i]<=prices[stack[top]]){
                // pop the element from stack.
                int w_i = stack[top];
                // Make subtraction.
                result[w_i] -= prices[i];

                top--;
            } 
            // push the current element to stack.
            stack[++top] = i;
        }

            // return the result.
            return result;
    }
};

// Method-2.
class Solution {
public:
    vector<int> finalPrices(vector<int>& prices) {
        // A Stack that holds raw memory pointers, not indices.
        int* stack[500];
        int top = -1;

        // Grab the physical memory boundaries of the array
        int* ptr = prices.data();
        int* end = ptr + prices.size();

        // Pointer Traversal.
        while (ptr < end) {
            // While the waiting room isn't empty AND current price <= waiting price.
            while (top >= 0 && *ptr <= *stack[top]) {
                // Dereference the top pointer and subtract the current price.
                (*stack[top]) -= *ptr;
                // Pop the pointer off the stack.
                top--;
            }
            // Push the current physical memory address into the waiting room.
            stack[++top] = ptr;
            // Move our iterator forward.
            ptr++;
        }
        // Return the mutated original array! No extra memory used..
        return prices;
    }
};