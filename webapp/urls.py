from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.webapp_index, name='webapp_index'),
    url(r'^select_ic', views.select_ic, name='select_ic'),
        ]
