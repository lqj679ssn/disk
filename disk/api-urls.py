# from django.conf.urls import url, include
from django.urls import path, include

urlpatterns = [
    path('user/', include('User.urls')),
    path('res/', include('Resource.urls')),
]