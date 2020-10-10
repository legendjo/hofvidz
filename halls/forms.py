from .models import Video
from django import forms


# Doc https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/
class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'url', 'youtube_id']
