from django.conf.urls import url
from . import views as publisher_views

urlpatterns = [
    url(r'^$', publisher_views.publisher, name='publisher'),
    url(r'^createApp/$', publisher_views.create_application, name="create-app")
]