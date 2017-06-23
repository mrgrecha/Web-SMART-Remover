from django.conf.urls import url
from . import views
from django.contrib import admin


admin.autodiscover()

urlpatterns = [
    url(r'^$', views.delete, name='delete'),
    url(r'^delete/$', views.delete, name='delete'),
    url(r'^tasks/$', views.tasks, name='tasks'),
    url(r'^show/$', views.show, name='show'),
    url(r'^show/trashBin/(?P<pk>\w+)/recover_from_trash$', views.recover, name='recover'),
    url(r'^show/trashBin/(?P<pk>\w+)/remove_from_trash$', views.remove_from_trash, name='remove'),
    url(r'^show/trashBin/(?P<pk>\w+)/$', views.show_trash, name='show'),
    url(r'^history/$', views.history, name='history'),
    url(r'^regex/', views.RegularCreate.as_view(), name='regular'),
    url(r'^settings/$', views.settings_without_bin, name='settings'),
    url(r'^settings/trashBin/(?P<pk>\w+)/$', views.TrashBinUpdate.as_view(), name='settings'),
    url(r'^remove/(?P<pk>\w+)/$', views.TrashBinDelete.as_view(), name='remove'),
    url(r'^add/$', views.TrashBinCreate.as_view(), name='add'),
    url(r'^logs/$', views.logs, name='logs'),
    url(r'get_info', views.get_info_for_file_system),
    url(r'^success/$', views.success),
    url(r'delete/add_task', views.add_task, name='adding_task'),
    url(r'tasks/execute_task', views.execute_task, name='executing_task'),
    url(r'tasks/delete_task', views.delete_task, name='deleting_task'),
    url(r'tasks/execute_regular_task', views.execute_regular_task, name='executing_regular_task'),
    url(r'tasks/delete_regular_task', views.delete_regular_task, name='deleting_regular_task'),
]


#    url(r'^remove/(?P<pk>\w+)/$', views.TrashBinDelete.as_view(), name='deleting'),