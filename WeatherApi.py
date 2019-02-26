import requests 
import simplejson as json
from bs4 import BeautifulSoup
import sys

#Welcome Message + Asks for user location and Tempreture Choice
print("Welcome to Weather Forcaster:")
Location = input("Please Enter Your Location:")

#link used for the API
Weather_api ='https://api.openweathermap.org/data/2.5/weather?APPID=89da9ee78fce51911e8ca20b9906d704&q='

#Adds Location onto the end of the API link
User_Weather_api = Weather_api + Location

#Trys to Pull From the API
try:
    Weather = requests.get(User_Weather_api).json()
except:
    print("Connection Error Please Check Internet..")
    print("Shutting Down...")
    sys.exit(0)

try:
#Selects the "Main" from the Weather Dictionary
    Weather_main = Weather['weather'][0]['main']
#Selects the Tempreture from the Main Dictionary
    Weather_temp_float = float(Weather['main']['temp'])
#Selects the Description from the Weather Dictionary
    Weather_description = Weather['weather'][0]['description']
#Selects the Windspeed from the Wind Dictionary and saves a float
    Weather_windspeed_float = float(Weather ['wind']['speed'])
#Converts Wind float to a String
    Weather_windspeed = str(Weather_windspeed_float)
except:
    print("Location Invalid Please Restart and Enter a Valid Location")
    print("Shutting Down....")
    input("Press Enter To Continue...")
    sys.exit(0)

print("Would you like to receive the Tempreture in Celcius or Fahrenheit")
Temp = input("Please Enter Either Celcius (C) or Fahrenheit (F):")


#DataPrinting
print('Location:' + Location)
print('Main:' + Weather_main)
print('Description:' + Weather_description)
print('Wind Speed:' + Weather_windspeed)
TempCelcius = (Weather_temp_float-273)
TempFar = (Weather_temp_float-273)*(9/5)+32

#Prints Data Based on User Choice
if Temp.lower() =="c":
    print('Tempreture:', round(TempCelcius,2),"C")
elif Temp.lower()=="f":
    print('Tempreture:', round(TempFar,2),"F")
else:
    print('Invalid Tempreture Choice: Celcius selected as default')
    print('Tempreture:', round(TempCelcius,2),"C")

