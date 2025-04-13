#include <stdio.h>
#include "scopeRules_file1.c"

extern int globalVar;
void myFunc();

int x = 10;

void display() {
    printf("%d\n", x);
}

int main() {
    printf("Value of x is: ");
    display();

    x = 20;
    printf("\nValue of x after modification is: ");
    display();

    globalVar = 30;
    myFunc();

    int a = 40, b = 50;
    printf("a = %d , b = %d\n", a, b);
    {
        int b = 60;

        a++;

        b++;

        printf("a = %d, b = %d\n", a, b);
    }
    return 0;
}