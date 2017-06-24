from django import forms
from .models import *


class AddingForm(forms.ModelForm):

    class Meta:
        model = Trash_bin
        exclude = [""]


class SettingForm(forms.ModelForm):

    class Meta:
        model = Trash_bin
        exclude = [""]


class RegularForm(forms.ModelForm):

    class Meta:
        model = RegularTask
        exclude = [""]
