#include <stdio.h>
#include <stdlib.h>

double *sltMaye(double *a,double *b,double *c);
void print_slt(double *slt, int length);

int main(){
    double a[]={2,1};
    double b[]={3,-1};
    double c[]={8,-1};
    // sltMaye(a,b,c);
    print_slt(sltMaye(a,b,c),2);
    return 0;
}

double *sltMaye(double *a,double *b,double *c){
    double *slt = (double*)malloc(3*sizeof(double));
    double  detD = 0,
            detX = 0,
            detY = 0;
    printf("Slt de Mayer\n");
    /**
     * 00 01
     * 10 11
     * 
     * det = a_00 * a_11 - a_10 * a_01
     */
    detD = a[0]*b[1] - b[0]*a[1];
    printf("D  =  %g\n",detD);

    if(detD != 0){
        // det x
        detX = c[0]*b[1] - b[0]*c[1];
        // det y
        detY = a[0]*c[1] - a[1]*c[0];

        printf("Dx  =  %g\n",detX);
        printf("Dy  =  %g\n",detY);

        slt[0] = detX/detD;
        slt[1] = detY/detD;
        return slt;

    }else{
        printf("Pas se Solution ...\n");
        return NULL; 
    }
    
}

void print_slt(double *slt, int length){
    for(int i=0; i<length; i++)
        printf("%g%c",slt[i], (i == length-1)?'\n':' ');
}