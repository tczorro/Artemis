from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^upload/', views.handle_file, name='upload'),
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.user_login, name='login'),
    url(r'^logout/', views.user_logout, name='logout'),
]
