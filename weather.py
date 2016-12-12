from weatherclass import *
import requests
import json
import os.path


def userinput():
    zipcode = input("Please enter your five-digit zipcode: ")
    return zipcode


def displaycurrent(zipcode):
    print('\n')
    print("Current Weather: ")
    current_weather = Currentconditions()
    current = current_weather.get(zipcode)
    print("The temperature is {} degrees F".format(current[0]))
    print("The wind speed is {} mph".format(current[1]))
    print("The wind direction is {}".format(current[2]))
    print("The percipitation is {}".format(current[3]))
    print("The overall weather is {}".format(current[4]))
    print('\n')


def displaytendays(zipcode):
    print("Ten Day Forecast: ")
    tendayforcast = TenDay()
    tendayf = tendayforcast.get(zipcode)
    for i in range(0, 20, 2):
        print("{} you can expect {}".format(tendayf[i], tendayf[(i + 1)]))
    print('\n')


def displaysunrise(zipcode):
    print("Sunrise and Sunset: ")
    sunriseset = SunriseSunset()
    sunrise = sunriseset.get(zipcode)
    print("Sunrise {}:{}".format(sunrise[0], sunrise[1]))
    print("Sunset {}:{}".format(sunrise[2], sunrise[3]))
    print('\n')


def displayalerts(zipcode):
    print("Alerts for your area: ")
    warnings = Alerts()
    warning = warnings.get(zipcode)
    if warning == "no alerts":
        print("No Alerts")
    else:
        warning_format = ", ".join(warning)
        print("Alerts: {}".format(warning_format))
    print('\n')


def displaystorms():
    print("Storms: ")
    storms = Hurricane()
    current_storms = storms.get()
    if current_storms == "no storms":
        print("No Storms")
    else:
        storms_format = ", ".join(current_storms)
        print("Current Storms: {}".format(storms_format))
    print('\n')


def main():
    while True:
        zipcode = userinput()
        if len(zipcode) == 5:
            code = []
            for i in zipcode:
                if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    code.append(i)
            if len(code) == 5:
                break
            else:
                print("It must be five numbers")
        else:
            print("That is not five digits")
    displaycurrent(zipcode)
    displaytendays(zipcode)
    displaysunrise(zipcode)
    displayalerts(zipcode)
    displaystorms()


if __name__ == "__main__":
    main()
