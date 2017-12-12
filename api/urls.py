from django.conf.urls import url
from api.views import UserProfileData

urlpatterns = [
    url(r'^profile/(?P<username>\w{0,50})/$', UserProfileData),
]
