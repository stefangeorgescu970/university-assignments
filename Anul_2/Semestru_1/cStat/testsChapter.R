###############
# Exercise 7.3

teachers <- c(14, 17, 7, 33, 2, 24, 26, 22, 12)
office <- c(13, 15, 3, 2, 25, 4, 1, 18, 6, 9, 20, 11, 5, 1, 7)

n1 <- length(teachers)
n2 <- length(office)

alpha <- 0.05


qf(alpha/2, n1-1, n2-1)
qf(1 - alpha/2, n1-1, n2-1)


var.test(teachers, office)
# We cannot reject h0, so we assume that the sigmas are equal, so we use first model from tetsing formulas


qt(1-alpha, n1 + n2 - 2)

t.test(teachers, office, var.equal = T, alternative = "greater")
# since p value is smaller than 0.05

###############
# Exercise 7.5
p1 = 14/200
p = 0.04

binom.test(14, 200, 0.04, alternative = "greater")


###############
# Exercise 7.6

prop.test(c(455,517), c(700, 1320))


###############
# Exercise 8.1

phones <- c(2.5, 1.8, 6.0, 0.5, 8.75, 1.2, 3.75)
ks.test(phones, "pexp", 1/4)


###############
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

t.test(x, y, var.equal = T)
