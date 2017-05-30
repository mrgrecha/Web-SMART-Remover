from django import forms
from .models import *


class AddingForm(forms.ModelForm):

    class Meta:
        model = Trash_bin
        exclude = [""]
