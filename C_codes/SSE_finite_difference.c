// En este programa se resuelve la ecuación de Laplace
// usando el método de SOR para el problema de dos
// cuadrados concéntricos. El interior tiene un potencial
// de 100 y el exterior será 0. Siendo esta las condiciones
// a la frontera.
// "Todos debemos buscar nuestras propias respuestas."

#include<stdio.h>
#include<math.h>

#define mass 1
#define hbar 1
#define N 11
#define X 3.0

float V(float x, float k, float c, float norm){
    return (-k*x*x + c*x*x*x*x + norm) ;
}

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

void adjoint(float A[N][N], float adj[N][N]) 
{ 
    if (N == 1) 
    { 
        adj[0][0] = 1; 
        return; 
    } 
    int sign = 1;
    float temp[N][N]; 
  
    for (int i=0; i<N; i++) 
    { 
        for (int j=0; j<N; j++) 
        {
            getCofactor(A, temp, i, j, N); 
            sign = ((i+j)%2==0)? 1: -1; 
            adj[j][i] = (sign)*(determinant(temp, N-1)); 
        } 
    } 
} 
  
void inverse(float A[N][N], float inverse[N][N]) 
{
    float det = determinant(A, N); 
    if (det == 0) 
    { 
        printf("Singular matrix, can't find its inverse"); 
        return;
    }
    float adj[N][N]; 
    adjoint(A, adj); 
    for (int i=0; i<N; i++) 
        for (int j=0; j<N; j++) 
            inverse[i][j] = adj[i][j]/det; 
} 

float norma(float x[N]) {
    float res = 0.;
    for (int i=0; i<N; i++) {
        res = res + x[i]*x[i];
    }
    return sqrt(res);
}

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

void inverse_method(float A[N][N], float x[N], float sigma) {
    float B[N][N], B_inv[N][N], z[N];
    float xnorm, lnew;
    float count = 0;
    for(int i=0; i<N; i++)
    {
        for(int j=0; j<N; j++)
        {
            B[i][j] = A[i][j];
        }
        B[i][i] = A[i][i] - sigma;
    }
    inverse(B, B_inv);
    do {
        xnorm = norma(x);
        for(int i=0; i<N; i++) {
            z[i] = x[i]/xnorm;
        }
        for(int i=0; i<N; i++) {
            x[i]=0;
            for(int j=0; j<N; j++) {
                x[i]=x[i]+B_inv[i][j]*z[j];
            }
        }
        count = count + 1;
        if (count > 0) {
            break;
        }
    }
    while(fabs(lnew - lold)>0.001);
    // printf("\n The required eigen value is %f", lnew);
    // printf("\n\nThe required eigen vector is :\n");
    // for(int i=0; i<N; i++)
    // {
    //     printf("%f\t", x[i]);
    // }
}

void main()
{
    float k = 2.0, c = 0.25, norm = 4.0;
    float a = 2*X/(N-1);
    float t0 = hbar*hbar/(2.0*mass*a);
    float H[N][N], V_itr[N], H_inv[N][N], x[N];
    for (int i = 0; i<N; i++){
        for (int j = 0; j < N; j++){
            if ((j == i+1) | (j == i-1))
            {
                H[i][j] = -t0;
            }
            else {
                H[i][j] = 0;
            }
        }
        V_itr[i] = V(-X + i*a, k, c, norm);
        H[i][i] = 2*t0 + V(-X + i*a, k, c, norm);
        x[i] = 1.;
    }
    printf("Iniciando\n");
    inverse_method(H, x, 1.);
}