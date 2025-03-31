from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', views.index, name='home'),
    path('new', views.new, name='page2'),
                  path('portfolio', views.portfolio, name='portfolio'),
                  path('map', views.map, name='map'),
                  path('gallery', views.gallery, name='gallery'),
                  path('blog', views.blog, name='blog'),

              ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)