from rest_framework import serializers
from eq_map.models import Earthquake
from eq_map.models import Location
from eq_map.models import UserEarthquake
from django.contrib.auth.models import User
import eq_map.views

class EarthquakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Earthquake
        fields = ('id', 'usgs_id', 'eq_lat', 'eq_long', 'depth', 'mag', 'eq_date')

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('name', 'loc_lat', 'loc_long', 'radius')

class UserEarthquakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEarthquake
        fields = ('user_id', 'earthquake_id', 'location_id')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    games = UserEarthquakeSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('url', 'pk', 'username', 'user_earthquakes')
