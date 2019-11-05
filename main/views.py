from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django import forms
from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from main.models import Url


class RemoveUrl(LoginRequiredMixin, View):
    def post(self, request):
        url = request.POST.get('name')
        try:
            object = Url.objects.get(short_url=url)
        except Url.DoesNotExist:
            return HttpResponseBadRequest()
        if object.user != request.user:
            return HttpResponseBadRequest()
        object.delete()
        return redirect('home')


class IndexView(View):
    def get(self, request):
        urls = None
        if request.user.is_authenticated:
            urls = request.user.urls.values('original_url', 'short_url')
        return render(request, 'index.html', {'urls': urls,
                                              'site': settings.REDIRECT_DOMAIN if hasattr(settings, 'REDIRECT_DOMAIN') else request.get_host(),
                                              'protocol': 'https' if request.is_secure() else 'http'})


    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        url_validator = forms.URLField()
        source_original_url = request.POST.get('original_url')
        try:
            original_url = url_validator.clean(source_original_url)
        except ValidationError:
            error_msg = 'Введите корректный URL.'
            return render(request, 'index.html',
                          {'error_origin_url': error_msg, 'original_url_value': source_original_url})
        Url.objects.create(original_url=original_url, user=request.user)
        return redirect('home')


def redirect_to_original_url(request, url_code):
    try:
        url = Url.objects.get(short_url=url_code)
    except Url.DoesNotExist:
        return HttpResponseNotFound()
    return redirect(url.original_url)


