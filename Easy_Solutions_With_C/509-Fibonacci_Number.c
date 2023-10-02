#include <stdio.h>
int fib(int n);
int main(void) {
    int num;
    printf("Enter an integer value: ");
    scanf("%d", &num);
    int value = fib(num);
    printf("Fibonacci: %d\n", value);
    return 0;
}



int fib(int n){
  if ( n == 0 || n == 1)
  {
    return n;
  }
  return fib(n - 1) + fib(n - 2); 
}