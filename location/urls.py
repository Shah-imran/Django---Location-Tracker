from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('login/', sign_in, name="sign_in"),
    path('signup/', sign_up, name="sign_up"),
]
