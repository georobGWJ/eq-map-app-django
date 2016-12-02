from django.contrib.auth.models import User
from django.contrib.auth import get_user
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
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



# =================== API VIEWS ===================
# =================================================

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

# =================== HTML VIEWS ====================
# ===================================================

# Get main index page
def get_base(request):
    return render(request, template_name='base.html')

# Get Data Management tab
def get_data_tab(request):
    return render(request, template_name='user_earthquakes/new.html')

# Get Earthquake Map tab
def get_earthquake_tab(request):
    queryset = Location.objects.order_by('-created_at')
    context = {'locations': queryset}
    return render(request=request, context=context, template_name='earthquakes/index.html')

# Get EQ Visualization tab
def get_viz_tab(request):
    return render(request, template_name='user_earthquakes/index.html')

# Post EQ Catalog form data
@csrf_exempt
def create_catalog(request):
    user = get_user(request)
    if request.method == 'POST':
        name = request.POST.get('name')
        lati = request.POST.get('lati')
        longi = request.POST.get('longi')
        radius = request.POST.get('radius')
        starttime = request.POST.get('starttime')
        endtime = request.POST.get('endtime')
        minmag = request.POST.get('minmag')

    UserEarthquake.make(name, lati, longi, minmag, radius, starttime, endtime, user)
    return redirect('map_tab')
    # return render(request, template_name='users/show.html')


# def get_data(request):
#     return render(request, template_name='')
#
#
# def get_data(request):
#     return render(request, template_name='')
#
#
# def get_data(request):
#     return render(request, template_name='')
#
#
# def get_data(request):
#     return render(request, template_name='')
