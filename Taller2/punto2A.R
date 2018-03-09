A = matrix(c(-8.1, -7, 6.123, -2, -1, 4,
             -3, -1, 0, -1, -5, 0.6,
             -1, 0.33, 6, 1/2), nrow=4, byrow=TRUE)

print(A)

luDec <- lu(A)
L <- expand(luDec)$L
L

U <- expand(luDec)$U
U

D = matrix(c(NA, NA, NA, NA, NA, NA,
             NA, NA, NA, NA, NA, NA,
             NA, NA, NA, NA), nrow=4, byrow=TRUE)

for (i in 0:4){
  for (j in 0:4){
    if(i == j){
      D[i,j] <- A[i,j]
    }
  }
}

print(D)

#A = L + U + D
#A