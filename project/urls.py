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
    path('pdf/', views.pdf, name='pdf'),
    path('about/', views.about, name='project-about'),
    path('tips/', views.tips, name='project-tips'),
    path('examples/', views.examples, name='project-examples'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),

]
