#include <bits/stdc++.h>
using namespace std;

double Horner(double a[], double b[], int n, double t)
{
  int cont = 0;
  b[n] = a[n];
  for(int k=(n-1); k>=0; k--)
  {
       b[k] = t*b[k+1]+a[k];
       cont = cont +2;
  }
  return cont;
}

int main ( )
 {
      int n, i, m, k;
      double t;

    cout << "\n\n\t\t Metodo de Horner. Evaluo de polinomios eficientemente";
    cout << "\n\nRecuerde que este programa está orientado a corroborar que el algoritmo necesita hacer 2N operaciones (N sumas y N multiplicaciones) donde N representa el grado del polinomio";
    cout << "\n\nIngrese el grado del polinomio ";
    cin >> n;

    double a[n+1], b[n+1];
    cout << "\n\n Ingrese los coeficientes con su signo correspondiente \n";
    for(i=0; i<=n; i++)
    {
           m = n-i;
           cout << "\n a("<< m <<") : > ";
           cin >> a[n-i];
     }

     cout << "\n\n Polinomio ingresado: \n\n P(x) = ";
     for(i=0; i<=n; i++)
     {
           m=n-i;
           if(i!=n)
           {
                cout << " " << a[m] << " x^ " << m << " + ";
            }
           else
            {
               cout << " " << a[m] << " ";
             }
      }

      cout << "\n\n\n Coloque el valor para evaluar el P(x): ";
      cin >> t;

      int cont = Horner(a,b,n,t);


      cout << "\n\t La raiz es:  " << b[0];
      cout<< "\n\t Número de operaciones = "<< cont;

      cout << endl << endl;

      //cout<< "Derivada" << endl;
      double d[n],e[n];
      for(i=0; i<=n; i++)
           {
                 d[i] = a [i+1] * (i+1);
            }
      cout << "\n\n Polinomio de la derivada: \n\n P'(x) = ";
      for(i=1; i<=n; i++)
      {
            m=n-i;
            if(i!=n)
            {
                 cout << " " << d[m] << " x^ " << m << " + ";
             }
            else
             {
                cout << " " << d[m] << " ";
             }
      }
      int cont2 = Horner(d,e,n-1,t);
      cout << "\n\t La raiz es:  " << e[0];
      cout << "\n\t Número de operaciones = "<< cont2;
      cout << endl << endl;

      return 0;
}
