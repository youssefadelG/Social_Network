from django.shortcuts import render,redirect
from django.http import HttpResponse
from django .template import loader
from Social_Network.forms import RegistrationForm
from django.contrib.auth import logout

# Create your views here.

def home(request): # this is just a test make sure to try this path first to make sure that everyting is ok
    return render(request,'Social_Network/test.html')
##method = post means we are entering data in the forms,we are posting that data to the web server.
def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/anti-social/')
    else:
        form= RegistrationForm()

        args={'form':form}
        return render(request,'Social_Network/registration.html',args)

def logout_view(request):
    logout(request)
    return render(request,'Social_Network/logout.html')
