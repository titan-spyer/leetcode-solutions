#include <stdio.h>
#include <stdbool.h>

bool isUgly(int n);

int main(void)
{
    int n;
    printf("Enter an integer value: ");
    scanf("%d", &n);
    bool value = isUgly(n);
    if (value == true) {
        printf("True\n");
    } else if (value == false) {
        printf("False\n");
    }
    return 0;
}

bool isUgly(int n)
{
    if (n < 0)
    {
        return false;
    }
    else if (n <= 7)
    {
        return true;
    }
    while (n > 1)
    {
        /* code */
    }
    
    
}