#include <iostream>

using namespace std;

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
    //fuerza bruta
    float suma = 0;
    for(int i = 0; i < n; ++i){
        for(int j = 0; j < n; ++j){
            if ( matriz[i][j] != 0){
                suma += matriz[i][j];
            }
        }
    }

    //parte a y b

    suma = 0;
    int numeroOperaciones = 0;
    int faltantes = 0;
    int j;
    int contador;

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

    cout<<endl<<"La suma es "<<suma<<". Numero de operaciones realizadas fue "<<numeroOperaciones<<endl;

    cout<<endl<<"El numero de operaciones realizadas (calculado) es igual a "<<(n*(n+1))/2<<endl;

    return 0;
}
