#include <bits/stdc++.h>
using namespace std;

int main ( )
 {
      int n,d;
      cout << "\n\n\t\t Evaluacion de convergencia";
      cout<<"\n\nIngrese un valor n: ";
      cin >> n;
      int cont = 0;
      while(n > 0)
      {
        d = n % 2;
        n = n / 2;
        cout << d << " " << n << endl;
        cont++;
      }
      cout << "Numero de divisiones : "<<cont<<endl;
      cout << "El número de divisiones corresponde a la aproximación techo de log_2 N" << endl;
      return 0;
}
