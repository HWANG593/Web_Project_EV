from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect

from EVapp.models import User


def index(request):
 template = loader.get_template('EVapp/index.html')
 return HttpResponse(template.render(None, request))

def about(request):
 template = loader.get_template('EVapp/about.html')
 return HttpResponse(template.render(None, request))

def blog(request):
 template = loader.get_template('EVapp/blog.html')
 return HttpResponse(template.render(None, request))

def blog_details(request):
 template = loader.get_template('EVapp/blog_details.html')
 return HttpResponse(template.render(None, request))

def car(request):
 template = loader.get_template('EVapp/car.html')
 return HttpResponse(template.render(None, request))

def car_details(request):
 template = loader.get_template('EVapp/car_details.html')
 return HttpResponse(template.render(None, request))

def contact(request):
 template = loader.get_template('EVapp/contact.html')
 return HttpResponse(template.render(None, request))

def signup(request):
 if request.method == 'POST':
  email = request.POST.get('email')
  pwd = request.POST.get('pwd')
  name = request.POST.get('name')
  user = User(email=email, name=name, pwd=pwd)
  user.save()
  return HttpResponseRedirect('EVapp/signup.html')
 return render(request,'EVapp/signup.html',None)