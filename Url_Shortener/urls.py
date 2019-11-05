from django.contrib import admin
from django.contrib.auth import get_user_model, login
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.shortcuts import redirect, render
from django.urls import path, include
from django.views.generic import TemplateView, FormView

from main.views import IndexView, RemoveUrl, redirect_to_original_url

User = get_user_model()


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")
        field_classes = {'username': UsernameField}


class RegistrationView(FormView):
    form_class = RegistrationForm
    success_url = '/'
    template_name = 'registration/registration.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registration/', RegistrationView.as_view(), name='registration'),
    path('remove_url/', RemoveUrl.as_view(), name='remove_url'),
    path('<str:url_code>/', redirect_to_original_url),
]
