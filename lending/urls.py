from django.conf.urls import url
from . import views

app_name = 'lending'

urlpatterns = [
        url(r'^$', views.home, name='home'),
        url(r'^(?P<user_id>[0-9]+)/$', views.show_user, name='show_user'),
	url(r'^register/$', views.UserFormView.as_view(), name='register'),
        url(r'^profile/(?P<profile_id>[0-9]+)/$', views.show_profile, name='show_profile'),
        url(r'^requests/$', views.show_requests, name='show-requests'),
        url(r'^requests/accept/(?P<request_id>[0-9]+)/$', views.accept_request, name='accept-request'),
        url(r'^contracts/$', views.show_contracts, name='show-contracts'),
        url(r'^profile/edit/(?P<pk>[0-9]+)/$', views.UpdateProfile.as_view(), name='profile-edit'),
        url(r'^login/$', views.LoginFormView.as_view(), name='login'),
        url(r'^logout/$', views.log_out, name='logout'),
        url(r'^dashboard/$', views.dashboard, name='dashboard'),
        url(r'^add-object/$', views.CreateObject.as_view(), name='create-object'),
        url(r'^objects/(?P<user_id>[0-9]+)/$', views.show_objects, name='show-objects'),
        url(r'^delete-object/(?P<pk>[0-9]+)/$', views.DeleteObject.as_view(), name='delete-object'),
        url(r'^update-object/(?P<pk>[0-9]+)/$', views.UpdateObject.as_view(), name='update-object'),
        url(r'^create-request/(?P<object_id>[0-9]+)/$', views.CreateRequestView.as_view(), name='create-request'),
]
