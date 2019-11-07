from django.contrib import admin
from django.urls import path, include

from main.views import IndexView, RemoveUrl, redirect_to_original_url




urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('user_control.urls')),
    path('', IndexView.as_view(), name='home'),
    path('remove_url/', RemoveUrl.as_view(), name='remove_url'),
    path('<str:url_code>/', redirect_to_original_url),
]
