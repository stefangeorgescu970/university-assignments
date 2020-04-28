# Exercise 2.1
election = c("Mary", "Mary", "Mary", "John", "Kate", "Mary", "Peter", "Peter", "John", "John", "Peter", "Kate",
             "Peter", "John", "John", "Mary", "Mary", "Mary", "Kate", "John", "John", "Mary", "John", "Mary",
             "Mary", "John")

nrVotes = length(election)
votesData = table(election) #creates table with each unique entry
percentageData = votesData * 100 / nrVotes # this will give you percentage

barplot(percentageData, main="Election", col = c("red", "blue", "green", "black")) #argument called names.arg to put labels

pie(percentageData, main="Election",  col = c("red", "blue", "green", "black"))

# Exercise 2.2
carsTable = read.csv2("/Users/Stefan/Documents/Facultate/Anul_2/Semestru_1/computerStatistics/CompStat_teaching_materials/CompStat_teaching_materials/DataSets/cars.csv")
carsTable
mpgs = carsTable$mpg


#here be careful, some computation may not work, so be sure to check for that, here there is no check

fc = 3.785*100/(mpgs*1.609)
fc

carsTable = cbind(carsTable, fc)

fuelcons = fc

fuelcons[fc<7] <- "small"
fuelcons[fc>=7 & fc<10] <- "medium"
fuelcons[fc>=10] <- "large"

fuelcons = factor(fuelcons)

fuelcons

carsTable = cbind(carsTable, fuelcons)

carsTable

barplot(table(carsTable$fuelcons))


# Exercise 2.3
mean(fc[!is.na(fc)])
median(fc[!is.na(fc)])
min(fc[!is.na(fc)])
max(fc[!is.na(fc)])
range(fc[!is.na(fc)])
quantile(fc[!is.na(fc)], c(0.1, 0.25, 0.5, 0.75, 0.9))
summary(fc[!is.na(fc)])
mean(fc[!is.na(fc)], trim = 0.1)

var(fc[!is.na(fc)])  # variance
sd(fc[!is.na(fc)])  # standard deviation
IQR(fc[!is.na(fc)])  # interquartile range
diff(range(fc[!is.na(fc)]))  # range
sd(fc[!is.na(fc)])/mean(fc[!is.na(fc)])  # coefficient of variation
boxplot(fc[!is.na(fc)], horizontal = T)
hist(fc[!is.na(fc)])
stem(fc[!is.na(fc)])

# Exercise 2.4
#see tutorial on putting multiple plots in one things


# Exercise 2.5
vector = c(23.30, 24.50, 25.30, 25.30, 24.30, 24.80, 25.20, 24.50, 24.60, 24.10,
           24.30, 26.10, 23.10, 25.50, 22.60, 24.60, 24.30, 25.40, 25.20, 26.80)

plot(1:20, vector, type="l")
plot(1:20, vector)
plot(1:20, vector, type="b", pch = "c" , lty = 1) #change points type and line type respectively

# Exercise 2.6
ages<-c("19 yrs and less", "20-24", "25-29", "30-34", "35-39", "40-44", "45 yrs and more")
ageLevel <- factor(ages)

numbers<-c(19230, 93569, 139853, 86825, 28487, 5975, 305)
data<-data.frame("Age of mother"=ageLevel, "Live births"=numbers)
pie(data$Live.births, labels = data$Age.of.mother)
dotchart(data$Live.births, labels = data$Age.of.mother)
barplot(data$Live.births, names.arg = data$Age.of.mother)

# Exercise 2.7
minutes = c(26, 22, 26, 20, 25, NA, 21, 20, 28, 27, 26, 38, 23, 30, 21, 25, 26, 23, 25, 27, 27, NA, 
            25, 22, 23, 31, 19, NA, 25, 25, 23, 25, 24)

hist(minutes)
#from the histogram, we get that mainly the postman arrives between 21 and 25 minutes, also we have 2
#outliers, one between 31 and 35, one between 36 and 40


stem(minutes)
#all values that are higher than 18 and lower than 20, and so on. one outlier, 38.if we add argument
# scale = 2, we get step one between the values, so we see exactly


boxplot(minutes, horizontal = TRUE)
#those 2 are outliers, yay. 35 is the value of q3 + IQR*3 then 38 definitely is an outlier. no can say
#about the 31 tho.

summ = summary(minutes)

# Exercise 2.8
q1 = summ[2]

q2 = summ[3]

q3 = summ[5]

filteredTimes = minutes[!is.na(minutes)]

filteredTimes = filteredTimes[filteredTimes < 35]

filteredTimes

categorisedTimes = rep("", length(filteredTimes))

categorisedTimes[filteredTimes<q1] = "2Early"

categorisedTimes[filteredTimes>=q1 & filteredTimes<q2] = "Early"

categorisedTimes[filteredTimes==q2] = "Punctual"

categorisedTimes[filteredTimes>q2 & filteredTimes<=q3] = "Late"

categorisedTimes[filteredTimes>q3] = "2Late"

levels = factor(categorisedTimes)

levelTable = table(levels)

barplot(levelTable[c(1,3,5,2,4)])


# Exercise 2.9
carsTable
boxplot(carsTable$accel, horizontal = T)
#needto be separated into countries, not big deal


# Exercise 2.10
library("datasets")
morley
morley$Expt<-factor(morley$Expt)
hist(morley$Speed)
summary(morley$Speed)

# Exercise 2.11
#just no


# Exercise 2.12
wind_mean = function(x, alpha){ 
  x = sort(x)
  k = floor(alpha*length(x))
  if(k > 0){
    x[1:k] = x[k+1]
    x[(length(x) - k + 1) : length(x)] = x[length(x) - k]
    return(mean(x))
  }
}

vect = c(2,2,3,4,5,7,9,11,13,15)
alpha = 0.1
wind_mean(vect, alpha)

# Exercise 2.13
kurtosis = function(x) {
  n<-length(x)
  first<-(n*(n-1))/((n-1)*(n-2)*(n-3))
  third<-(3*(n-1)^2)/((n-2)*(n-3))
  second<-sum((x-mean(x))^4)/var(x)^2
  return(first*second-third)
}
x<-c(1,1,1,1,1,2)
kurtosis(x)


# Exercise 2.14
#basic

