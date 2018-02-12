#include<bits/stdc++.h>
#include <iostream>
#include <math.h>
#include <list>

using namespace std;

long double funcion(long double x){

    //funci�n es (32 - 2x)(24 - 2x)x = 1000
    return 4.0*(pow(x,3)) - 112.0*(pow(x,2)) + 768.0*x - 1000;
}

long double trisection(long double a, long double b, long double error){

    if (funcion(a) * funcion(b) > 0){
        return -1;
    }

    long double c = a;
    long double x1, x2;

    while (abs(b-a) >= error){

        if( abs(funcion(a)) < abs(funcion(b)) ){ // si a est� m�s cerca de la ra�z

            x1 = a + (b-a)/3;

            if(funcion(a)*funcion(x1) < 0){ //hay una ra�z entre a y x1
                b = x1;

            }else{
                x2 = b - (b-a)/3;

                if(funcion(x1)*funcion(x2) < 0){ //hay una ra�z entre x1 y x2
                    a = x1; //x1 ser� el menor del intervalo
                    b = x2; //x2 ser� el mayor del intervalo
                }else{
                    a = x2; //x2 ser� el menor del intervalo
                }
            }
        }else{ // si b est� m�s cerca de la ra�z
            x2 = b - (b-a)/3;

            if(funcion(b)*funcion(x2) < 0){ //hay una ra�z entre x2 y b
                a = x2; //x2 ser� el menor del intervalo
            }else{
                x1 = a + (b-a)/3;

                if(funcion(x1)*funcion(x2) < 0){ //hay una ra�z entre x1 y x2
                    a = x1; //x1 ser� el menor del intervalo
                    b = x2; //x2 ser� el mayor del intervalo
                }else{
                    b = x1; //x1 ser� el mayor del intervalo
                }

            }

        }

    }

    return (a+b)/2;
}

int main(){

    int largo = 32, ancho = 24;
    long double intervalo = 0.0001, error = 0.00000001;

    long double maximo = ancho/2 - intervalo;
    long double contador = 0;

    long double resultado;

    list<long double> raices;

    while(contador < maximo){
        long double a = contador, b = contador+intervalo;
        resultado = trisection(a, b, error);
        if(resultado != -1){
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
