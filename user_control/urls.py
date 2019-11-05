from django.urls import path, include

from user_control.views import RegistrationView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('registration/', RegistrationView.as_view(), name='registration'),
]