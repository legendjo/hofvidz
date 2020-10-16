from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Hall, Video
from .forms import VideoForm, SearchForm
from django.forms import formset_factory

YOUTUBE_API_KEY ='AIzaSyBIKGPZFh9Puj8SuUShxrpwHxwTTwedUQU'

# Create your views here.
def home(request):
    return render(request, 'halls/home.html')

def dashboard(request):
    return render(request, 'halls/dashboard.html')

#ModelForm
#  https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/
def add_video(request, pk):                             #N:B- pk here refers to a hall id, the video will be addded to
    form = VideoForm()                                  #An empty form
    search_form = SearchForm()                          #Instantiate an empty SearchForm object

    if request.method == 'POST':
        #Create video
        form_filled = VideoForm(request.POST)
        if form_filled.is_valid():                 #validation begins
            video = Video()
            video.url = form_filled.cleaned_data['url']
            video.title = form_filled.cleaned_data['title']
            video.youtube_id = form_filled.cleaned_data['youtube_id']
            video.hall = Hall.objects.get(pk=pk)
            video.save()

    return render(request, 'halls/add_video.html', {'form':form, 'search_form':search_form})

'''
#SignUp:
It is important to use [registration] here its Djnago's registration keyword,
else if you use something differnt you will have to created a custome view for that to work
#Login a SignUp User After SignUp
1-Use form_valid
2-get the view
3-get username and password
4-authenticate user
5-login the user
return view'''

#Signup
class SignUp(generic.CreateView ):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'
    #Login a SignUp User After SignUp
    def form_valid(self, form):
        view = super(SignUp, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request,user)
        return view

'''
1-get the Halls models
2-set the fields
3-template for the creat
4-If create is sucess, redirect to home page
'''
class CreateHall(generic.CreateView):
    model = Hall
    fields = ['title']
    template_name = 'halls/create_hall.html'
    success_url = reverse_lazy('home')

    # user associated with creating a hall
    '''
    1-Use Djnago inbuilt form_valid as function name
    2-Get the user object
    3-Use super i.e the generic class of form_valid to validate
    4-Redirect home
    https://docs.djangoproject.com/en/2.2/topics/class-based-views/generic-editing/#basic-forms
    https://docs.djangoproject.com/en/2.2/ref/class-based-views/generic-editing/#createview
    '''
    def form_valid(self, form):
        form.instance.user = self.request.user
        super(CreateHall, self).form_valid(form)
        return redirect('dashboard') # we will later correct and redirect to a user' halls

# https://docs.djangoproject.com/en/2.2/ref/class-based-views/generic-editing/#formview

class DetailHall(generic.DetailView):
    model = Hall
    template_name = 'halls/detail_hall.html'

class UpdateHall(generic.UpdateView):
    model = Hall
    template_name = 'halls/update_hall.html'
    fields = ['title']
    success_url = reverse_lazy('dashboard')

class DeleteHall(generic.DeleteView):
    model = Hall
    template_name = 'halls/delete_hall.html'
    success_url = reverse_lazy('dashboard')
