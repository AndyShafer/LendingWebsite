from django.conf.urls import url
from . import views

app_name = 'lending'

urlpatterns = [
        url(r'^$', views.home, name='home'),
        url(r'^(?P<user_id>[0-9]+)/$', views.show_user, name='show_user'),
	url(r'^register/$', views.UserFormView.as_view(), name='register'),
        url(r'^profile/(?P<profile_id>[0-9]+)/$', views.show_profile, name='show_profile'),
        url(r'^profile/edit/(?P<pk>[0-9]+)/$', views.UpdateProfile.as_view(), name='profile-edit'),
        url(r'^login/$', views.LoginFormView.as_view(), name='login'),
        url(r'^logout/$', views.log_out, name='logout'),
        url(r'^dashboard/$', views.dashboard, name='dashboard')
]
