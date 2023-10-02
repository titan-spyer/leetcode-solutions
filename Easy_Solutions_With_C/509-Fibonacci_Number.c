// This program is for printing the Fibonacci Number Using Recursion
// The header file you need most
#include <stdio.h>

// Declaring a function to complete the recursion
int fib(int n);

// Main function for printing and providing the value to "fib" function
int main(void)
{
  int num;
  printf("Enter an integer value: ");
  scanf("%d", &num);
  int value = fib(num);
  printf("Fibonacci: %d\n", value);
  return 0;
}

// Defining the function for Fibonacci number
int fib(int n)
{
  // Base function for Recursion
  if (n == 0 || n == 1) // Here it means that we know the fibonacci of 0 or 1 is itself 0 and 1 so if the number becomes one of them return the number
  {
    return n;
  }
  // This is recursive function based on base function it means it the number isn't 0 || 1 subtract the number by 1 and subtract the number also by 2 it will gives us value to make addition between two of the value 
  return fib(n - 1) + fib(n - 2);
}