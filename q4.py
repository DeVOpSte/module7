from datetime import datetime

# get currentdate

datetimeObject = datetime.now()

print(datetimeObject)

print('Type: -',type(datetimeObject))

def timeObject(a,b):
    newForm = print(datetime.strftime(a,"Date: %m{0}%d{1}%Y \nTime: %H{2}%M{3}%S".format(b,b,b,b)))
    return newForm


timeObject(datetimeObject,input("Enter sub for dashes:"))

#input("Enter sub for dashes:")