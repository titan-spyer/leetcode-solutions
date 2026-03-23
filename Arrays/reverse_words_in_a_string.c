// #include <stdio.h>
// #include <stdlib.h>
// #include <string.h>

// char * reverseWords(char * s)
// {
//     char *token;
//     // int n = strlen(s);
//     // printf("%d\n", n);
//     char a = ' ';
//     // token = strtok(s, a);
//     printf ("%d\n", strlen(token));
//     while (token != NULL)
//     {
//         for (int i = strlen(s); i > 0; i--)
//         {
//             if (s[i - 1] == ' ')
//             {
//                 char a = s[i];
//                 s[i] = *s;
//                 *s = a;
//                 *s++;
//             }
//         }
//     }
//     return s;
// }

// int main(void)
// {
//     char s[] = "the sky is blue";
//     char* a = reverseWords(s);
//     printf("%s\n", a);
// }