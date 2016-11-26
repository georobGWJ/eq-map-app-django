from django.conf.urls import url
from eq_map import views

urlpatterns = [
    url(r'^earthquakes/$',
        views.EarthquakeList.as_view(),
        name=views.EarthquakeList.name),
    url(r'^earthquakes/(?P<pk>[0-9]+)/$',
        views.EarthquakeDetail.as_view(),
        name=views.EarthquakeDetail.name),

    url(r'^locations/$',
        views.LocationList.as_view(),
        name=views.LocationList.name),
    url(r'^locations/(?P<pk>[0-9]+)/$',
        views.LocationDetail.as_view(),
        name=views.LocationDetail.name),

    url(r'^user_earthquakes/$',
        views.UserEarthquakeList.as_view(),
        name=views.UserEarthquakeList.name),
    url(r'^user_earthquakes/(?P<pk>[0-9]+)/$',
        views.UserEarthquakeDetail.as_view(),
        name=views.UserEarthquakeDetail.name),

    url(r'^$',
        views.ApiRoot.as_view(),
        name=views.ApiRoot.name),
        
    url(r'^users/$',
        views.UserList.as_view(),
        name=views.UserList.name),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name=views.UserDetail.name),
]
