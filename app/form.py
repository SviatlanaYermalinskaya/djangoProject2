from django import forms

from app.models import Img


class ImageForm(forms.ModelForm):
    class Meta:
        model = Img
        fields = ('img', 'name')
