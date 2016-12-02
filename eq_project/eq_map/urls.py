from django.conf.urls import url
from eq_map import views

urlpatterns = [
    # =================== API ROUTES ===================
    # ==================================================
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

    # =================== HTML ROUTES ===================
    # ===================================================

    url(r'^$', views.get_base, name='base'),

    url(r'^earthquakes/$', views.get_earthquake_tab, name='map_tab'),


    url(r'^user_earthquakes/$', views.get_viz_tab, name='viz_tab'),

    url(r'^user_earthquakes/new/$', views.get_data_tab, name='data_tab'),

    url(r'^user_earthquakes/post/$', views.create_catalog, name='create_catalog'),

    url(r'^locations/$', views.get_all_eqs, name='get_all_eqs'),

    url(r'^locations/(?P<pk>[0-9]+)/$', views.get_catalog_eqs, name='get_loc_eqs'),

    url(r'^user_earthquakes/post/$', views.create_catalog, name='create_catalog'),

    # url(r'^earthquakes/show/$', views.show_catalog, name='show_catalog'),
    #
    # url(r'^$', views.get_data_tab, name='data_tab'),
    #
    # url(r'^$', views.get_data_tab, name='data_tab'),




]
