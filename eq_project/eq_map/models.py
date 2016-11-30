from django.db import models
from django.contrib.auth.models import User

class Earthquake(models.Model):
    usgs_id = models.CharField(max_length=100, unique=True)
    eq_lat = models.FloatField()
    eq_long = models.FloatField()
    depth = models.FloatField()
    mag = models.FloatField()
    eq_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True, unique=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('mag',)

    def __str__(self):
        return ('Mag: '+self.mag+'\nDate: '+self.eq_date)

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
