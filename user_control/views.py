from django.contrib.auth import get_user_model, login
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.shortcuts import render
from django.views.generic import FormView

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