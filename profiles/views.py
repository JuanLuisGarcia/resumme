from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render

from core.models import Bio, ProviderProfile
from core.serializers import (serialize_user_provider_profiles,
                              serialize_profile)


def LoadProfileView(request, username):
    data = {}
    try:
        user = User.objects.get(username=username)
        data['profile'] = serialize_profile(
            Bio.objects.get(user=user)
        )

        data['courses'] = serialize_user_provider_profiles(
            ProviderProfile.objects.filter(user=user)
        )
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'profile.html', {'courses': data['courses'],
                                            'profile': data['profile']})