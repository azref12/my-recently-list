from django.conf.urls import url
from rest_framework import routers
from movies import views
from movies import search_movies
from .views import *

router = routers.DefaultRouter()

urlpatterns = [

        url (r'movies/$', views.movies_list),
        url (r'movies_detail/(?P<pk>[0-9]+)$', views.movies_detail),
        url (r'movies_search/$', search_movies.Search_Movies),
]

urlpatterns += router.urls

