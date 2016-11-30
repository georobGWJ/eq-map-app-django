from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions
from eq_map.models import Earthquake
from eq_map.models import Location
from eq_map.models import UserEarthquake
from eq_map.serializers import EarthquakeSerializer
from eq_map.serializers import LocationSerializer
from eq_map.serializers import UserEarthquakeSerializer
from eq_map.serializers import UserSerializer

# Create your views here.


class ApiEarthquakeList(generics.ListCreateAPIView):
    queryset = Earthquake.objects.all()
    serializer_class = EarthquakeSerializer
    name = 'api-earthquake-list'

class ApiEarthquakeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Earthquake.objects.all()
    serializer_class = EarthquakeSerializer
    name = 'api-earthquake-detail'

class ApiLocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    name = 'api-location-list'

class ApiLocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    name = 'api-location-detail'

class ApiUserEarthquakeList(generics.ListCreateAPIView):
    queryset = UserEarthquake.objects.all()
    serializer_class = UserEarthquakeSerializer
    name = 'api-user_earthquake-list'

class ApiUserEarthquakeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserEarthquake.objects.all()
    serializer_class = UserEarthquakeSerializer
    name = 'api-user_earthquake-detail'

class ApiUserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'api-user-list'

class ApiUserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'api-user-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'earthquakes': reverse(ApiEarthquakeList.name, request=request),
            'locations': reverse(ApiLocationList.name, request=request),
            'user_earthquakes': reverse(ApiUserEarthquakeList.name, request=request),
            'users': reverse(ApiUserList.name, request=request)
            })
