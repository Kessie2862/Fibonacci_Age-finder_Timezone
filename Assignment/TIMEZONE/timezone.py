# Python program that tells a user the timezone in a few selected countries

from datetime import datetime 
import pytz

# Get the standard UTC time 
UTC = pytz.utc

# Check timezones of different countries
london = pytz.timezone('Europe/London')
london_time = datetime.now(london)
print ("Current Date and Time in london:",london_time.strftime('%Y-%m-%d %H:%M:%S %Z %z'))

belgium = pytz.timezone('Europe/Brussels')
belgium_time = datetime.now(belgium)
print ("Current Date and Time in belgium:",belgium_time.strftime('%Y-%m-%d %H:%M:%S %Z %z'))

czech = pytz.timezone('Europe/Prague')
czech_time = datetime.now(czech)
print ("Current Date and Time in czech:",czech_time.strftime('%Y-%m-%d %H:%M:%S %Z %z'))

denmark = pytz.timezone('Europe/Copenhagen')
denmark_time = datetime.now(denmark)
print ("Current Date and Time in denmark:",denmark_time.strftime('%Y-%m-%d %H:%M:%S %Z %z'))

ghana = pytz.timezone('Africa/Accra')
ghana_time = datetime.now(ghana)
print ("Current Date and Time in ghana:",ghana_time.strftime('%Y-%m-%d %H:%M:%S %Z %z'))

south_africa = pytz.timezone('Africa/Johannesburg')
south_africa_time = datetime.now(south_africa)
print ("Current Date and Time in south_africa:",south_africa_time.strftime('%Y-%m-%d %H:%M:%S %Z %z'))

egypt = pytz.timezone('Africa/Cairo')
egypt_time = datetime.now(egypt)
print ("Current Date and Time in egypt:",egypt_time.strftime('%Y-%m-%d %H:%M:%S %Z %z'))












