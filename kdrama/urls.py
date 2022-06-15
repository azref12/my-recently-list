from django.conf.urls import url
from rest_framework import routers
from kdrama import views
from kdrama import search_kdrama
from .views import *

router = routers.DefaultRouter()

urlpatterns = [

        url (r'kdrama/$', views.kdrama_list),
        url (r'kdrama_detail/(?P<pk>[0-9]+)$', views.kdrama_detail),
        url (r'kdrama_search/$', search_kdrama.Search_Kdrama),
]

urlpatterns += router.urls

