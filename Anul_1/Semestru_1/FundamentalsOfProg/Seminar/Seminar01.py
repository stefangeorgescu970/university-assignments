#Compute the sum of the first n natural numbers


def sumToN(n):
    """
    Returns the sum of the first n natural numbers.
    Arguments: n - The number to which the sum is calculated, n>0, natural
    Returns: The sum of the first n numbers
    """
    sum = 0
    for i in range(n):
        sum += i
    return sum

print("The sum is ",sumToN(3))



#Check if a given number n is prime"

from math import sqrt

def isPrime(n):
    if n < 2 or n % 2 == 0 and n>2:
        return False
    for div in range(3,int(sqrt(n))+1,2)
        if n % div == 0:
            return False
    return True


#Compute the greatest common divisor between two integers a and b


def gcd(a,b):
    """
    r=a%b
    while r!=0:
        a=b
        b=r
        r=a&b;
    return b
    """
    while b!=0:
        a,b=b,a%b
    return a if a > 0 else a * -1

#Compile the first prime number greater then n

def nextPrime(n):
    while True:
        n += 1
        if isPrime(n):
            return n


#Print the first k prime numbers greater than a given integer n

def nextKPrimes(k,n):
    for i in range (k):
        n=nextPrime(n)
        print(n)

        
#Compute the age of a person in number fo days. So, given the date of birth of a person in the format dd mm yyyy
#(three integers), and the current date (in the same format) compute the age of that person
#in the number of days.

        
    




        



