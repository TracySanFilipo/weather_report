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
        current = r.json()["current_observation"]
        temperature = current["temp_f"]
        windspeed = current["wind_mph"]
        winddirection = current["wind_dir"]
        percipitation = current["precip_today_string"]
        weather = current["weather"]
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
        for number in range(0, 20, 2):
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
        address = "http://api.wunderground.com/api/5a7e29d09f0d254e/astronomy/settings/q/{}.json".format(zipcode)
        r = requests.get(address)
        sun = r.json()["moon_phase"]
        sunrise_hr = sun["sunrise"]["hour"]
        sunrise_min = sun["sunrise"]["minute"]
        sunset_hr = sun["sunset"]["hour"]
        sunset_min = sun["sunset"]["minute"]
        return [str(sunrise_hr), str(sunrise_min), str(sunset_hr), str(sunset_min)]


class Alerts:
    def __init__(self):
        pass

    def get(self, zipcode):
        self.zipcode = zipcode
        address = "http://api.wunderground.com/api/5a7e29d09f0d254e/alerts/settings/q/{}.json".format(zipcode)
        r = requests.get(address)
        results = r.json()["alerts"]
        if len(results) == 0:
            return "no alerts"
        else:
            alerts_list = []
            for i in range(0, len(results)):
                alerts_list.append(results[i]["description"])
            return alerts_list

class Hurricane():
    def __init__(self):
        pass

    def get(self):
        hurricanes = "http://api.wunderground.com/api/5a7e29d09f0d254e/currenthurricane/view.json"
        r = requests.get(hurricanes)
        storm = r.json()["currenthurricane"]
        if len(storm) == 0:
            return "no storms"
        else:
            storm_list = []
            for i in range(0, len(storm)):
                storm_list.append(storm[i]["stormInfo"]["stormName_Nice"])
            return storm_list
