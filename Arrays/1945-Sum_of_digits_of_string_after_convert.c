#include <stdio.h>

int getLucky(char *s, int k);

int main(void) {
    char * let = "hvmhoasabaymnmsd";
    int k;
    printf("Enter an integer value: ");
    scanf("%d", &k);
    int n = getLucky(let, k);
    printf("%d\n", n);
    return 0;
}

int getLucky(char *s, int k)
{
    int value  = 0;
    for (int j = 0; j < 100; j++)
    {
        if (s[j] == '\0')
        {
            break;
        }
        int deci;
        int value1 = 0;
        for (char ak = 'a'; ak <= 'z'; ak++)
        {
        if (s[j] == ak)
        {
        deci = ak - 'a' + 1;                
        while (deci > 9)
        {
            int num = deci % 10;
            deci /= 10;
            deci += num;
        }
        value1 += deci;
        break;
        }
    }
    value += value1;             
    }
    if (k != 1)
    {
        int value2 = 0;
        for (int i = 1; i < k; i++)
        {
            while (value > 9)
            {
                int num = value % 10;
                value /= 10;
                value += num;

            }
        value += value2;
        if (value <= 9)
        {
            return value;
        }
        }
    }
    return value;       
}