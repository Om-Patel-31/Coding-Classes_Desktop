#include <stdio.h>

#define varNum 10

enum NUMS { num = 30};

int main() {
    const int a = 1;
    printf("The value of a is: %d\n", a);
    printf("The value of varNum is: %d\n", varNum);
    #ifdef varNum
    #undef varNum
    #define varNum 20
    #endif
    printf("%d", varNum);
    printf("The value of num is: %d\n", num);
}