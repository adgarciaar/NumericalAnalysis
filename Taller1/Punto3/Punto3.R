#Algoritmo raíz cuadrada

# Entra:   n dato
#             E error permitido 
#             x valor inicial
#    Sale:    y respuesta calculada con error E


# function ----------------------------------------------------------------

cuadraticRoot <- function(n,E,x){
  y <- 0.5*(x+n/x)
  i <- 1
  while( (abs(x-y)) > E ){
    x <- y
    y <- 0.5*(x+n/x)
    cat("Iteration ",i,": \tx = ",x," \ty = ",y,"\tabs(x-y) = ",abs(x-y),"\n")
    i <- i+1
  }
  return(y)
}

# execution ---------------------------------------------------------------

n <- 7
E <- 0.0000000001
x <- 100

cRoot <- cuadraticRoot(n, E, x)

cat("\nCuadratic root is ", cRoot,"\n")

# validation --------------------------------------------------------------

#calculate absolute error

abserror <- abs(sqrt(n)-cRoot)

cat("\nAbsolute error is ", abserror, "\n")

#calculate relative error

relrror <- (abs(sqrt(n)-cRoot)) / abs(sqrt(n)) 

cat("\nRelative error is ", relrror, "\n")

