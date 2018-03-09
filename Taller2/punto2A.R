require(Matrix)
require(pracma)

A = matrix(c(-8.1, -7, 6.123, -2, -1, 4,
             -3, -1, 0, -1, -5, 0.6,
             -1, 0.33, 6, 1/2), nrow=4, byrow=TRUE)

A

ludec = lu(A)
L <- ludec$L
L

U <-ludec$U
U

D <- diag(diag(A))
D

A = L %*% U
A