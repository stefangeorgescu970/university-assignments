##############
# Exercise 6.2

m <- 50
n <- 10
mu <- 1
sigma <- 2
alpha <- 0.05 # 1-aplha is confidence, which is 95

# Get 50 samples of size 10
randMatrix <- matrix(rnorm(m*n, mu, sigma), nrow = m)

# Construct mean for each sample
vectorWithMeans <- apply(randMatrix, 1, mean)

# We look in the tutorial for the formula
left <- vectorWithMeans - qnorm(1-alpha/2)*sigma/sqrt(n)
right <- vectorWithMeans + qnorm(1-alpha/2)*sigma/sqrt(n)

# We count
sum(left < mu & mu < right) / m

# Visualisation of the result
matplot(rbind(left, right), rbind(1:m, 1:m), type="l", lty=1, col = c("grey", "black"))
abline(v = 1)


##############
# Exercise 6.7

p <- 3/12
n <- 12
alpha <- 0.05

# Formula from tutorial
intervalHeads <- c(p - qnorm(1-alpha/2)*sqrt(p*(1-p)/n), p + qnorm(1-alpha/2)*sqrt(p*(1-p)/n))

# Probability of a fair dice
1/6

# We cannot say that the dice is unfair since its probability interval encapsulates the probability of a fair one. If 1/6 was out of that interval, it would be unfair.


##############
# Exercise 6.5

alpha <- 0.05
melt <- c(330.0, 322.0, 345.0, 328.6, 331.0, 342.0,
          342.4, 340.4, 329.7, 334.0, 326.5, 325.8,
          337.5, 327.3, 322.6, 341.0, 340.0, 333.0)

mean1 <- mean(melt)
sd1 <- sd(melt)
n <- length(melt)

# From the formula for estimating mean
intervalHeads <- c(mean1 - qt(1-alpha/2, n-1)*sd1/sqrt(n), mean1 + qt(1-alpha/2, n-1)*sd1/sqrt(n))

# We check the values that we got
t.test(melt, conf.level = (1-alpha), alternative = "two.sided")

# We use the formula from the tutorial
interval2Heads <- sqrt(c((n-1)*sd1^2/qchisq(1-alpha/2, n-1), (n-1)*sd1^2/qchisq(alpha/2, n-1)))

# Since we want on the right side 5% out of the interval, we take 1-alpha with alpha = 0.01 since we need 99%
alpha <- 0.01
oneSideIntervalHeadsLeft <- c(-Inf, mean1 + qt(1-alpha, n-1)*sd1/sqrt(n))
oneSideIntervalHeadsRight <- c(mean1 - qt(1-alpha, n-1)*sd1/sqrt(n), Inf)

# We check the values that we got
t.test(melt, conf.level = (1-alpha), alternative = "less")
t.test(melt, conf.level = (1-alpha), alternative = "greater")


###############
# Exercise 6.22


families <- c(rep(0.2, 25),rep(0.6, 50),rep(1.02, 40),rep(1.4, 35),rep(1.8, 30))
alpha <- 0.1

mean1 <- mean(families)
sd1 <- sd(families)
n <- length(families)

# Use Model 3 formula for large n
intervalHeadsMean <- c(mean1 - qnorm(1-alpha/2)*sd1/sqrt(n), mean1 + qnorm(1-alpha/2)*sd1/sqrt(n))
intervalHeadsSigma <- c(2*(n-1)*sd1^2/((sqrt(2*n - 3) + qnorm(0.95))^2), 2*(n-1)*sd1^2/((sqrt(2*n - 3) - qnorm(0.95))^2))


###############
# Exercise 6.21 similar to 6.7

p <- 2/100
n <- 200
alpha <- 0.01

# Formula from tutorial
intervalHeads <- c(p - qnorm(1-alpha/2)*sqrt(p*(1-p)/n), p + qnorm(1-alpha/2)*sqrt(p*(1-p)/n))