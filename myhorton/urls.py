from django.conf.urls import url, include
from . import views


urlpatterns = [
        url(r'^$', views.horton_index, name='horton_index'),    
        url(r'^calculation', views.horton_calculation, name='horton_calculation'),
    ]
