#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char * reversevowel(char *s)
{
    int i = strlen(s);
    char *a = s;
    int j = i - 1;
    i--;
    j--;
    while (*s != '\0')
    {
        if (*s == 'a' || *s == 'e' || *s == 'i' || *s == 'o' || *s == 'u')
        {
            char te = s[j];
            s[j] = *s;
            *s = te;
        }
        j--;
        i--;
        *s++;
    }
    return a;
}
int main(void)
{
    char s[] = "leetcode";
    char *a = reversevowel(s);
    printf("%s\n", a);
}