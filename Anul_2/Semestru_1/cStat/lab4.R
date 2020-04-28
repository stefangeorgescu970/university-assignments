
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
