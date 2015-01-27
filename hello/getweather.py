from bs4 import BeautifulSoup
import urllib
from ast import literal_eval

url = "http://api.openweathermap.org/data/2.5/forecast/daily?q=columbus&mode=json$unit=metric&cnt=1/"
soup = BeautifulSoup(urllib.urlopen(url).read())

Tmin = literal_eval(soup.p.string)['list'][0]['temp']['min']
Tmax = literal_eval(soup.p.string)['list'][0]['temp']['max']

print 'Hello, the temperature range in Columbus today is %s to %s' % (Tmin-273.15, Tmax-273.15)