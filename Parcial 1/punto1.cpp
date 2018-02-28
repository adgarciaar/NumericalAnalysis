#include <iostream>
#include <ctime>

using namespace std;

int f(int n);

int main(){

    int n;

    cout<<"Digite n: ";
    cin>>n;

    float matriz[n][n];

    //asumiendo que se ingresa la matriz correctamente
    for(int i = 0; i < n; ++i){
        for(int j = 0; j < n; ++j){
            cout<<"Posicion "<<i<<", "<<j<<" :";
            cin>>matriz[i][j];
            cout<<endl;
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
            suma += matriz[i][j];
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
