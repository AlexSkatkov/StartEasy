from django.urls import path
from . import views
# when a user enters the url we send him to the suitable view
urlpatterns = [
    path('', views.home, name='project-home'),
    path('success/', views.home, name='success'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('help/', views.help, name='help'),
    path('about/', views.about, name='project-about')

]
