library(pracma)

# función para reducir

reduccion <-function(M){
  r=0
  for (i in 1:nrow(M)){#todas las filas
    p = M[i][i]
    for (j in 1:ncol(M)){
      M[i][j] = (M[i][j])/p
      r<-r+1
    }
    for (j in 1:nrow(M)){#todas las filas
      if(j!=i){
        p = M[j][i]
        for (k in 1:ncol(M)){#todas las columnas
          M[j][k] = M[j][k] - p*(M[i][k])
          r<-r+1
        }
      }
    }
  }
  print(M)
  cat("\nMultiplicaciones = ",r)
}


#generación automática de matriz

n= 5
rows = n
columns = n

A <- matrix(data = NA, nrow = rows, ncol = columns, byrow = FALSE)
b <- matrix(data = NA, nrow = rows, ncol = 1, byrow = FALSE)

for (i in 1:rows){
  for (j in 1:columns){
    randomNumber <- runif(1, 1, 100) #genera 1 número real entre 1 y 100
    A[i,j] = randomNumber
  }
  randomNumber <- runif(1, 1, 100) #genera 1 número real entre 1 y 100
  b[i,1] = randomNumber
}
A
b  

#unir b como columna a A
c <- cbind(A, b)
c

#reducir mediante Gauss-Jordan
rref(c)

#reducir con función de arriba
reduccion(c)

# 99 73 7
# 48 36 87

# A <- matrix(c(99,48,73,36), nrow = 2, ncol = 2, byrow = FALSE)
# b <- matrix(c(7,87), nrow = 2, ncol = 1, byrow = FALSE)
# c <- cbind(A, b)
# c
# rref(c)
# reduccion(c)