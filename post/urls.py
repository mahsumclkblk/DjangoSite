from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^list/$',view=index,name='list'),
    url(r'^login/$',view=user_login,name='user_login'),
    url(r'^logout/$',view=user_logout,name='user_logout'),
    url(r'^user_profile_edit/$',view=user_profile_edit,name='user_profile_edit'),
    url(r'^user_register/$',view=user_register,name='user_register'),
    url(r'^update/(?P<id>[0-9]+)/$',view=changing,name='update'),
]
