from django.conf.urls import url
from wiki import views

urlpatterns = [
    url(r'^add_topic/$', views.add_topic, name='add_topic'),
]