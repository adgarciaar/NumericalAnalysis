#include <bits/stdc++.h>
using namespace std;

int main ( )
 {
      int i;
      int t;
      double v, ev, et;
      cout << "\n\n\t\t Evaluacion de propagacion del Error. Error absoulto y Error relativo";
      cout<<"\n\nIngrese la velocidad: ";
      cin >> v;
      cout<<"\n\nIngrese el error de la velocidad: ";
      cin >> ev;
      cout<<"\n\nIngrese el tiempo: ";
      cin >> t;
      cout << "\n\nIngrese el error de tiempo: ";
      cin >> et;
      double d[t+1], EAbs[t+1], Erel[t+1];
      double ValVerd = 0.0;
      double dist;
      for(i = 0; i <= t ; i++)
      {
        dist = v * (double)i;
        d[i] = dist;
        ValVerd += dist;
      }
      ValVerd = ValVerd / t;
      for(i = 0; i <= t ; i++)
      {
        EAbs[i] = d[i] - ValVerd;
        Erel[i] = EAbs[i] / ValVerd;
      }
      for(i = 0; i <= t ; i++)
      {
        printf("\n\n\tDistancia en t(%d) : %.1f",i,d[i]);
        printf("\n\n\tError absoluto en t(%d) : %.1f",i,EAbs[i]);
        printf("\n\n\tError relativo en t((%d) : %.1f",i,Erel[i]);
        printf("\n---------------------------------------------------------------\n" );
      }

      return 0;
}
