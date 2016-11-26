from rest_framework import serializers
from eq_map.models import Earthquake

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
