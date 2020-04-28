#Exercise 3.1

x<-seq(-10,10,0.01)

plot(x, dnorm(x), type = "l") #N(0,1)
plot(x, dnorm(x,1), type = "l") #N(1,1)
plot(x, dnorm(x,2), type = "l") #N(2,1)

plot(x, dnorm(x), type = "l")
plot(x, dnorm(x, sd = 0.1), type = "l") #N(0,0.1)
plot(x, dnorm(x, sd = 3), type = "l") #N(0,3)


plot(x, pnorm(x), type = "l") #P(0,1)
plot(x, pnorm(x,1), type = "l") #P(1,1)
plot(x, pnorm(x,2), type = "l") #P(2,1)

plot(x, pnorm(x), type = "l")
plot(x, pnorm(x, sd = 0.1), type = "l") #P(0,0.1)
plot(x, pnorm(x, sd = 3), type = "l") #P(0,3)



#Exercise 3.2

#1
pnorm(179, 173, 6)

#2
pnorm(180, 173, 6) - pnorm(167, 173, 6)

#3
1-pnorm(181, 173, 6)

#4
qnorm(0.6, 173, 6)


#Exercise 3.3

values <- rnorm(100)
plot(rnorm(100), type = "l")
hist(values)
density(values)


# Exercise 3.4

x<-seq(0,10,1)
plot(x, dbinom(x, 10, 0.25), type="l")

x<-seq(0,100,1)
plot(x, dbinom(x, 100, 0.25), type="l")

x<-seq(0,100,1)
plot(x, dbinom(x, 1000, 0.25), type="l")



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


# Expercise 3.7

1 - pexp(100, 0.00625)

1 - pexp(200, 0.00625)

1 - pexp(300, 0.00625)

qexp(0.9, 0.00625)


#Exercise 3.8   

ppois(20,15)

ppois(20,15) - ppois(9,15)

qpois(0.8, 15)






