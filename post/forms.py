from django import forms
from . import models


class Form_for_bookshow(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = "__all__"

        # Второй способ для частичного ввода
        # fields = [
        #     "title",
        #     "description",
        #     "genre",
        #
        # ]