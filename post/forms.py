from django import forms
from . import models


class Form_for_marketplase(forms.ModelForm):
    class Meta:
        model = models.Marketplace
        fields = "__all__"
