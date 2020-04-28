data("iris")
iris

eyesSetosa <- iris[iris$Species=="setosa", ]
eyesSetosaSepalLength <- eyesSetosa$Sepal.Length

eyesVirginica <- iris[iris$Species=="virginica", ]
eyesVirginicaSepalLength <- eyesVirginica$Sepal.Length

eyesVersicolor <- iris[iris$Species=="versicolor", ]
eyesVersicolorSepalLength <- eyesVersicolor$Sepal.Length


# We will now apply summary function for each set of eye species. This will give us bsic statistics 
# position, such as the minimum, maximum, median and mean plus the other 2 quartiles.
sumSetosa <- summary(eyesSetosaSepalLength)

sumVirginica <- summary(eyesVirginicaSepalLength)

sumVersicolor <- summary(eyesVersicolorSepalLength)


# For basic dispertion statistics, we will check standard deviation, variance, interquartial range 
# and range. Also, the boxplots will help in this analisys.

sd(eyesSetosaSepalLength)
var(eyesSetosaSepalLength)
iqrSetosa <- IQR(eyesSetosaSepalLength)
range(eyesSetosaSepalLength)
boxplot(eyesSetosaSepalLength, horizontal = T)

sd(eyesVirginicaSepalLength)
var(eyesVirginicaSepalLength)
iqrVirginica <- IQR(eyesVirginicaSepalLength)
range(eyesVirginicaSepalLength)
boxplot(eyesVirginicaSepalLength, horizontal = T)

sd(eyesVersicolorSepalLength)
var(eyesVersicolorSepalLength)
iqrVersicolor <- IQR(eyesVersicolorSepalLength)
range(eyesVersicolorSepalLength)
boxplot(eyesVersicolorSepalLength, horizontal = T)

#histograms of each sample

hist(eyesSetosaSepalLength)
# From the histogram we get that most values are centered around 5, and that there are no outliers.

hist(eyesVersicolorSepalLength)
# From the histogram we get that most of the results are plced between 5.5 and 6.0, and that there are
# no outliers.

hist(eyesVirginicaSepalLength)
# From the histogram we get that most of the results are placed between 6 and 6.5 and that we hve one 
# outliers between 4.5 and 5


# In order to detect outliers, we will need the vlues of IQR and Q1 and Q3, in order to compute the 
# margins from which outliers start.
lbSetosa <- sumSetosa[2] - (3/2)*iqrSetosa
rbSetosa <- sumSetosa[5] + (3/2)*iqrSetosa
outlierSetosa <- eyesSetosaSepalLength[eyesSetosaSepalLength <= lbSetosa | eyesSetosaSepalLength >= rbSetosa]
outlierSetosa
#This means setosa has no outliers

lbVersicolor <- sumVersicolor[2] - (3/2)*iqrVersicolor
rbVersicolor <- sumVersicolor[5] + (3/2)*iqrVersicolor
outlierVersicolor <- eyesVersicolorSepalLength[eyesVersicolorSepalLength <= lbVersicolor | eyesVersicolorSepalLength >= rbVersicolor]
outlierVersicolor
#This means Versicolor has no outliers

lbVirginica <- sumVirginica[2] - (3/2)*iqrVirginica
lbVirginica
rbVirginica <- sumVirginica[5] + (3/2)*iqrVirginica
outlierVirginica <- eyesVirginicaSepalLength[eyesVirginicaSepalLength <= lbVirginica | eyesVirginicaSepalLength >= rbVirginica]
outlierVirginica
#This means Virginica has one outlier, 4.9 


#To answer the final question, let's reprint the summary statistics, removing outlier from Virginica Set
sumSetosa
summary(eyesVirginicaSepalLength[eyesVirginicaSepalLength > lbVirginica])
sumVersicolor

#It is clear that species Virginic has the highest value of sepal length

#Now, for comparing width

eyesSetosa <- iris[iris$Species=="setosa", ]
eyesSetosaSepalWidth <- eyesSetosa$Sepal.Width

eyesVirginica <- iris[iris$Species=="virginica", ]
eyesVirginicaSepalWidth <- eyesVirginica$Sepal.Width

eyesVersicolor <- iris[iris$Species=="versicolor", ]
eyesVersicolorSepalWidth <- eyesVersicolor$Sepal.Width


# We will now apply summary function for each set of eye species. This will give us bsic statistics 
# position, such as the minimum, maximum, median and mean plus the other 2 quartiles.
sumSetosa <- summary(eyesSetosaSepalWidth)

sumVirginica <- summary(eyesVirginicaSepalWidth)

sumVersicolor <- summary(eyesVersicolorSepalWidth)


# For basic dispertion statistics, we will check standard deviation, variance, interquartial range 
# and range. Also, the boxplots will help in this analisys.

sd(eyesSetosaSepalWidth)
var(eyesSetosaSepalWidth)
iqrSetosa <- IQR(eyesSetosaSepalWidth)
range(eyesSetosaSepalWidth)
boxplot(eyesSetosaSepalWidth, horizontal = T)

sd(eyesVirginicaSepalWidth)
var(eyesVirginicaSepalWidth)
iqrVirginica <- IQR(eyesVirginicaSepalWidth)
range(eyesVirginicaSepalWidth)
boxplot(eyesVirginicaSepalWidth, horizontal = T)

sd(eyesVersicolorSepalWidth)
var(eyesVersicolorSepalWidth)
iqrVersicolor <- IQR(eyesVersicolorSepalWidth)
range(eyesVersicolorSepalWidth)
boxplot(eyesVersicolorSepalWidth, horizontal = T)

#histograms of each sample

hist(eyesSetosaSepalWidth)
# From the histogram we get that most values are between 3.0 and 3.5, and we only have one measurement for lower than 2.5.

hist(eyesVersicolorSepalWidth)
# From the histogram we get that most of the results are plced between 2.8 and 3.0, and that there are
# no outliers.

hist(eyesVirginicaSepalWidth)
# From the histogram we get that most of the results are placed between 2.5 and 3 and that we hve one a few observations bigger.


# In order to detect outliers, we will need the vlues of IQR and Q1 and Q3, in order to compute the 
# margins from which outliers start.
lbSetosa <- sumSetosa[2] - (3/2)*iqrSetosa
rbSetosa <- sumSetosa[5] + (3/2)*iqrSetosa
outlierSetosa <- eyesSetosaSepalWidth[eyesSetosaSepalWidth <= lbSetosa | eyesSetosaSepalWidth >= rbSetosa]
outlierSetosa
#This means setosa has 2 outliers, 2.3 and 4.4

lbVersicolor <- sumVersicolor[2] - (3/2)*iqrVersicolor
rbVersicolor <- sumVersicolor[5] + (3/2)*iqrVersicolor
outlierVersicolor <- eyesVersicolorSepalWidth[eyesVersicolorSepalWidth <= lbVersicolor | eyesVersicolorSepalWidth >= rbVersicolor]
outlierVersicolor
#This means Versicolor has no outliers

lbVirginica <- sumVirginica[2] - (3/2)*iqrVirginica
rbVirginica <- sumVirginica[5] + (3/2)*iqrVirginica
outlierVirginica <- eyesVirginicaSepalWidth[eyesVirginicaSepalWidth <= lbVirginica | eyesVirginicaSepalWidth >= rbVirginica]
outlierVirginica
#This means Virginica has 3 outliers, 2.2, 3.8 twice


#To answer the final question, let's reprint the summary statistics, removing outlier from required Sets
summary(eyesSetosaSepalWidth[eyesSetosaSepalWidth > lbSetosa | eyesSetosaSepalWidth < rbSetosa])
summary(eyesVirginicaSepalWidth[eyesVirginicaSepalWidth > lbVirginica | eyesVirginicaSepalWidth < rbVirginica])
sumVersicolor

#It is clear that species Setosa has the highest value of sepal Width

# The answer for question 2 is no, since species are different for length and width.

numberSetosa <- length(eyesSetosaSepalLength)
numberVirginica <- length(eyesVirginicaSepalLength)
numberVersicolor <- length(eyesVersicolorSepalLength)

numberObservtions <- c(numberSetosa, numberVirginica, numberVersicolor)

barplot(numberObservtions, names.arg = c("Setosa", "Virginica", "Versicolor"))

#We can see that all samples (1 for each species) has 50 observations
