from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path ('admin/', admin.site.urls),
    url (r'^genre/', include('genre.urls')),
    url (r'^kdrama/', include('kdrama.urls')),
    url (r'^movies/', include('movies.urls')),
]