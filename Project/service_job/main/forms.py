from django import forms
from .models import Reviews_about_service



class ReviewForm(forms.ModelForm):
    name = forms.CharField(required=True)
    surname = forms.CharField(required=True)
    title = forms.CharField(required=True)
    message = forms.CharField(required=True)

    class Meta:
        model = Reviews_about_service
        fields = [
            "name",
            "surname",
            "title",
            "message"
        ]
