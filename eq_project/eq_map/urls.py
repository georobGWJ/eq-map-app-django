from django.conf.urls import url
from eq_map import views

urlpatterns = [
    url(r'^api/earthquakes/',
        views.ApiEarthquakeList.as_view(),
        name=views.ApiEarthquakeList.name),

    url(r'^api/earthquakes/(?P<pk>[0-9]+)/',
        views.ApiEarthquakeDetail.as_view(),
        name=views.ApiEarthquakeDetail.name),

    url(r'^api/locations/$',
        views.ApiLocationList.as_view(),
        name=views.ApiLocationList.name),

    url(r'^api/locations/(?P<pk>[0-9]+)/$',
        views.ApiLocationDetail.as_view(),
        name=views.ApiLocationDetail.name),

    url(r'^api/user_earthquakes/$',
        views.ApiUserEarthquakeList.as_view(),
        name=views.ApiUserEarthquakeList.name),

    url(r'^api/user_earthquakes/(?P<pk>[0-9]+)/$',
        views.ApiUserEarthquakeDetail.as_view(),
        name=views.ApiUserEarthquakeDetail.name),

    url(r'^api/users/$',
        views.ApiUserList.as_view(),
        name=views.ApiUserList.name),

    url(r'^api/users/(?P<pk>[0-9]+)/$',
        views.ApiUserDetail.as_view(),
        name=views.ApiUserDetail.name),

    url(r'^api/$',
        views.ApiRoot.as_view(),
        name=views.ApiRoot.name),
]
