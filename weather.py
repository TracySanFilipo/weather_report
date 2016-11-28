from weatherclass import *
import requests
import json
import os.path


def userinput():
    zipcode = input("Please enter your five-digit zipcode: ")
    return zipcode


def main():
    while True:
        zipcode = userinput()
        if len(zipcode) == 5:
            code = []
            for item in zipcode:
                if item in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    code.append(item)
            if len(code) == 5:
                break
            else:
                print("It must be five numbers")
        else:
            print("That is not five digits")
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
    print("Ten Day Forcast: ")
    tendayforcast = TenDay()
    tendayf = tendayforcast.get(zipcode)
    print("{} you can expect {}".format(tendayf[0], tendayf[1]))
    print("{} you can expect {}".format(tendayf[2], tendayf[3]))
    print("{} you can expect {}".format(tendayf[4], tendayf[5]))
    print("{} you can expect {}".format(tendayf[6], tendayf[7]))
    print("{} you can expect {}".format(tendayf[8], tendayf[9]))
    print("{} you can expect {}".format(tendayf[10], tendayf[11]))
    print("{} you can expect {}".format(tendayf[12], tendayf[13]))
    print("{} you can expect {}".format(tendayf[14], tendayf[15]))
    print("{} you can expect {}".format(tendayf[16], tendayf[17]))
    print("{} you can expect {}".format(tendayf[18], tendayf[19]))
    print('\n')
    print("Sunrise and Sunset: ")
    sunriseset = SunriseSunset()
    sunrise = sunriseset.get(zipcode)
    print("Sunrise {}:{}".format(sunrise[0], sunrise[1]))
    print("Sunset {}:{}".format(sunrise[2], sunrise[3]))
    print('\n')
    print("Alerts for your area: ")
    warnings = Alerts()
    warning = warnings.get(zipcode)
    print("Alerts: {}".format(warning))
    print('\n')
    print("Storms: ")
    storms = Hurricane()
    storm = storms.get(zipcode)
    print("Current Storms: {}".format(storm))
    print('\n')

if __name__ == "__main__":
    main()
