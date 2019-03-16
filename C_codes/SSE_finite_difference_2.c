/*
En este programa se resuelve la ecuación de Shcrödinger
estacionaria para un pozo doble de potencial usando el 
método de diferencias finitas para expresar el Hamiltoniano 
en forma matricial. Posteriormente, se emplea el método de 
la potencia inversa sobre tal matriz para obtener los valores 
y vectores propios. 
Para tal fin, se emplea el método de eliminación Gaussiana para
resolver el sistema de ecuaciones obtenido en el método de la 
potencia inversa (para no vernos obligados a calcular la inversa 
de la matriz).
"No nos sentamos a esperar por una oportunidad, 
nosotros creamos una."
*/

// Librerías
#include<stdio.h>
#include<math.h> 

/*
ATENCION
Debido a que usamos math.h, es necesario compilar
este código usando gcc SSE_finite_difference_2.c -o name.out -lm
para hacer referencia a la libería.
ATENCION
*/

#define mass 1 // Masa
#define hbar 1 // h barra
#define N 161 // Número de bins para las diferencias finitas (IMPAR!!!)
#define X 5.0 // Intervalo donde se calculan los vectores propios [-X, X]
#define GNUP "/usr/bin/gnuplot" //Llama gnuplot

/*
Función del pozo doble de potencial
Revisar: https://en.wikipedia.org/wiki/Double-well_potential#The_symmetric_double-well
'x' es la pocisión donde se calcula el potencial.
'k' es el coeficiente del término cuadrático.
'l' es el coeficiente del término a la cuarta.
'norm' es una normalización para colocar el mínimo del potencial
en cero.
*/
float V(float x, float k, float l, float norm){
    return (-k*x*x + l*x*x*x*x + norm); // hacemos k = h^4/4 y l = c^2/2
}

/*
Función para determinar el cofactor de una matriz
Esta función es de utilidad para calcular el determinante
de una matriz grande.
'A' es la matriz de la que se obtiene su cofactor respesto a su
entrada ['p']['q'].
En 'temp' se guarda el coafactor.
*/
void getCofactor(float A[N][N], float temp[N][N], int p, int q, int n) 
{ 
    int i = 0, j = 0; 
    for (int row = 0; row < n; row++) 
    { 
        for (int col = 0; col < n; col++) 
        {
            if (row != p && col != q) 
            { 
                temp[i][j++] = A[row][col]; 
                if (j == n - 1) 
                { 
                    j = 0; 
                    i++; 
                } 
            } 
        } 
    } 
} 

/*
Función para calcular el determinante de una matriz.
'A' es la matriz de la que se obtiene su determinante.
'n' es su dimensión.
*/
float determinant(float A[N][N], int n) 
{ 
    float D = 0.;
    if (n == 1) {
        return A[0][0]; 
    }
    float temp[N][N];
    int sign = 1;
    for (int f = 0; f < n; f++) 
    {
        getCofactor(A, temp, 0, f, n); 
        D += sign * A[0][f] * determinant(temp, n - 1); 
        sign = -sign; 
    } 
    return D; 
} 

/*
Calcula la norma del arreglo unidimensional 'x'.
*/
float norma(float x[N]) {
    float res = 0.;
    for (int i=0; i<N; i++) {
        res = res + x[i]*x[i];
    }
    return sqrt(res); // Aquí se usa math!!!!.
}

/*
Función para presentar en pantalla la matriz 'A'
con un orden 'n'. 
*/
void display(float A[N][N], int n) 
{ 
    for (int i=0; i<n; i++) 
    { 
        for (int j=0; j<n; j++) {
            printf("%f ", A[i][j]); 
        }
        printf("\n"); 
    } 
} 

/*
Lleva acabo el método de eliminación Gaussiano para obtener 
el vector 'y' del sistema de ecuaciones:
                        'B*y = v'.
El vector 'y' puede tener cualquier valor real en sus entradas.
*/
void GaussElim(float B[N][N], float v[N], float y[N]) {
    float A[N][N+1], sum=0.0, c;
    // Primero se crea la matriz A con el vector v agregado 
    // en otra columna.
    for (int i = 0; i < N; i++) {
        for (int j = 0; j<N+1; j++) {
            if (j == N) {
                A[i][j] = v[i];
            } else {
                A[i][j] = B[i][j];
            }
        }
    }
    // Después se calcula la matriz triangular
    // superior de la matriz 'A'.
    for(int i=0; i<N; i++) {
        for(int j=0; j<N; j++) {
            if(i > j) {
                c=A[i][j]/A[j][j];
                for(int k=0; k<N+1; k++) {
                    A[i][k]=A[i][k]-c*A[j][k];
                }
            }
        }
    }
    // Aquí se concluye el método de eliminación
    // Gaussiana con backsubstitution.
    y[N-1]=A[N-1][N]/A[N-1][N-1];
    for(int i=N-2; i>=0; i--) {
        sum=0;
        for(int j=i+1; j<N; j++) {
            sum=sum+A[i][j]*y[j];
        }
        y[i]=(A[i][N]-sum)/A[i][i];
    }
}

/*
Implementa el método de la potencia inversa sobre la matriz 'A'
con un vector de prueba 'y' y un valor inicial 'sigma'.
Devuelve el eigenvalor 'lambda' que es más cercano al valor
inicial 'sigma', mientras 'y' es el eigenvector correspondiente.
*/
float inverse_method(float A[N][N], float y[N], float sigma) {
    float B[N][N], v[N], diff[N];
    float ynorm, theta_new = 0., theta_old;
    // Las siguientes cuatro líneas se pueden descomentar si se 
    // desea comprobar si la matriz es o no singular.
    // OJO: hace el programa más lento.
    // if (determinant(A, N) == 0.) {
    //     printf("Matriz es singular!!");
    //     return 0.;
    // }
    // Se calcula la matriz B = A - sigma*I (la cual se desea)
    // "invertir".
    for(int i=0; i<N; i++) {
        for(int j=0; j<N; j++)
        {
            B[i][j] = A[i][j];
        }
        B[i][i] = A[i][i] - sigma;
    }
    // Aquí se lleva acabo el método de la potencia inversa
    // para un límite de 100 iteraciones como máximo, lo cual
    // se puede modificar como se crea necesario.
    // Aunque eligiendo correctamente 'sigma' y 'y' el código
    // converge rápidamente.
    for (int k = 0; k<100; k++) {
        ynorm = norma(y);
        for(int i=0; i<N; i++) {
            v[i] = y[i]/ynorm;
        }
        GaussElim(B, v, y); // Se usa el método de eliminación Gaussiano
        // para calcular 'y'. COn ello se evita invertir 'B'.
        theta_old = theta_new; //Valor de la pasada iteración.
        theta_new = 0.; // Aquí se guardará el resultado de esta iteración.
        for(int i=0; i<N; i++) {
            theta_new = theta_new + v[i]*y[i]; 
        }
        if (fabs(theta_new - theta_old) < 0.000001) { // Comprobación de convergencia
        // se puede hacer más pequeño o grande.
            printf("Convergencia en %d pasos\n", k);
            break;
        }
    }
    // Calcula el eigenvalor.
    float lambda = sigma + (1./theta_new);
    // Calcula el eigenvector normalizado.
    for (int i = 0; i<N; i++) {
        y[i] = y[i]/theta_new;
    }
    return lambda; // devuelve el eigenvector.
}

void main()
{   
    FILE *gp; //Apuntador tipo archivo a GNUPLOT
    FILE *potential;
    float k = 2.0, c = 0.25, norm = 4.0; // Valores a usar en 'V'.
    float a = 2*X/(N-1), lambda; // 'a' es el tamaño de bin.
    float t0 = hbar*hbar/(2.0*mass*a); // t0 es el intervalor 'temporal'
    // para el método de diferencias finitas.
    float H[N][N], V_itr[N], y[N], x[N];
    // 'H' es el Hamiltoniano obtenido por diferencias finitas.
    // 'V_itr' es el arreglo del potencial. 
    // 'y' es el vector donde se guardarán los eigenvectores temporalmente.
    // 'x' es el arreglo de posiciones.
    // Abajo se ejetuca el método de diferencias finitas.
    for (int i = 0; i<N; i++){
        for (int j = 0; j < N; j++){
            if ((j == i+1) | (j == i-1))
            {
                H[i][j] = -t0; // términos fuera de la diagonal.
            }
            else {
                H[i][j] = 0;
            }
        }
        V_itr[i] = V(-X + i*a, k, c, norm); 
        H[i][i] = 2*t0 + V(-X + i*a, k, c, norm); // términos de la diagonal.
        y[i] = 1.;
        x[i] = -X + i*a;
    }
    if((potential = fopen("data_V.dat", "w")) == NULL){
		printf("No se pudo inicializar la matriz\n\n"); //En caso de que no se haya podido crear el archivo
		}
	else{
	for(int i=0;i<N;i++){
		fprintf(potential, "%f %f", x[i], V_itr[i]); //Se escribe la matriz resultante en el archivo Matriz.dat
		fprintf(potential, "\n");
		}
	}
	fclose(potential);

    // Abajo se ejetuca el método de la potencia inversa.
    lambda = inverse_method(H, y, 0.5);
    printf("1er eigenvalor: %f\n", lambda);
    FILE *l0;
    if((l0 = fopen("data_l0.dat", "w")) == NULL){
		printf("No se pudo inicializar la matriz\n\n"); //En caso de que no se haya podido crear el archivo
		}
	else{
	for(int i=0;i<N;i++){
		fprintf(l0, "%f %f", x[i], y[i]+lambda); //Se escribe la matriz resultante en el archivo Matriz.dat
		fprintf(l0, "\n");
		}
	}
	fclose(l0);
    // printf("El respectivo eigenvalor es :\n");
    // for(int i=0; i<N; i++)
    // {
    //     printf("%f\t", y[i]);
    // }
    // printf("\n");

    for (int i=0; i<N; i++){
        y[i] = 1.;
    }
    lambda = inverse_method(H, y, 1.0);
    printf("2do eigenvalor: %f\n", lambda);
    FILE *l1;
    if((l1 = fopen("data_l1.dat", "w")) == NULL){
		printf("No se pudo inicializar la matriz\n\n"); //En caso de que no se haya podido crear el archivo
		}
	else{
	for(int i=0;i<N;i++){
		fprintf(l1, "%f %f", x[i], y[i]+lambda); //Se escribe la matriz resultante en el archivo Matriz.dat
		fprintf(l1, "\n");
		}
	}
	fclose(l1);
    // printf("El respectivo eigenvalor es :\n");
    // for(int i=0; i<N; i++)
    // {
    //     printf("%f\t", y[i]);
    // }
    // printf("\n");
    
    for (int i=0; i<N; i++){
        y[i] = 1.;
    }
    lambda = inverse_method(H, y, 1.5);
    printf("3er eigenvalor: %f\n", lambda);
    FILE *l2;
    if((l2 = fopen("data_l2.dat", "w")) == NULL){
		printf("No se pudo inicializar la matriz\n\n"); //En caso de que no se haya podido crear el archivo
		}
	else{
	for(int i=0;i<N;i++){
		fprintf(l2, "%f %f", x[i], y[i]+lambda); //Se escribe la matriz resultante en el archivo Matriz.dat
		fprintf(l2, "\n");
		}
	}
	fclose(l2);
    // printf("El respectivo eigenvalor es :\n");
    // for(int i=0; i<N; i++)
    // {
    //     printf("%f\t", y[i]);
    // }
    // printf("\n");
    
    for (int i=0; i<N; i++){
        y[i] = 1.;
    }
    lambda = inverse_method(H, y, 2.0);
    printf("4to eigenvalor: %f\n", lambda);
    FILE *l3;
    if((l3 = fopen("data_l3.dat", "w")) == NULL){
		printf("No se pudo inicializar la matriz\n\n"); //En caso de que no se haya podido crear el archivo
		}
	else{
	for(int i=0;i<N;i++){
		fprintf(l3, "%f %f", x[i], y[i]+lambda); //Se escribe la matriz resultante en el archivo Matriz.dat
		fprintf(l3, "\n");
		}
	}
	fclose(l3);
    // printf("El respectivo eigenvalor es :\n");
    // for(int i=0; i<N; i++)
    // {
    //     printf("%f\t", y[i]);
    // }
    // printf("\n");
    
    for (int i=0; i<N; i++){
        y[i] = 1.;
    }
    lambda = inverse_method(H, y, 2.5);
    printf("5to eigenvalor: %f\n", lambda);
    FILE *l4;
    if((l4 = fopen("data_l4.dat", "w")) == NULL){
		printf("No se pudo inicializar la matriz\n\n"); //En caso de que no se haya podido crear el archivo
		}
	else{
	for(int i=0;i<N;i++){
		fprintf(l4, "%f %f", x[i], y[i]+lambda); //Se escribe la matriz resultante en el archivo Matriz.dat
		fprintf(l4, "\n");
		}
	}
	fclose(l4);
    // printf("El respectivo eigenvalor es :\n");
    // for(int i=0; i<N; i++)
    // {
    //     printf("%f\t", y[i]);
    // }
    // printf("\n");
    
    gp = popen(GNUP, "w"); //se comunica con gnuplot
	if(gp == NULL){
		printf("No se pudo iniciar gnuplot");
	} else {
        fprintf(gp, "set xlabel \"x\" \n");
        fprintf(gp, "set ylabel \"phi\" \n");
        fprintf(gp, "set yrange [-1:6] \n");
        fprintf(gp, "plot \"data_V.dat\" with linespoints title \"Potencial\", \t"); //Aqui esta el comando de graficar la matriz
        fprintf(gp, "\"data_l0.dat\" with linespoints title \"eigenvector 0\", \t"); //Aqui esta el comando de graficar la matriz
	    fprintf(gp, "\"data_l1.dat\" with linespoints title \"eigenvector 1\", \t");
        fprintf(gp, "\"data_l2.dat\" with linespoints title \"eigenvector 2\", \t");
        fprintf(gp, "\"data_l3.dat\" with linespoints title \"eigenvector 3\", \t");
        fprintf(gp, "\"data_l4.dat\" with linespoints title \"eigenvector 4\"\n");
        fflush(gp); //se vacia el buffer de datos de gp
	    fflush(stdin); //se vacia el de stdin
	    getchar();
	    getchar(); //estos son para hacer una pausa y que no se cierre gnuplot inmediatamente
	    pclose(gp); //tras apretar enter, se cierra gnuplot y el programa
    }
}
