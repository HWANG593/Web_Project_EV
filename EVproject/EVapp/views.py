#### ADD 수연 #####
import os
import json
####################


####### ADD 재웅 ######
from .models import ElectricCarList

#####################

############# ADD 서영 ###############

from .models import Question
from django.utils import timezone
from .forms import NewQuestionForm
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
#########################################

from tkinter import messagebox

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

################## ADD 재웅 ##############################
def car(request):
    template = loader.get_template('EVapp/car.html')
    car_1 = ElectricCarList.objects.get(number=1)
    car_2 = ElectricCarList.objects.get(number=2)
    car_3 = ElectricCarList.objects.get(number=3)
    car_4 = ElectricCarList.objects.get(number=4)
    car_5 = ElectricCarList.objects.get(number=5)
    car_6 = ElectricCarList.objects.get(number=6)
    car_7 = ElectricCarList.objects.get(number=7)
    car_8 = ElectricCarList.objects.get(number=8)
    car_9 = ElectricCarList.objects.get(number=9)
    context = {"car_1": car_1, "car_2": car_2, "car_3": car_3, "car_4": car_4, "car_5": car_5, "car_6": car_6, "car_7": car_7, "car_8": car_8, "car_9": car_9}
    return HttpResponse(template.render(context, request))
###################################################################

def car_details(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        name = request.POST.get('name')
        Car_Model = request.POST.get('Car_Model')
        user = User(email=email, name=name, pwd=pwd, Car_Model=Car_Model)
        user.save()
        return HttpResponseRedirect('http://localhost:8000/EVapp/contact/')  # 회원가입시 넘어가져야 할 페이지 로그인페이지
    return render(request, 'EVapp/car_details.html', None)  # 회원가입 페이지


def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        try:
            exist_user = User.objects.get(email=email, pwd=pwd)

            return HttpResponseRedirect('http://localhost:8000/EVapp/car/')
        except:
            #messagebox.showinfo('알림창','존재하지 않는 ID입니다.')
            return render(request, 'EVapp/contact.html/', None)

    return render(request, 'EVapp/contact.html')



################## ADD 수연 ######################


def map(request):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + '/' + 'EVdata.json', encoding='utf-8') as json_file:
        attractions = json.load(json_file)['records']
        attractiondict = []
        for attraction in attractions:
            content = {
                "title": attraction['충전소명'],
                "mapx": attraction['경도'],
                "mapy": attraction['위도'],
                "addr": str(attraction['충전소위치상세']),
                "fee": attraction['주차료부과여부'],
                "starttime": str(attraction['이용가능시작시각']),
                "endtime": str(attraction['이용가능종료시각']),
                "slowYN": attraction['완속충전가능여부'],
                "fastYN": attraction['급속충전가능여부'],
            }
            if attraction.get('급속충전타입구분'):
                content['fasttype'] = str(attraction['급속충전타입구분'])
            else:
                content['fasttype'] = ''
            attractiondict.append(content)
        attractionJson = json.dumps(attractiondict, ensure_ascii=False)
    return render(request, 'EVapp/map.html', {'attractionJson': attractionJson})


def loadMapData(request, id):
    global n
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + '/' + 'EVdata.json', encoding='utf-8') as json_file:
        attractions = json.load(json_file)['records']
        attractiondict = []
        for attraction in attractions:
            if id == 0:
                content = {
                    "title": attraction['충전소명'],
                    "mapx": attraction['경도'],
                    "mapy": attraction['위도'],
                    "addr": str(attraction['충전소위치상세']),
                    "fee": attraction['주차료부과여부'],
                    "starttime": str(attraction['이용가능시작시각']),
                    "endtime": str(attraction['이용가능종료시각']),
                    "slowYN": attraction['완속충전가능여부'],
                    "fastYN": attraction['급속충전가능여부'],
                }
                if attraction.get('급속충전타입구분'):
                    content['fasttype'] = str(attraction['급속충전타입구분'])
                else:
                    content['fasttype'] = ''
                attractiondict.append(content)

            if id == 1:
                if attraction['주차료부과여부'] == "N":
                    content = {
                        "title": attraction['충전소명'],
                        "mapx": attraction['경도'],
                        "mapy": attraction['위도'],
                        "addr": str(attraction['충전소위치상세']),
                        "fee": attraction['주차료부과여부'],
                        "starttime": str(attraction['이용가능시작시각']),
                        "endtime": str(attraction['이용가능종료시각']),
                        "slowYN": attraction['완속충전가능여부'],
                        "fastYN": attraction['급속충전가능여부'],
                    }
                    if attraction.get('급속충전타입구분'):
                        content['fasttype'] = str(attraction['급속충전타입구분'])
                    else:
                        content['fasttype'] = ''
                    attractiondict.append(content)

            if id == 2:
                if attraction['급속충전가능여부'] == "Y":
                    content = {
                        "title": attraction['충전소명'],
                        "mapx": attraction['경도'],
                        "mapy": attraction['위도'],
                        "addr": str(attraction['충전소위치상세']),
                        "fee": attraction['주차료부과여부'],
                        "starttime": str(attraction['이용가능시작시각']),
                        "endtime": str(attraction['이용가능종료시각']),
                        "slowYN": attraction['완속충전가능여부'],
                        "fastYN": attraction['급속충전가능여부'],
                    }
                    if attraction.get('급속충전타입구분'):
                        content['fasttype'] = str(attraction['급속충전타입구분'])
                    else:
                        content['fasttype'] = ''
                    attractiondict.append(content)

        attractionJson = json.dumps(attractiondict, ensure_ascii=False)
    return HttpResponse(attractionJson, content_type="application/json")
##############################################################


#################### ADD 서영 ################################

def question_list(request):
 page = request.GET.get('page', '1')
 question_list = Question.objects.order_by('-create_at')
 paginator = Paginator(question_list, 10)
 page_obj = paginator.get_page(page)
 # template = loader.get_template('EVapp/question_list.html')
 # return HttpResponse(template.render(None, request))
 return render(request, 'EVapp/question_list.html', {'question_list':page_obj})

def question_detail(request, question_id):
 # question = get_object_or_404(Question,id=question_id)
 question = Question.objects.get(id=question_id)
 return render(request, 'EVapp/question_detail.html', {'question':question})

# @login_required(login_url='common:login')
def question_create(request):
 if request.method == 'POST':
  form = NewQuestionForm(request.POST)
  if form.is_valid():
   question = form.save(commit=False)
   # question.author = request.user
   question.create_at = timezone.now()
   question.save()
   return redirect('question_list')
 else:
  form = NewQuestionForm()
  return render(request, 'EVapp/question_create.html', {'form': form})

# @login_required(login_url='common:login')
def answer_create(request, question_id):
 question = get_object_or_404(Question, pk=question_id)
 question.answer_set.create(content=request.POST.get('content'), create_at=timezone.now())
 return redirect('question_detail', question_id=question_id)
 # if request.method == 'POST':
 #  form = AnswerForm(request.POST)
 #  if form.is_valid():
 #   answer = form.save(commit=False)
 #   answer.author = request.user
 #   answer.question = question
 #   answer.create_at = timezone.now()
 #   answer.save()
 #   return redirect('question_detail', question_id=question_id)
 # else:
 #  form = AnswerForm()
 # context = {'question': question, 'form': form}
 # return render(request, 'EVapp/question_detail.html', context)