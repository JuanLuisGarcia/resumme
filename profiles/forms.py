# -*- coding: utf-8 -*-

from django import forms

from core.models import ProviderProfile, Bio


class BioEditForm(forms.ModelForm):

    class Meta:
        model = Bio
        exclude = ('user',)


class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = ProviderProfile
        fields = ('username_provider',)
