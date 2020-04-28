# Exercise 3.4


# Bin(10,0.25)
x <- 0:10
y <- dbinom(x, 10, 0.25)
barplot(y, names.arg = x)

# since the chance of success is low, the probability of getting 10 wins is really low, while getting none is bigger.
# if chance is .5, then the plot will be symmetric

#Exercise 3.8   

ppois(20,15)

ppois(20,15) - ppois(9,15)

qpois(0.8, 15)

# Have to look into these things, quantiles whatevs


# Exercise 3.5
# alpha equal to 2

u <- runif(1000) # uniform distribution 
x <- (1/(1-u))^(1/2) #sqrt de ordin alpha = 2
# calculus for this thing on paper, found random sample of certain thign
hist(x, breaks = 100)

x2 <- (1/(u))^(1/2)
hist(x2, breaks = 100)


# Exercise 3.6

plot.new()
rect(0,0,1,1,border = "blue")
x_axis<-seq(0,1,0.01)
lines(x_axis,x_axis^2, col = "red")

x <- runif(100000)
y <- runif(100000)
plot(x, y)
rect(0,0,1,1,border = "blue")
x_axis<-seq(0,1,0.01)
lines(x_axis,x_axis^2, col = "red")
sum(y < x^2) / length(x)



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
