#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void reverseString(char* s, int sSize){
    sSize--;
    while (sSize > 0)
    {
        char a = s[sSize];
        s[sSize] = *s;
        *s = a;
        s++;
        sSize--;
        sSize--;
    }
}

int main(void)
{
    char s[] = "hello";
    int sSize = strlen(s);
    reverseString(s, sSize);
    printf("%s\n", s);
}