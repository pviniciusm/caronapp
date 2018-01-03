from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Puser
import json

# Create your views here.
def homepage(request):
    users = Puser.objects.all()
    return render(request, 'users/homepage.html', {'users':users})

def signup(request):
    return render(request, 'users/signup.html', {})

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        city = request.POST.get('city')
        state = request.POST.get('state')

        response_data = {}

        
        if Puser.objects.filter(email=email).exists():
            response_data['error'] = 'user_already_exists'
        
            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )    
        new_puser = Puser(name=name, email=email, password=password, city=city, state=state)
        new_puser.save()

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return redirect('/signup', request=request)
