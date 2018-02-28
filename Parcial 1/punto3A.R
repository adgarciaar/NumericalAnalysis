#tercer metodo
# Remueve todos los objetos creados
rm(list=ls())
Fx <- function(x) log(x+2) - sin(x)
F1x <- function(x) (1/(x+2)) -cos(x)

# Metodo de la Secante
# Halla la raiz de Fx
secante <- function(x0,x1) {
  #(Fx(b)*a-Fx(a)*b)/(Fx(b)-Fx(a))
  x<-(Fx(x1)*x0-Fx(x0)*x1)/(Fx(x1)-Fx(x0))
  error <-1 #error se inicializa en 1
  while (error > 1.e-7) {
    x0<-x1 #ahora límite inferior igual a superior
    x1<-x #ahora límite superior igual a x calculado
    x<-(Fx(x1)*x0-Fx(x0)*x1)/(Fx(x1)-Fx(x0))
    if (Fx(x) == 0) # se encontró la raíz
      break
    error<-abs(Fx(x)/F1x(x))
    cat("X=",x,"\t","E=",error,"\n")
  }
}

system.time({secante(-1.8,-1.0)})
