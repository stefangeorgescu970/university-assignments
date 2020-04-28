#exercise 2.7

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

#exercise 2.8

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


#exercise 2.12

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

#exercise 2.13

#kurtosis shows how wide is the distribution comparing to values


kurtosis = function(x, )
