from django.shortcuts import redirect

#it will just to redirect to the login page
def login_redirect( request ):
    return (redirect("/anti-social/login"))

