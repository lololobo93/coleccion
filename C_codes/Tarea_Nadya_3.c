#include<stdio.h>
int Roman_to_Arabic(char *Rom_Num);

int main(){
   char Rom_Num[100];
   int result = 0;
   printf( "Introduzca numero romano: \n");
   scanf("%s", Rom_Num);
   result = Roman_to_Arabic(Rom_Num);
   printf("El numero introducido fue :");
   printf("\n%d", result);
   printf("\n");
   return 0;
}
int Roman_to_Arabic(char *Rom_Num)
{
    int result = 0;
    int actual = 0; 
    int anterior = 0;
    while (*Rom_Num) 
    {
        switch(*Rom_Num)
        {
            case 'I':
                actual = 1;
                break;
            case 'V':
                actual = 5;
                break;
            case 'X':
                actual = 10;
                break;
            case 'L':
                actual = 50;
                break;
            case 'C':
                actual = 100;
                break;
            case 'D':
                actual = 500;
                break;
            case 'M':
                actual = 1000;
                break;
            default:
                break;
        }
        if (anterior >= actual)
        {
            result += actual;
        }
        else
        {
            result += (actual - 2*anterior);
        }
        anterior = actual;
        ++Rom_Num;
    }
    return result;
}