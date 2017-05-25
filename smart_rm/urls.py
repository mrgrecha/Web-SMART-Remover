from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^delete$', views.delete, name='delete'),
    url(r'^tasks$', views.tasks, name='tasks'),
    url(r'^show$', views.show, name='show'),
    url(r'^history', views.history, name='history'),
    url(r'^add$', views.add, name='add'),
    url(r'^settings$', views.settings, name='settings'),
    url(r'^logs$', views.logs, name='logs'),
]