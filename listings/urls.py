from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='index'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('cars/', views.car, name='cars'),
    path('contact/', views.contact, name='contact'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
