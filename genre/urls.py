from django.conf.urls import url
from rest_framework import routers
from genre import views
from genre import search_genre
from .views import *

router = routers.DefaultRouter()

urlpatterns = [

        url (r'genre/$', views.genre_list),
        url (r'genre_detail/(?P<pk>[0-9]+)$', views.genre_detail),
        url (r'genre_search/$', search_genre.Search_Genre),
]

urlpatterns += router.urls

