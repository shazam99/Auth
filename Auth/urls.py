
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html")),
    path('accounts/', include('allauth.urls')), #Django Allauth Library
    path('logout', LogoutView.as_view(),name='logout'), #Logout function
]
