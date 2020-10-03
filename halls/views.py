from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'halls/home.html')


class SignUp(generic.CreateView ):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    '''It is important to use [registration] here its Djnago's registration keyword,
        else if you use something differnt you will have to created a custome view for that to work
    '''
    template_name = 'registration/signup.html'
