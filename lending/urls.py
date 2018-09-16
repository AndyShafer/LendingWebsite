from django.conf.urls import url
from . import views

app_name = 'lending'

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^(?P<user_id>[0-9]+)/$', views.show_user, name='show_user'),
        url(r'^register/$', views.UserFormView.as_view(), name='register')
]
