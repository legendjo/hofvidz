from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .models import Hall

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

"""
1-get the Halls models
2-set the fields
3-template for the creat
4-If create is sucess, redirect to home page

"""
class CreateHall(generic.CreateView):
    model = Hall
    fields = ['title']
    template_name = 'halls/create_hall.html'
    success_url = reverse_lazy('home')
