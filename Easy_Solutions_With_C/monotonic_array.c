#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool isMonotonic(int* nums, int numsSize){
    // int i = 0, j = 0;
    // for (int k = 0; k < numsSize; k++)
    // {
    //     if(*nums > nums[+1]) i++;
    //     else if (*nums < nums[+1]) j++;
    //     else if (*nums == nums[+1])
    //     {
    //         i++;
    //         j++;
    //     }
    //     *nums++;
    // }
    // if (i == (numsSize)) return true;
    // else if (j == (numsSize)) return true;
    // else return false;
    bool i = true;
    bool j = true;
    while (numsSize > 0)
    {
        if(*nums > nums[+1]) i = false;
        else if (*nums < nums[+1]) j = false;
        *nums++;
        numsSize--;
    }
    if (!i && !j) 
    {
        return false;
    }
    return true;

}
int main(void) {
    int arr[] = {1,4,2,3};
    int n = sizeof(arr) / 4;
    bool value = isMonotonic(arr, n);
    if (value == true) {
        printf("True\n");
    } else if (value == false) {
        printf("False\n");
    }
    return 0;
}