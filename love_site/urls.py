from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('main/', views.main_site, name='main'),
    path('memories/', views.memories, name='memories'),
    path('gallery/', views.gallery, name='gallery'),
    path('treasure/', views.treasure, name='treasure'),
    path('our-photos/', views.our_photos, name='our_photos'),
    path('secret/', views.secret, name='secret'),
]