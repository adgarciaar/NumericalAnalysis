library(pracma)
A = matrix(c(-8.1, -7.00, 6.123, -2.0, -1.0, 4.00,
             -3.000, -1.0, 0.0, -1.00, -5.00, 0.6,
             -1.0, 0.33, 6.000, 0.5), nrow=4, byrow=TRUE)
A
b <- c(1.45,3,5.12,???4)
itersolve(A, b, tol = 1e-9, method = "Gauss-Seidel")

