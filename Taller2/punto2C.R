#MODIFICANDO FUNCIÓN ITERSOLVE

itersolve <- function(A, b, x0 = NULL, 
                      nmax = 1000, tol = .Machine$double.eps^(0.5),
                      method = c("Gauss-Seidel", "Jacobi", "Richardson")) {
  stopifnot(is.numeric(A), is.numeric(b))
  
  n <- nrow(A)
  if (ncol(A) != n)
    stop("Argument 'A' must be a square, positive definite matrix.")
  b <- c(b)
  if (length(b) != n)
    stop("Argument 'b' must have the length 'n = ncol(A) = nrow(A).")
  if (is.null(x0)) {
    x0 <- rep(0, n)
  } else {
    stopifnot(is.numeric(x0))
    x0 <- c(x0)
    if (length(x0) != n)
      stop("Argument 'x0' must have the length 'n=ncol(A)=nrow(A).")
  }
  
  method <- match.arg(method)
  
  if (method == "Jacobi") {
    L <- diag(diag(A))
    U <- eye(n)
    beta <- 1; alpha <- 1
  } else if (method == "Gauss-Seidel") {
    L <- tril(A)
    U <- eye(n)
    beta <- 1; alpha <- 1
  } else {  # method = "Richardson"
    L <- eye(n)
    U <- L
    beta <- 0
  }
  
  b <- as.matrix(b)
  x <- x0 <- as.matrix(x0)
  r <- b - A %*% x0
  r0 <- err <- norm(r, "f")
  
  iter <- 0
  while (err > tol && iter < nmax) {
    iter <- iter + 1
    z <- qr.solve(L, r)
    z <- qr.solve(U, z)
    if (beta == 0) alpha <- drop(t(z) %*% r/(t(z) %*% A %*% z))
    x <- x + alpha * z
    r <- b - A %*% x
    err <- norm(r, "f") / r0
    cat("Iteración ",iter," -> Error relativo = ", err,"\n")
  }
  
  cat ("\nNúmero de iteraciones realizado fue ",iter)
  
  cat ("\n\nSoluciones:")
  print(c(x))
}


A = matrix(c(-8.1, -7, 6.123, -2, -1, 4,
             -3, -1, 0, -1, -5, 0.6,
             -1, 0.33, 6, 1/2), nrow=4, byrow=TRUE)

b <- matrix(c(1.45,3,5.12,4.0), nrow = 4, ncol = 1, byrow = TRUE)

cat("Mediante método de Jacobi\n")

itersolve(A, b, nmax = 5, tol = 1e-9, method = "Jacobi")




# CREANDO FUNCIÓN DE NOVO

library( pracma)
A <- matrix(c(-8.1, -7, 6.123, -2, -1, 4,
              -3, -1, 0, -1, -5, 0.6,
              -1, 0.33, 6, 1/2), nrow=4, byrow=TRUE)
print(A)

b<-c(8,15,1,-4) 

f1<-function(A,x,B,n){
  sup<-matrix(0,n,n)
  inf<-matrix(0,n,n)
  diag<-matrix(0,n,n)
  for (i in 0:n){
    for (j in 0:n){
      if(j>i){
        sup[i,j]=A[i,j]
      }
      if(j<i){
        inf[i,j]=A[i,j]
      }
      if(j==i){
        diag[i,j]=A[i,j]
      }
    }
  }
  print(" descomposicion LDU ")
  print("diagonal superior")
  print("  ")
  print(sup)
  print("  ")
  print("diagonal inferior")
  print("  ")
  print(inf)
  print("  ")
  print("diagonal ")
  print("  ")
  print(diag)
  f2(sup,inf,diag,x,B)
  
}

f2<-function(sup,inf,diag,x,B){
  n=0
  print("iteracion ")
  print(n)
  inv=solve(diag)
  print(inv)
  err=1
  while( n<5){
    print("iteracion ")
    print(n)
    x1<-x
    t<-(-1*inv%*%(inf+sup))
    c<-inv%*%B
    x<-(t%*%x1+c)
    print(x)
    err=abs((x[1]-x1[1]))/abs(x[1])
    print("error: ")
    print(err)
    n=n+1
  }
  c<-(sup+inf+diag)
  print("prueba final: ")
  for(i in 0:4){
    for (j in 0:4){
      c[i,j]=c[i,j]*x[i]
    }
  }
  print(c)
}

x<-c(100,2000,3000,4000)
f1(A,x,b,4)
