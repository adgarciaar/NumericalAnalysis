library(polynom)
x <- c(0,1,2)
y <- c(10,15,5)
poly.calc(x, y)

require(graphics)

plot(x, y,main = paste("Interpolacion por Lagrange"),asp = 1)
lines(spline(x, y, n = 201), col = 2)
