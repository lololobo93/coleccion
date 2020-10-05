// En este programa se resuelve la ecuación de Laplace
// usando el método de SOR para el problema de dos
// cuadrados concéntricos. El interior tiene un potencial
// de 100 y el exterior será 0. Siendo esta las condiciones
// a la frontera.
// "Todos debemos buscar nuestras propias respuestas."

#include <stdio.h>


/**
 * Función para checar si número es par o impar.
 * Regresa 1 si número es par, 0 si es impar.
 */
int isEven(int num)
{
    return !(num & 1);
}

int main(){
	
	int N, num;
    int N_ap = 0;
    int N_no = 0;
    int sum_ap = 0;
    int sum_no = 0;

	printf("Diga un número entero: ");
	scanf("%d",&N);
	printf("\n");

	for(int i=0; i<N; i++){ //Definiendo el margen, y todo
		printf("Diga un número entero para carta: ");
	    scanf("%d",&num);
	    printf("\n");

        if(isEven(num))
        {
            sum_ap += num;
            N_ap += 1;
        }
        else
        {
            sum_no += num;
            N_no += 1;
        }
	};
	
    float ans_ap = (float)sum_ap / (float)N_ap;
    float ans_no = (float)sum_no / (float)N_no;

    if(ans_ap>ans_no)
    {
        printf("APARICIO");
        printf("\n");
    }
    else if(ans_ap<ans_no)
    {
        printf("NONILA");
        printf("\n");
    }
    else
    {
        printf("EMPATE!");
        printf("\n");
    }
    
}
