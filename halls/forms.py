from .models import Video
from django import forms

#ModelForm
# 1. https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/

# class VideoForm(forms.ModelForm):
#     class Meta:
#         model = Video
#         fields = ['title', 'url', 'youtube_id']
#         #Customization
#         labels = {'youtube_id':'YouTube ID'} # The word [ {labels} is a keyword]

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['url']
        #Customization
        labels = {'url':'YouTube Url'} # The word [ {labels} is a keyword]

#Non ModelForm
#https://docs.djangoproject.com/en/2.2/topics/forms/#the-form-class
#https://docs.djangoproject.com/en/2.2/topics/forms/#the-view
class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=255, label ='Search for Videos')
