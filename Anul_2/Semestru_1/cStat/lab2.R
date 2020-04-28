# exercise 2.5

vector = c(23.30, 24.50, 25.30, 25.30, 24.30, 24.80, 25.20, 24.50, 24.60, 24.10,
24.30, 26.10, 23.10, 25.50, 22.60, 24.60, 24.30, 25.40, 25.20, 26.80)

plot(1:20, vector, type="l")
plot(1:20, vector)
plot(1:20, vector, type="b", pch = "c" , lty = 1) #change points type and line type respectively


# exercise 2.1

election = c("Mary", "Mary", "Mary", "John", "Kate", "Mary", "Peter", "Peter", "John", "John", "Peter", "Kate",
"Peter", "John", "John", "Mary", "Mary", "Mary", "Kate", "John", "John", "Mary", "John", "Mary",
"Mary", "John")

nrVotes = length(election)
votesData = table(election) #creates table with each unique entry
percentageData = votesData * 100 / nrVotes # this will give you percentage

barplot(percentageData, main="Election", col = c("red", "blue", "green", "black")) #argument called names.arg to put labels

pie(percentageData, main="Election",  col = c("red", "blue", "green", "black"))

#use round() to round numbers

#excercise 2.2

#either use double backslash or normal slash 
carsTable = read.csv2("h:/Windows7/Desktop/CompStat_teaching_materials/CompStat_teaching_materials/DataSets/cars.csv")
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

# exercise 2.3

fcWithoutNa = fc[!is.na(fc)]

mean(fcWithoutNa)

median(fcWithoutNa)

var(fcWithoutNa)

sd(fcWithoutNa)

quantile(fcWithoutNa, 0.25) #find a value st .25 of the values to the left, .75 on the right

range(fcWithoutNa) #also can be found with min max

summary(fcWithoutNa)


IQR(fcWithoutNa)


hist(fcWithoutNa)


#exercise 2.6