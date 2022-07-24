from django.forms import ModelForm
from .models import Recommend


class RecommendForm(ModelForm):
    class Meta:
        model = Recommend
        fields = ['song', 'text']
