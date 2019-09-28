
import time;

localtime = time.asctime( time.localtime(time.time()) )
print ("Waktu lokal saat ini :", localtime)

import calendar

cal = calendar.month(2019, 8)
print ("Dibawah ini adalah kalender:")
print (cal)