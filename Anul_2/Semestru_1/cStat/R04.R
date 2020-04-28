# Exercise 4.1

x_axis = seq(-5,5,0.01)
plot(x_axis, pnorm(x_axis), type = "l")

x <- rnorm(20)
x <- sort(x)
step <- 1/length(x)
x1 <- c(-5, rep(x, each = 2),5)
y <- seq(0,1,step)
for (i in 1:length(y)) {
  
  lines(x1[c(2*i-1,2*i)], c(y[i], y[i]), col="red")
  
}
