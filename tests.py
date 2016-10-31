import ephem 
from pytz import timezone
import pytz
#defining an observer 
obs = ephem.Observer() 
#defining position 
longi = ' -3.691944' 
lat = '40.418889' 
timezoneLocal='Europe/Madrid'


myzone = timezone(timezoneLocal)
obs.long = ephem.degrees(longi) 
obs.lat = ephem.degrees(lat) 
print ("long = ", obs.long, "lat = ", obs.lat )
#defining date 
date = '2016/10/31' 
obs.date = ephem.Date(date) 
#defining an astronomic object; Sun in this case 
sun = ephem.Sun(obs) 
r1 = obs.next_rising(sun) 
s1 = obs.next_setting(sun) 
print ("rising sun (UTC time): ", r1) 
print ("setting sun (UTC time): ", s1 )
r1_lt = ephem.Date(r1 - 6 * ephem.hour) #local time 
(y, mn, d, h, min, s) = r1_lt.tuple() 
print ("rising sun: (local time): {:.2f}".format( h + min/60. + s/3600. ))
print ("local time rising ", ephem.localtime(r1))

utc= pytz.utc
utc_dt = utc.localize( ephem.localtime(r1))
myloc_dt = utc_dt.astimezone(myzone)
print (myloc_dt)





