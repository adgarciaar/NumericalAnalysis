#include <iostream>
#include <ctime>
#include <cstdlib>

using namespace std;

int f(int n);

int main(){

    srand(time(NULL));

    int n;

    cout<<"Digite n: ";
    cin>>n;
    cout<<endl;

    //inicialización matriz

    float** matriz = new float*[n];

    for (int i = 0; i < n; i++){
        *(matriz+i) = new float[n];
    }

    for(int i = 0; i < n; ++i){
        for(int j = 0; j < n; ++j){
            if(i>j){
                (*(*(matriz+i)+j)) = 0;
            }else{
                (*(*(matriz+i)+j)) = rand() % 5 + 1;
            }
        }
    }

    //parte a y b

    int suma = 0;
    int numeroOperaciones = 0;
    int faltantes = 0;
    int j;
    int contador;

    // Record start time
	clock_t startTime = clock( );

	// Portion of code to be timed

    for(int i = n-1; i >= 0; i--){
        faltantes++;
        contador = 0;
        j = n-1;
        while (contador < faltantes){
            suma += (*(*(matriz+i)+j));
            numeroOperaciones++;
            //cout<<"sumado "<<matriz[i][j]<<endl;
            j--;
            contador++;
        }
    }

    // Record end time
	clock_t endTime = clock( );

	double ellapsedSeconds = double( endTime - startTime ) / double( CLOCKS_PER_SEC );

    cout<<endl<<"La suma es "<<suma<<". Numero de operaciones realizadas fue "<<numeroOperaciones<<". Tiempo de ejecucion = "<<ellapsedSeconds<< " milisegundos"<<endl;

    //parte c

    cout<<endl<<"El numero de operaciones realizadas (calculado) es igual a "<<f(n)<<endl<<endl;

    return 0;
}

//parte c
int f(int n){
    return (n*(n+1))/2;
}
