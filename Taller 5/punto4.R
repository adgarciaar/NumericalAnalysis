f <- function(x,y) {
  dydx <- 1-x^2+x+y
  return(dydx)
}

h <- 0.1

m <- 20

x <- vector()
x <- c(x, 0:m+1) #inicializar vector

y <- vector()
y <- c(y, 0:m+1) #inicializar vector

x[1] <- 0
y[1] <- 1

cat("i\t    x\t     y\n\n")
 
for (i in 1:m){
  cat(i,"\t ", x[i],"\t ", y[i],"\t\n")
  k1 = h * f(x[i], y[i])
  k2 = h * f(x[i]+h ,y[i]+k1)
  y[i+1] = y[i] + (1/2)*(k1+k2)
  x[i+1] = x[i]+h
}

plot(x,y)