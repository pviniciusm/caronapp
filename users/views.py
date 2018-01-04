from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Puser
from .forms import PuserForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout

import json
import datetime

# Create your views here.
def homepage(request):
    if not request.user.is_authenticated:
        return render(request, 'users/homepage.html', {})
    else:
        return render(request, 'users/index.html', {'user':request.user})


def log_out(request):
    if not request.user.is_authenticated:
        return redirect('/', request=request)
    else:
        logout(request)
        return redirect('/', request=request)



def log_in(request):
    username = request.POST['login-email']
    password = request.POST['login-pass']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/', request=request)
    else:
        return redirect('/signup', request=request)



def signup(request):
    if request.user.is_authenticated:
        return redirect('/', request=request)

    form = PuserForm
    return render(request, 'users/signup.html', {'form':form})

def register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password = make_password(password=password, salt=None, hasher='default')

        bday_day = request.POST.get('bdayday')
        bday_month = request.POST.get('bdaymonth')
        bday_year = request.POST.get('bdayyear')

        city = request.POST.get('city')
        state = request.POST.get('state')

        bday = "%s-%s-%s" % (bday_year, bday_month, bday_day)

        response_data = {}

        
        if Puser.objects.filter(email=email).exists():
            response_data['error'] = 'user_already_exists'
        
            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )    
        new_puser = Puser(first_name=fname, last_name=lname, email=email, username=email, password=password, birthday=bday, city=city, state=state)
        new_puser.save()

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return redirect('/signup', request=request)
