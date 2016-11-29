import requests
import json
import os.path


class Currentconditions:
    def __init__(self):
        pass

    def get(self, zipcode):
        self.zipcode = zipcode
        address = "http://api.wunderground.com/api/5a7e29d09f0d254e/conditions/settings/q/{}.json".format(zipcode)
        r = requests.get(address)
        temperature = r.json()["current_observation"]["temp_f"]
        windspeed = r.json()["current_observation"]["wind_mph"]
        winddirection = r.json()["current_observation"]["wind_dir"]
        percipitation = r.json()["current_observation"]["precip_today_string"]
        weather = r.json()["current_observation"]["weather"]
        return [temperature, windspeed, winddirection, percipitation, weather]


class TenDay:
    def __init__(self):
        pass

    def get(self, zipcode):
        self.zipcode = zipcode
        address = "http://api.wunderground.com/api/5a7e29d09f0d254e/forecast10day/settings/q/{}.json".format(zipcode)
        r = requests.get(address)
        tenday = r.json()["forecast"]["txt_forecast"]["forecastday"]
        alldays = []
        for number in [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]:
            day = tenday[number]["title"]
            alldays.append(day)
            weather = tenday[number]["fcttext"]
            alldays.append(weather)
        return alldays

class SunriseSunset:
    def __init__(self):
        pass

    def get(self, zipcode):
        self.zipcode = zipcode
        address = "http://api.wunderground.com/api/5a7e29d09f0d254e/astronomy/settings/q/" + str(zipcode) + ".json"
        r = requests.get(address)
        sunrisehour = r.json()["moon_phase"]["sunrise"]["hour"]
        sunriseminute = r.json()["moon_phase"]["sunrise"]["minute"]
        sunsethour = r.json()["moon_phase"]["sunset"]["hour"]
        sunsetminute = r.json()["moon_phase"]["sunset"]["minute"]
        return [str(sunrisehour), str(sunriseminute), str(sunsethour), str(sunsetminute)]


class Alerts:
    def __init__(self):
        pass

    def get(self, zipcode):
        self.zipcode = zipcode
        address = "http://api.wunderground.com/api/5a7e29d09f0d254e/alerts/settings/q/" + str(zipcode) + ".json"
        r = requests.get(address)
        results = r.json()["alerts"]
        if len(results) == 0:
            return "no alerts"
        else:
            return r.json()["alerts"]["type"]


class Hurricane():
    def __init__(self):
        pass

    def get(self, zipcode):
        self.zipcode = zipcode
        address = "http://api.wunderground.com/api/5a7e29d09f0d254e/currenthurricane/settings/q/{}.json".format(zipcode)
        r = requests.get(address)
        try:
            storm = r.json()["currenthurricane"][0]["stormInfo"]["stormName_Nice"]
        except IndexError:
            return "no storms"
        else:
            return storm
