
from django.conf.urls import url
from profiles.views import LoadProfileView, ProfileEditView

urlpatterns = [
    url(r'^edit/$', ProfileEditView.as_view(), name='profile_edit'),
    url(r'^(?P<username>\w{0,50})/$', LoadProfileView),
]
