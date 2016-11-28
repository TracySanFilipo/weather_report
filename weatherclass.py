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
        day1day = tenday[0]["title"]
        alldays.append(day1day)
        day1weather = tenday[0]["fcttext"]
        alldays.append(day1weather)
        day2day = tenday[2]["title"]
        alldays.append(day2day)
        day2weather = tenday[2]["fcttext"]
        alldays.append(day2weather)
        day3day = tenday[4]["title"]
        alldays.append(day3day)
        day3weather = tenday[4]["fcttext"]
        alldays.append(day3weather)
        day4day = tenday[6]["title"]
        alldays.append(day4day)
        day4weather = tenday[6]["fcttext"]
        alldays.append(day4weather)
        day5day = tenday[8]["title"]
        alldays.append(day5day)
        day5weather = tenday[8]["fcttext"]
        alldays.append(day5weather)
        day6day = tenday[10]["title"]
        alldays.append(day6day)
        day6weather = tenday[10]["fcttext"]
        alldays.append(day6weather)
        day7day = tenday[12]["title"]
        alldays.append(day7day)
        day7weather = tenday[12]["fcttext"]
        alldays.append(day7weather)
        day8day = tenday[14]["title"]
        alldays.append(day8day)
        day8weather = tenday[14]["fcttext"]
        alldays.append(day8weather)
        day9day = tenday[16]["title"]
        alldays.append(day9day)
        day9weather = tenday[16]["fcttext"]
        alldays.append(day9weather)
        day10day = tenday[18]["title"]
        alldays.append(day10day)
        day10weather = tenday[18]["fcttext"]
        alldays.append(day10weather)
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
        storm = r.json()["currenthurricane"][0]["stormInfo"]["stormName_Nice"]
        return storm
