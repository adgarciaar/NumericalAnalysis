#include <bits/stdc++.h>
using namespace std;

//  fastPrecisePow Retorna la potenica de a elevado a b, esto con fines de no usar la funcion pow y mantener solo operaciones simples, sin embargo no es sensible al número de decimales
// Remplaza en la funcion raizNesima por pow

inline double fastPrecisePow(double a, double b) {
  // calculate approximation with fraction of the exponent
  int e = (int) b;
  union {
    double d;
    int x[2];
  } u = { a };
  u.x[1] = (int)((b - e) * (u.x[1] - 1072632447) + 1072632447);
  u.x[0] = 0;

  // exponentiation by squaring with the exponent's integer part
  // double r = u.d makes everything much slower, not sure why
  double r = 1.0;
  while (e) {
    if (e & 1) {
      r *= a;
    }
    a *= a;
    e >>= 1;
  }

  return r * u.d;
}
//Metodo obtencion de la raiz mediante el metodo de Newton
double raizNesima(int A, int N)
{
    double aux = rand() % 10;
    double tolerancia = 1e-3;
    double xMayor = INT_MAX ;
    double x;

    while (xMayor > tolerancia)
    {
        x = ((N - 1.0) * aux + (double)A/pow(aux, N-1)) / (double)N;
        xMayor = abs(x - aux);
        aux = x;
    }

    return x;
}
int main()
{
    int N;
    int A;
    cout << "\n\n\t\t Raiz n-esima mediante el uso del metodo de Newton";
    cout<<"\n\nIngrese la raiz buscada (n-esima): ";
    cin >> N;
    cout<<"\nIngrese el numero al que se le buscara dicha raiz: ";
    cin >> A;
    double raiz = raizNesima(A, N);
    cout << "\nLa n-esima raiz es " << raiz << endl;

    return 0;
}
