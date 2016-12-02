from django.shortcuts import get_object_or_404, get_list_or_404
from django.conf import settings
from django.db import models
# from eq_map import models, serializers
# # from models import Earthquake
# from models import Location
# from models import UserEarthquake
# from serializers import EarthquakeSerializer
# from eq_map.serializers import LocationSerializer
# from serializers import UserEarthquakeSerializer
# from serializers import UserSerializer
import http.client
import csv

conn = http.client.HTTPConnection("earthquake.usgs.gov")

headers = {
    'cache-control': "no-cache",
    }


starttime = "2014-01-01"
endtime = "2016-11-09"
minmag = 3
lati = 37.784
longi = -122.395
radius = 50
name = "test"


# def make(starttime, endtime, minmag, lati, longi, radius, name):
def make():
    conn.request("GET", "/fdsnws/event/1/query?format=csv&starttime="+starttime+"&endtime="+endtime+"&minmagnitude="+str(minmag)+"&latitude="+str(lati)+"&longitude="+str(longi)+"&maxradiuskm="+str(radius), headers=headers)
    # conn.request("GET", "/fdsnws/event/1/query?format=csv&starttime=1900-01-01&endtime=2016-11-09&minmagnitude=3&latitude=37.784&longitude=-122.395&maxradiuskm=50", headers=headers)

    if Location.objects.get(name=name):
        print("No location exists!")

    res = conn.getresponse()
    data = res.read()

    # print(data.decode("utf-8"))
    parsed_data = (data.decode("utf-8")).split("\n")
    print(type(parsed_data))
    print(len(parsed_data))
    print(parsed_data[1])
    for x in range(1,len(parsed_data)-1):
        parsed_data_line = parsed_data[x].split(",")
        print(parsed_data_line[4])



make()
# idx = 1
# while idx < eqs.length
#   eq = Event.create({usgs_id:eqs[idx][11], northing:eqs[idx][1], easting:eqs[idx][2],
#                 depth:eqs[idx][3], magnitude:eqs[idx][4], date_time:eqs[idx][0]})
#   idx += 1
#
# c = Category(name="Test")
# c.save()
