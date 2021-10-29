#include<stdio.h>

int main(){
   int TM_matrix[10][10];
   int i, j;
   for(i=1; i<11; i++) {
      for(j=1; j<11;j++) {
         TM_matrix[i-1][j-1] = i*j;
      }
   }
   //Displaying array elements
   printf("Matrix elements:\n");
   for(i=0; i<10; i++) {
      for(j=0;j<10;j++) 
         {
			   printf("%d x %d = %d\t", i, j, TM_matrix[i][j]);
		  }
		  printf("\n");
      }
   return 0;
}