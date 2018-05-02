from django .urls import path
from . import views
from django.contrib.auth.views import login,logout



# all add your needed urls here
urlpatterns = [
    path('',views.home , name='home') ,# this is just a test make sure to try this path first to make sure that everyting is ok
    path('login/', login,{'template_name': 'Social_Network/login.html'}),
    path('logout/', logout, {'template_name': 'Social_Network/logout.html'}),
    path('register/',views.register,name='register')
]