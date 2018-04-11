library(polynom)
require(graphics)
x <- c(0,1,2,3)
y = matrix(c(1,0,0,10,1,1,1,1,15,1,2,4,8,5,0,1,0,0,1), nrow=4, byrow=TRUE)

poly.calc(x, y)

plot(poly.calc(x,y))

