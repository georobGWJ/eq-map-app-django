from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, get_list_or_404
import http.client
import csv

class Earthquake(models.Model):
    usgs_id = models.CharField(max_length=100, unique=True)
    eq_lat = models.FloatField()
    eq_long = models.FloatField()
    depth = models.FloatField()
    mag = models.FloatField()
    eq_date = models.DateTimeField()
    location_id = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True, unique=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('mag',)

    # def __str__(self):
    #     return ('Mag: '+str(self.mag)+'\nDate: '+str(self.eq_date))

class Location(models.Model):
    name = models.CharField(max_length=120, unique=True)
    loc_lat = models.FloatField()
    loc_long = models.FloatField()
    radius = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True, unique=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ('Name: '+self.name+'\nRadius: '+self.radius)

class UserEarthquake(models.Model):
    user_id = models.ForeignKey('auth.User', related_name='user_earthquakes', on_delete=models.CASCADE)
    earthquake_id = models.ForeignKey(Earthquake, related_name='user_earthquakes', on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location, related_name='user_earthquakes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, unique=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ('User ID: '+self.user_id+'\nEQ ID:  '+self.earthquake_id+'\nLocation ID: '+self.location_id)

    # def make(starttime, endtime, minmag, lati, longi, radius, name):
    def make(name, lati, longi, minmag, radius, starttime, endtime, user_id):
        # CREATE Location object
        loc = Location.objects.create(name=name, loc_lat=lati, loc_long=longi, radius=radius)

        # CALL USGS TO GET ALL EARTHQUAKES
        conn = http.client.HTTPConnection("earthquake.usgs.gov")

        headers = { 'cache-control': "no-cache", }

        conn.request("GET", "/fdsnws/event/1/query?format=csv&starttime="+starttime+"&endtime="+endtime+"&minmagnitude="+str(minmag)+"&latitude="+str(lati)+"&longitude="+str(longi)+"&maxradiuskm="+str(radius), headers=headers)

        res = conn.getresponse()
        data = res.read()

        parsed_data = (data.decode("utf-8")).split("\n")

        for idx in range(1,len(parsed_data)-1):
            eq = parsed_data[idx].split(",")

            # Create Earthquake Object
            event = Earthquake.objects.create(usgs_id=eq[11], eq_lat=eq[1], eq_long=eq[2], depth=eq[3], mag=eq[4], eq_date=eq[0], location_id=loc.id)

            # Create UserEarthquake Object
            UserEarthquake.objects.create(user_id=user_id, earthquake_id=event, location_id=loc)
