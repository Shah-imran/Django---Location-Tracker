from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    # pages
    path('', home, name="home"),
    path('dashboard/', dashboard, name="dashboard"),
    path('change-password/', change_password, name="change_password"),

    # user authenticate
    path('login/', auth_views.LoginView.as_view(template_name='location/login.html'), name="sign_in"),
    path('signup/', sign_up, name="sign_up"),
    path('logout/', logout_user, name="logout_user"),

    # reset password
    path('reset-password/',
        auth_views.PasswordResetView.as_view(template_name="users/reset/password-reset.html"),
        name='reset_password'),
    path('password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name="users/reset/password_reset_done.html"),
        name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name="users/reset/password_reset_confirm.html"),
        name='password_reset_confirm'),
    path('password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name="users/reset/password_reset_complete.html"),
        name='password_reset_complete'),

]
