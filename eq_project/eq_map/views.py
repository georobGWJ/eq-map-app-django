from django.contrib.auth.models import User
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
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'

class EarthquakeList(generics.ListCreateAPIView):
    queryset = Earthquake.objects.all()
    serializer_class = EarthquakeSerializer
    name = 'earthquake-list'

class EarthquakeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Earthquake.objects.all()
    serializer_class = EarthquakeSerializer
    name = 'earthquake-detail'

class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    name = 'location-list'

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    name = 'location-detail'

class UserEarthquakeList(generics.ListCreateAPIView):
    queryset = UserEarthquake.objects.all()
    serializer_class = UserEarthquakeSerializer
    name = 'user_earthquake-list'

class UserEarthquakeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserEarthquake.objects.all()
    serializer_class = UserEarthquakeSerializer
    name = 'user_earthquake-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    # renderer_classes = (TemplateHTMLRenderer,)

    # def get(self, request, *args, **kwargs):
    #     queryset = Earthquake.objects.all()
    #     self.object = self.get_object()
    #     return Response(request, template_name='index/index.html')

    def get(self, request, *args, **kwargs):
        # return Response(template_name='index/index.html')
        return Response({
            'earthquakes': reverse(EarthquakeList.name, request=request),
            'locations': reverse(LocationList.name, request=request),
            'user_earthquakes': reverse(UserEarthquakeList.name, request=request),
            'users': reverse(UserList.name, request=request),
            })
