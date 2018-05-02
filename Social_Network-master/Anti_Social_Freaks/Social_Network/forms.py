#this is where i'll create our version of Django form #

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'password1',
                  'password2'
        )
        #i also need to define a function that allows the form to save the data to the model.
    def save(self, commit=True):
        user = super(RegistrationForm,self).save(commit = False)
        user.first_name = self.cleaned_data['first_name']
#cleaned_data--> makes sure that there is no SQL in the data and it's safe to save it.
        user.last_name = self.cleaned_data['last_name']


        if commit:
            user.save()

        return user
#now to use the form we replace in views.py the UserCreationForm to RegistrationForm