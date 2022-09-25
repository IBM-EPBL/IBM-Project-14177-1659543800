# import the random and time library in python script.
import random
import time

# iterate the random values of Temperature and humidity within the specified range.
while True:
    temperature = random.randint(32, 212)
    humidity = random.randint(0, 100)
    #print the values of Temperature and humidity.
    print("Temperature is : "+str(temperature)+"°F")
    print("Temperature in celsius : "+str(((temperature-32)*5)//9)+"℃")
    print("The Humidity is : "+str(humidity)+"%")
    # check if the temperature values are higher than 100°F.
    if (temperature >= 100):
        print("High Temperature Alert : "+str(temperature)+"°F")
        time.sleep(10)
