#include <stdio.h>

int main() {
    int i = 10;
    int j = 20;
    const int* p = &i;
    printf("ptr: %d\n", *p);
    p = &j;
    printf("ptr: %d\n", *p);
    const int* const q = &i;
    printf("ptr: %d\n", *q);
    return 0;
}