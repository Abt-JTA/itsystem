from django.conf.urls import url
from wiki import views

urlpatterns = [
    url(r'^add_topic/$', views.add_topic, name='add_topic'),
    url(r'^edit_topic/(?P<t_slug>[\w-]+)/$', views.edit_topic, name='edit_topic'),
    url(r'^view_topic/(?P<t_slug>[\w-]+)/$', views.view_topic, name='view_topic'),
]