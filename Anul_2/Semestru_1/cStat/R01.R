# to search for a function by keyword, use ??"whatever you want to find"
# if you know the name of the function use ?nameOfFunction

# to introduce sequences: 1:10

# to get remainder: %%

# Exercise 1.1
people <- read.table("/Users/Stefan/Documents/Facultate/Anul_2/Semestru_1/computerStatistics/CompStat_teaching_materials/CompStat_teaching_materials/DataSets/example.csv",
                     comment.char = "#",
                     sep = ";",
                     dec = ",",
                     header = T)

bdates <- strptime(people$BirthDate, "%Y-%m-%d")

age <- floor(as.numeric(difftime(Sys.time(), bdates, units = "weeks")/52))

people<- cbind(people, Age=age)

people


#Exercise 1.2
#1 foot is equal to 0.3048 meters

inFeet <- people$Height/30.48
people <- cbind(people, HeightInFeet = inFeet)
people


#Exercise 1.3
head(ToothGrowth)

ToothGrowth$dose <- factor(ToothGrowth$dose)
levels(ToothGrowth$dose)
levels(ToothGrowth$supp)

tapply(ToothGrowth$len, ToothGrowth$supp, mean)


#Exercise 1.4

# infinite cycle lol


#Exercise 1.5

myVector <- c(23,51,0,-2,32,62,12,1.2,35.3,-9,0)
#a
myVector[myVector >= 0]
#b
myVector[seq(1,length(myVector), 2)]
#c
myVector[myVector == 0] <- NA
#d
sort(myVector, decreasing = T)


#Exercise 1.6

values <- c(3,1.2,5,3.2,-1,0,1,-3,4)
myMatrix <- matrix(values, nrow = 3, byrow = T)

#a
myMatrix[2,2]

#b
myMatrix[3,]

#c
myMatrix[,1]

#d
b <- c(4,-3,2)
solve(myMatrix, b)

#e
inverse = solve(A)
solution <- inverse %*% b
solution
#here i did not get the same result, no need to look into it


#Exercise 1.7

# I know, no use of wasting time


#Exercise 1.8

#a
sum(0:10) 

#b
sum((0:10)^2)^3

#c
i<-rep((1:10), 20)
j<-rep((1:20), each=10)
i*j
sum(i*j)

#d
i<-rep((1:10), 3)
j<-rep((1:3), each=10)
1/sqrt(sum(i^j))

#e
log(prod(2:100))
sum(log(2:100)) #this is better for bigger values

#f
sum(seq(1,99,2))*sum(seq(2,100,2))

#g
i<-rep(seq(1,99,2), 50)
j<-rep(seq(2,100,2), each=50)
i*j
sum(i*j)


#Exercise 1.9
#basic logical operators


#Exercise 1.10 and Exercise 1.11
#maybe look into them later, right now out of scope


#Exercise 1.12
data1 <- data.frame(nums = sample(1:10, 10, replace = TRUE), chars = sample(letters, 10, replace=TRUE))
data1
data2<- data1[seq(2, nrow(data1), 2),]
data2$nums<-data2$nums*2
data2
rbind(data1, data2)
data3<-data.frame(num2 = log(data2$nums))
data3
data1 <- cbind(data1, data3)
data1


#Exercise 1.13

patients <- read.table("/Users/Stefan/Documents/Facultate/Anul_2/Semestru_1/computerStatistics/CompStat_teaching_materials/CompStat_teaching_materials/DataSets/patients.csv",
                     comment.char = "#",
                     sep = ";",
                     dec = ".",
                     header = T)
patients$Temperature..F. <- (patients$Temperature..F. - 32) * 5 / 9

bmi <- patients$Weight * 10000 / (patients$Height^2)
patients <- cbind(patients, BMI = bmi)
whoScale <- rep("", 10)
whoScale[bmi < 18.5] <- "Underweight"
whoScale[bmi >= 18.5 & bmi < 25] <- "Normal"
whoScale[bmi >= 25 & bmi < 30] <- "Overweight"
whoScale[bmi >= 30] <- "Obese"

patients<-cbind(patients, scale=whoScale)

subset(patients, scale=="Underweight", select = Name)

#jump over date conversion and export for now

order(patients$Name)
patients[order(patients$Name),]
