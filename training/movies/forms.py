from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

from .models import Reviews, Raiting, RaitingStar


class ReviewForm(forms.ModelForm):
    """Форма отзыва"""
    captcha = ReCaptchaField()
    class Meta:
        model = Reviews
        fields = ("name", "email", "text")
        widgets = {
            "name": forms.TextInput(attrs={"class":"form-control border"}),
            "email": forms.EmailInput(attrs={"class":"form-control border"}),
            "text": forms.Textarea(attrs={"class":"form-control border"})
        }

class RatingForm(forms.ModelForm):
    """Форма добавления рейтинга"""
    star = forms.ModelChoiceField(
        queryset=RaitingStar.objects.all(), widget=forms.RadioSelect(), empty_label=True
    )

    class Meta:
        model = Raiting
        fields = ('star',)