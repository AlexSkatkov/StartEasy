from django.urls import path
from . import views
# when a user enters the url we send him to the suitable view
urlpatterns = [
    path('', views.home, name='project-home'),
    path('success/', views.home, name='success'),


]
