vector1<-c(1,2,3,4,-2,4,1,0,1,2)
vector1
vector1[1]
length(vector1)
sum(vector1)

#excersise 1.5

#a
vector1[vector1>=0]


#b
vector1[seq(1, length(vector1), 2)]

#c  this doesn't work yet
vector1[vector1==0] <- NA


#d
sort(vector1, decreasing = TRUE)

#d manually

#to check for na, use is.na(vector1)
vector1[is.na(vector1)] <- 0

v2<-rep(0, length(vector1))
v3<-vector1
j<-1
while(length(v3)>0) {
  maxV3 <- max(v3)
  len<-sum(v3==maxV3)
  for(i in 0:(len-1)){
    v2[j+i]<-maxV3
  }
  j<-j+len
  v3<-v3[v3!=maxV3]
}

#Exercise 1.8

#a
sum(0:10) #equiv of seq(1,10)

#b
# use ^ for power

sum((0:10)^2)^3

#c
i<-rep((1:10), 20)
j<-rep((1:20), each=10)
i*j
sum(i*j)

#f
sum(seq(1,99,2))*sum(seq(2,100,2))

#g
i<-rep(seq(1,99,2), 50)
j<-rep(seq(2,100,2), each=50)
i*j
sum(i*j)

#e
log(prod(2:100))
sum(log(2:100))


#1.6

matrix(c(3, 1.2, 5, 3.2, -1, 0 ,1, -3,-4), nrow=3) #they get added on columns, not rows
A<-t(matrix(c(3, 1.2, 5, 3.2, -1, 0 ,1, -3,-4), nrow=3)) #transposed

A[2,2]

matrix(A[3,], nrow = 1)
matrix(A[,1], ncol = 1)

b<-c(4,-3,2)

solve(A,b)

#Data frame example ex1.12 ceva

data1 <- data.frame(nums = sample(1:10, 10, replace = TRUE), chars = sample(letters, 10, replace=TRUE))
data1
data2<- data1[seq(2, nrow(data1), 2),]
data2$nums<-data2$nums*2
data2
rbind(data1, data2)
data3<-data.frame(num2 = log(data2$nums))
data3
cbind(data1, data3)




