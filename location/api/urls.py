from django.urls import path
from .views import *
from rest_framework.authtoken import views as auth_views


urlpatterns = [
    path('locations/', location_list, name="location_list"),
    
    # auth
    path('auth/', auth_views.obtain_auth_token, name="obtain_auth_token"),
]
