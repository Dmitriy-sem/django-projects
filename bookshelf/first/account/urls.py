from django.urls import path
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, LogoutView
from .views import *


urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', register, name='register'),

    path('password-reset/', Reset.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name="account/password_reset_done.html"),
         name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name="account/password_reset_confirm.html"), name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(
        template_name="account/password_reset_complete.html"), name='password_reset_complete'),

    path('cabinet/', cabinet, name='cabinet'),
    path('password-change/', change_password, name='password_change'),
]
