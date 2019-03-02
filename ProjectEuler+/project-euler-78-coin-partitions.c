#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    long mf = 1000000007l;
    int ub = 60001;
    unsigned long pc[ub];
    pc[0] = 1l;
    for (int k=1; k<ub; k++)
        pc[k] = 0l;
    for (int k=1; k<ub; k++) {
        for (int n=k; n<ub; n++) {
            pc[n] += (pc[n-k]%mf);
        }
    }
    int t = 0;
    scanf("%d\n", &t);
    for (int i=0; i<t; i++) {
        int n = 0;
        scanf("%d\n", &n);
        printf("%lu\n", pc[n]);
    }
    return 0;
}
