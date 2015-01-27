from flask import Flask
from google.appengine.ext import ndb
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

class Event_in_NDB(ndb.Model):
    name = ndb.StringProperty()
    category = ndb.IntegerProperty()
    server_date = ndb.DateTimeProperty(auto_now_add=True)

@app.route('/')
def index():
    return 'Index'

@app.route('/checkin')
def hello():
    testEvent = Event_in_NDB(name = 'check in',category = 0)
    testEventKey = testEvent.put()
    return 'Hello, the time of your visit is %s' % testEvent.server_date

@app.route('/checkin_count')
def checkin_count():
    results = Event_in_NDB.query(Event_in_NDB.category==0)
    checkin_times = results.count()
    return 'The number of visits: %d' % checkin_times

@app.route('/showNDB')
def showNDB():
    """read from database"""
    results = Event_in_NDB.query(Event_in_NDB.category==0)
    # the query return is an iterator
    message = ""
    for result in results:
        message += (result.name+'\n')
    return message

@app.route('/greeting/')
@app.route('/greeting/<name>')
def greeting(name='Stranger'):
    # show the user profile for that user
    return 'Hello, %s!' % name

from datetime import datetime
@app.route('/hello')
def timenow():
    now = datetime.now()
    return 'Hello, the server time is %s' % now

from bs4 import BeautifulSoup
import urllib
from ast import literal_eval
@app.route('/weather')
def weather_columbus():
    url = "http://api.openweathermap.org/data/2.5/forecast/daily?q=columbus&mode=json$unit=metric&cnt=1/"
    soup = BeautifulSoup(urllib.urlopen(url).read())
    Tmin = literal_eval(soup.contents[0])['list'][0]['temp']['min']
    Tmax = literal_eval(soup.contents[0])['list'][0]['temp']['max']
    return 'Hello, the temperature range in Columbus today is %s to %s deg' % (Tmin-273.15, Tmax-273.15)

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404