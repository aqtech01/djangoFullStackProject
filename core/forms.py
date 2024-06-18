from django import forms
from core.models import *


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ["tweet", "photo"]
