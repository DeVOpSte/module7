#question 2
from datetime import timedelta
import datetime


currentDate = datetime.datetime.today()

def minute():
    min = timedelta(seconds=-60)
    Onemin = currentDate - min
    #print(Onemin)
    return Onemin

def Twoyear():

    yearTwo = timedelta(days= 730)
    finalTime = minute() + yearTwo
    return finalTime


print("The current time is: {0}".format(currentDate))

print("The updated time is:",minute())

print("The next updated time is:",Twoyear())

# question 3
obj = timedelta(days=100,hours=10,minutes=13)

print(obj)


