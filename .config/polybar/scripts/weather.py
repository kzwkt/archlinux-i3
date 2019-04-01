#!/usr/bin/env python

import json
import urllib
import urllib.parse
import urllib.request
import os


def main():
    city = "Kathmandu,NP"
    api_key = "fe36d573c1e17e8b6ea1a81b4d4ff562"

    try:
        data = urllib.parse.urlencode({'q': city, 'appid': api_key, 'units': 'metric'})
        weather = json.loads(urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?' + data)
            .read())
        desc = weather['weather'][0]['description'].capitalize()
        icons = {"Thunderstorm":"", "Drizzle":"", "Rain":"", "Snow":"", "Mist":"", "Smoke":"", "Haze":"", "Dust":"", "Fog":"", "Sand":"", "Dust":"", "Ash":"", "Squall":"", "Tornado":"", "Clear":"", "Clouds":""}
        icon = icons.get (desc, 'none')
        temp = int(float(weather['main']['temp']))
        #return icon + ' ' + desc + ' ' + temp + ''
        return ' {}  {}, {}°C '.format(icon, desc, temp)
        #return '{}°C'.format(temp)
    except:
        return ''


if __name__ == "__main__":
	print(main())
