from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
import logging

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
    if request.method == 'POST':
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        name = request.POST.get('name')
        user = User(email=email, name=name, pwd=pwd)
        user.save()
        logging.warn("warn로그인 입니다.")
        return HttpResponseRedirect('http://localhost:8000/EVapp/contact/')  # 회원가입시 넘어가져야 할 페이지 로그인페이지
    return render(request, 'EVapp/car_details.html', None)  # 회원가입 페이지


def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')

        try:
            exist_user = User.objects.get(email=email, pwd=pwd)
            return HttpResponseRedirect(request,'http://localhost:8000/EVapp/')
        except:
            return render(request, 'EVapp/car_details.html/')

        finally:
            return render(request, 'EVapp/contact.html/')
    return render(request, 'EVapp/contact.html')




"""
def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        name = request.POST.get('name')
        user = User(email=email, name=name, pwd=pwd)
        user.save()
        return HttpResponseRedirect('http://localhost:8000/EVapp/signup/')
    return render(request, 'EVapp/signup.html', None)


def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')

        try:
            exist_user = User.objects.get(email=email, pwd=pwd)
            return render(request, 'EVapp/signin_success.html/')
        except:
            return render(request, 'EVapp/signin_fail.html/')

    return render(request, 'EVapp/signin.html')
"""