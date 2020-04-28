# Excerise 7.1

bottles <- c(1.36, 1.14, 1.27, 1.15, 1.20, 1.29, 1.27, 1.18, 1.23, 1.36, 1.38, 1.37,
            1.30, 1.21, 1.33, 1.28, 1.32, 1.29, 1.33, 1.25)

n <- length(bottles)

sd1 <- 0.07


mu_0 <- 1.20

alpha <- 0.04

# test statistic from tutorial
z<- ( mean(bottles) - mu_0 ) * sqrt(n) / sd1

z > qnorm(1-alpha)

# We note that the value of the test statistic 
# T falls into the rejection region R0.04 = [1.7507, +inf), therefore the null hypothesis should be rejected.

###############
# Exercise 7.2


coffee <- c(142, 151, 148, 151, 145, 150, 141)

n <- length(coffee)

mu_0 <- 150

alpha <- 0.05

t_stat <- ( mean(coffee) - 150 )/sd(coffee) * sqrt(n)

qt(1-alpha/2, n-1)

qt(alpha/2, n-1)

t_stat <  qt(1-alpha/2, n-1)
t_stat >  -qt(1-alpha/2, n-1)
#it is not in the critical region, no reason to reject h0

pt(t_stat, n-1) + 1 - pt(-t_stat, n-1)

t.test(coffee, mu = 150)

# p value is higher than 0.05, cannot reject h0


###############
# Exercise 7.3

teachers <- c(14, 17, 7, 33, 2, 24, 26, 22, 12)
office <- c(13, 15, 3, 2, 25, 4, 1, 18, 6, 9, 20, 11, 5, 1, 7)

n1 <- length(teachers)
n2 <- length(office)

alpha <- 0.05


# Here we test if the variance of 2 samples is equal
var.test(teachers, office)
# We cannot reject h0, so we assume that the sigmas are equal, so we use first model from tetsing formulas

# Probably we would have var.equal to false if previous thing gave bad answer
t.test(teachers, office, var.equal = T, alternative = "greater")
# since p value is smaller than 0.05, we reject h0 and conclude that the average age of the academia is bigger


###############
# Exercise 7.4

alpha <- 0.01

pre <- c(27, 21, 34, 24, 30, 27, 33, 31, 22, 27)
post <- c(29, 32, 29, 27, 31, 26, 35, 30, 29, 28)

n <- 10

t.test(pre, post, paired=T, alternative = "less")

# since the p-value is bigger than significance level 0.01, we have no reason of rejecting h0, therefore no improvement


###############
# Exercise 7.5
p1 = 14/200
p = 0.04

binom.test(14, 200, 0.04, alternative = "greater")

#since the p-value is smaller than alfa, we reject null, accept alternative, and tell the nigga to fix his stuff


###############
# Exercise 7.6

prop.test(c(455,517), c(700, 1320))

# since alfa is extremely small, we conclude that the proportions differ significantly


###############
# Exercise 7.7

n1 <- 16
n2 <- 16

mu1 <- 175.8
mu2 <- 181.3

sd1 <- 3
sd2 <- 3

z <- (mu1 - mu2 ) / sqrt(sd1^2/n1 + sd2^2/n2)
z < - qnorm(0.99)

# value of test statistic is in critical interval, so they are allowed to use beutiful bottles



###############
# Exercise 8.1

phones <- c(2.5, 1.8, 6.0, 0.5, 8.75, 1.2, 3.75)
ks.test(phones, "pexp", 1/4)



# Exercise 8.2

counts <- c(2792, 3591, 1486, 2131)
labels <- list(c("Voted", "Didn't vote"), c("Men", "Women"))
m1 <- matrix(counts, byrow = T, nrow = 2, ncol = 2, dimnames = labels)

# see also in tutorial how to do this

n<-sum(m1)
r<-rowSums(m1)
c<-colSums(m1)

E<-outer(r,c)/n

sum(((m1-E)/sqrt(E))^2)


#degrees of freedom 2-1 inmultit cu 2-1
qchisq(0.95, 1)




###############
# Exercise 8.4


x <- c(146.08, 150.97, 149.3, 148.48, 148.05, 144.33, 148.95, 147.91)
y <- c(152.28, 152.45, 153.32, 150.84, 153.34, 150.9, 153.84, 152.31, 152.26, 149.51, 151.32, 152.18, 148.9)

shapiro.test(x)

shapiro.test(y)


var.test(x,y)

t.test(x, y, var.equal = T, alternative = "less")


# exercise 8.7

observations <- c(40,1043,30,861,20,801,10,745)
emp <- c(1043, 861, 801, 745)
probs <- c(0.4, 0.3, 0.2, 0.1)
labels = list(c("type 0","type A","type B","type AB"), c("belief", "empirical"))

m1 <- matrix(observations, byrow=T, nrow = 4, ncol = 2, dimnames = labels)

n<-sum(m1)
r<-rowSums(m1)
c<-colSums(m1)

E<-outer(r,c)/n

T <- sum(((m1-E)/sqrt(E))^2)
T >= qchisq(1 - 0.01, (4-1)*(2-1))


?chisq.test
chisq.test(emp, p = probs)

# PAY A LOT OF ATENTION TO THIS, cuz i don't know how to solve it.
# Probably the test is good.

####################
#Exercise 8.8

obs1 <- c(21, 55, 47, 49, 22, 5 ,1,0)
obs2 <- c(47, 63 ,58 ,27 ,4 ,1 ,0,0 )
obs3 <- c(3 ,29, 51, 53, 43, 16, 4, 1)



# we follow 8.1.2

#########obs1
n <- sum(obs1)

pi_vect <- dbinom(c(0,1,2,3,4,5,6,7), 7, 0.3)


npi_vect <- n * pi_vect


di_vect <- ((obs1 - npi_vect)/sqrt(npi_vect))^2

T <- sum(di_vect)

T >= qchisq(1-0.01, 7)

###########obs 2
n <- sum(obs2)

pi_vect <- dbinom(c(0,1,2,3,4,5,6,7), 7, 0.3)


npi_vect <- n * pi_vect


di_vect <- ((obs2 - npi_vect)/sqrt(npi_vect))^2

T <- sum(di_vect)

T >= qchisq(1-0.01, 7)

##################obs 3
n <- sum(obs3)

pi_vect <- dbinom(c(0,1,2,3,4,5,6,7), 7, 0.3)


npi_vect <- n * pi_vect


di_vect <- ((obs3 - npi_vect)/sqrt(npi_vect))^2

T <- sum(di_vect)

T >= qchisq(1-0.01, 7)



########################
