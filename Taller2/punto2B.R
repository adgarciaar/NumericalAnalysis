A = matrix(c(-8.1, -7, 6.123, -2, -1, 4,
             -3, -1, 0, -1, -5, 0.6,
             -1, 0.33, 6, 1/2), nrow=4, byrow=TRUE)

b <- matrix(c(1.45,3,5.12,4.0), nrow = 4, ncol = 1, byrow = TRUE)

cat("Mediante método de Gauss-Seidel\n")

itersolve(A, b, tol = 1e-9, method = "Gauss-Seidel")