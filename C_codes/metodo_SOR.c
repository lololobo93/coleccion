// En este programa se resuelve la ecuación de Laplace
// usando el método de SOR para el problema de dos
// cuadrados concéntricos. El interior tiene un potencial
// de 100 y el exterior será 0. Siendo esta las condiciones
// a la frontera.
// "Todos debemos buscar nuestras propias respuestas."

#include<stdio.h>
#include<stdlib.h>

#define tam_ext 401 //Tamaño cuadro exterior (IMPAR!!!)
#define tam_int 50 //Tamaño cuadrado interno
#define GNUP "/usr/bin/gnuplot" //Llama gnuplot

float M[tam_ext][tam_ext]; //se definen 2 matrices
float F[tam_ext][tam_ext];

void iteracion(float p, int n_itr){ //Aqui se ejecuta el metodo SOR

    int none, i, j;
    float rij;

	for(none=0;none<n_itr;none++){

	for(i=0; i<tam_ext; i++){
		for(j=0; j<tam_ext; j++){
			if(F[i][j] == 0){
                rij = -4*M[i][j]+M[i+1][j]+M[i-1][j]+M[i][j-1]+M[i][j+1];
				M[i][j] += p*rij/4; //Método SOR
				}
			else{
			};
			}
		}
	}
}


int main(){
	
	int a,b,r,y,t,h,q;
    float p_param;

	FILE *gp; //Apuntador tipo archivo a GNUPLOT
	FILE *matriz; //Apuntador tipo archivo al documento "matriz.dat"

	printf("Diga el numero de iteraciones: ");
	scanf("%d",&y);
	printf("\n");

	printf("Diga el parametro p: ");
	scanf("%f",&p_param);
	printf("\n");

	for(a=0; a<tam_ext; a++){ //Definiendo el margen, y todo
		F[a][0]=1; //La matriz F dice donde no hacer promedios
		F[a][tam_ext-1]=1;
		F[0][a]=1;
		F[tam_ext-1][a]=1;
		M[a][0]=0; //M tiene los valores iniciales de frontera
		M[a][tam_ext-1]=0;
		M[0][a]=0;
		M[tam_ext-1][a]=0;
		};
	
	for(h=(((tam_ext-1)/2)-tam_int); h<(((tam_ext-1)/2)+tam_int);h++){
	for(q=(((tam_ext-1)/2)-tam_int); q<(((tam_ext-1)/2)+tam_int);q++){
		F[h][q]=1; //La matriz F dice donde no hacer promedios
		M[h][q]=100; //M tiene los valores iniciales de frontera
		};
	};


	if((matriz = fopen("Matriz.dat", "w")) == NULL){
		printf("No se pudo inicializar la matriz\n\n"); //En caso de que no se haya podido crear el archivo
		}
	else{

	iteracion(p_param, y); //Se llaman las iteraciones

	for(a=0;a<tam_ext;a++){
		for(b=0;b<tam_ext;b++){
			fprintf(matriz, "%f ", M[a][b]); //Se escribe la matriz resultante en el archivo Matriz.dat
			};
		fprintf(matriz, "\n");
		};

	};
	fclose(matriz);

	gp = popen(GNUP, "w"); //se comunica con gnuplot
	if(gp == NULL){
		printf("No se pudo iniciar gnuplot");
		exit(EXIT_FAILURE);
	}

	fprintf(gp, "plot \"Matriz.dat\" matrix with image\n"); //Aqui esta el comando de graficar la matriz
	fflush(gp); //se vacia el buffer de datos de gp
	fflush(stdin); //se vacia el de stdin
	getchar();
	getchar(); //estos son para hacer una pausa y que no se cierre gnuplot inmediatamente
	pclose(gp); //tras apretar enter, se cierra gnuplot y el programa

	return(EXIT_SUCCESS);
}
