#include<bits/stdc++.h>
#include <iostream>
#include <math.h>
#include <list>

using namespace std;

long double funcion(long double x){

    return exp(x) - cos(3*x);
}

long double trisection(long double a, long double b, long double error){

    if (funcion(a) * funcion(b) > 0){
        return 1;
    }

    long double c = a;
    long double x1, x2;

    while (abs(b-a) >= error){

        if( abs(funcion(a)) < abs(funcion(b)) ){ // si a está más cerca de la raíz

            x1 = a + (b-a)/3;

            if(funcion(a)*funcion(x1) < 0){ //hay una raíz entre a y x1
                b = x1;

            }else{
                x2 = b - (b-a)/3;

                if(funcion(x1)*funcion(x2) < 0){ //hay una raíz entre x1 y x2
                    a = x1; //x1 será el menor del intervalo
                    b = x2; //x2 será el mayor del intervalo
                }else{
                    a = x2; //x2 será el menor del intervalo
                }
            }
        }else{ // si b está más cerca de la raíz
            x2 = b - (b-a)/3;

            if(funcion(b)*funcion(x2) < 0){ //hay una raíz entre x2 y b
                a = x2; //x2 será el menor del intervalo
            }else{
                x1 = a + (b-a)/3;

                if(funcion(x1)*funcion(x2) < 0){ //hay una raíz entre x1 y x2
                    a = x1; //x1 será el menor del intervalo
                    b = x2; //x2 será el mayor del intervalo
                }else{
                    b = x1; //x1 será el mayor del intervalo
                }

            }

        }

    }

    return (a+b)/2;
}

int main(){

    long double intervalo = 0.0001, error = 0.00000001;

    long double maximo = 2*atan(1)*4;
    long double contador = -2*atan(1)*4;

    long double resultado;

    list<long double> raices;

    while(contador < maximo){
        long double a = contador, b = contador+intervalo;
        resultado = trisection(a, b, error);
        if(resultado != 1){
            raices.push_back(resultado);
        }
        contador += intervalo;
    }

    cout<<"Raices"<<endl<<endl;
	for(list< long double >::iterator it = raices.begin(); it != raices.end( );	it++){
		cout <<*it << endl;
	}

    return 0;
}
