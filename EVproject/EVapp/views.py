#### ADD 수연 #####
import os
import json
####################


####### ADD 재웅 ######
import types

from .models import ElectricCarList

#####################

############# ADD 서영 ###############

from .models import Question, Answer, Comment
from django.utils import timezone
from .forms import NewQuestionForm, AnswerForm, CommentForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib.auth import authenticate, login
from EVapp.forms import UserForm
from django.contrib import messages
from django.db.models import Q, Count
#########################################

import pyautogui

from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect

from EVapp.models import User


def index(request):
    template = loader.get_template('EVapp/index.html')
    return HttpResponse(template.render(None, request))


def about(request):
    template = loader.get_template('EVapp/about.html')
    if request.method == 'POST':
        car_kind = request.POST.get('sel3')
        location = request.POST.get('sel1')

        #location_list = ['Seoul','Busan','Daegu','Incheon','Gwangju','Daejeon','Ulsan','Sejong','Gyeonggi','Kangwon','Chungbuk','Chungnam','Jeonbuk','Jeonnam','Gyeongbuk','Gyeongnam','Jeju']
        #location_money = [400,500,450,420,500,700,550,300,500,520,800,850,900,840,850,700,400]
        if location == 'Seoul':
            area_money = 400

        elif location == 'Busan':
            area_money = 500

        elif location == 'Daegu':
            area_money = 450

        elif location == 'Incheon':
            area_money = 420

        elif location == 'Gwangju':
            area_money = 500

        elif location == 'Daejeon':
            area_money = 700

        elif location == 'Ulsan':
            area_money = 550

        elif location == 'Sejong':
            area_money = 300

        elif location == 'Gyeonggi':
            area_money = 500

        elif location == 'Kangwon':
            area_money = 520

        elif location == 'Chungbuk':
            area_money = 800

        elif location == 'Chungnam':
            area_money = 850

        elif location == 'Jeonbuk':
            area_money = 900

        elif location == 'Jeonnam':
            area_money = 840

        elif location == 'Gyeongbuk':
            area_money = 850

        elif location == 'Gyeongnam':
            area_money = 700

        elif location == 'Jeju':
            area_money = 400

        if car_kind == 'A':
            country_money = 800

        elif car_kind == 'B':
            country_money = 690

        elif car_kind == 'C':
            country_money = 733

        elif car_kind == 'D':
            country_money = 701

        elif car_kind == 'E':
            country_money = 800

        elif car_kind == 'F':
            country_money = 780

        elif car_kind == 'G':
            country_money = 717

        elif car_kind == 'H':
            country_money = 750

        elif car_kind == 'I':
            country_money = 688

        elif car_kind == 'J':
            country_money = 722

        elif car_kind == 'K':
            country_money = 722

        elif car_kind == 'L':
            country_money = 722

        elif car_kind == 'M':
            country_money = 673

        elif car_kind == 'N':
            country_money = 673

        elif car_kind == 'O':
            country_money = 770

        elif car_kind == 'P':
            country_money = 770

        elif car_kind == 'Q':
            country_money = 649

        elif car_kind == 'R':
            country_money = 605

        elif car_kind == 'S':
            country_money = 605

        elif car_kind == 'T':
            country_money = 0

        elif car_kind == 'U':
            country_money = 684

        elif car_kind == 'V':
            country_money = 341

        elif car_kind == 'W':
            country_money = 329

        elif car_kind == 'X':
            country_money = 0

        elif car_kind == 'Y':
            country_money = 0

        elif car_kind == 'Z':
            country_money = 0

        elif car_kind == 'AA':
            country_money = 0

        elif car_kind == 'BB':
            country_money = 639

        area_state_money = (country_money / 800) * area_money
        area_state_money = int(area_state_money)

        total_money = country_money + area_state_money
        total_money = int(total_money)

        if country_money >= 400:
            price_coef = 100
        elif country_money >= 0:
            price_coef = 50
        else:
            price_coef = 0


        context = {'country_money': country_money,
                   'area_state_money': area_state_money,
                   'total_money': total_money,
                   'price_coef': price_coef}
        return HttpResponse(template.render(context, request))



    else:
        return HttpResponse(template.render(None,request))

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
"""
def car_details(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        name = request.POST.get('name')
        Car_Model = request.POST.get('Car_Model')
        # 여기에 address 추가
        user = User(email=email, name=name, pwd=pwd, Car_Model=Car_Model)
        if user.email and user.name and user.pwd and user.Car_Model != '':
            if user.email == User.objects.get(email=user.email).email:
                pyautogui.alert('중복되는 ID입니다.')
                return render(request, 'EVapp/car_details.html', None)
            else:
                user.save()
                return HttpResponseRedirect('http://localhost:8000/EVapp/contact/')  # 회원가입시 넘어가져야 할 페이지 로그인페이지

        else:
            pyautogui.alert('정보를 모두 기입해 주세요.')
    return render(request, 'EVapp/car_details.html', None)  # 회원가입 페이지
"""
"""
def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        try:
            exist_user = User.objects.get(email=email, pwd=pwd)
            print(exist_user.email)
            print(exist_user.pwd)
            return HttpResponseRedirect('http://localhost:8000/EVapp/')
        except:
            pyautogui.alert('존재하지 않는 ID 또는 비밀번호가 틀렸습니다.')
            return render(request, 'EVapp/contact.html/', None)

    return render(request, 'EVapp/contact.html')
"""


################## ADD 수연 ######################


def map(request):
 return render(request, 'EVapp/map.html', None)


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


def mapSearch(request):
 mapword = request.GET.get('mapword')
 mapselect = request.GET.get('mapselect')
 if mapword == '':
    mapword = mapselect
 context = {
     'mapword': mapword,
     'mapselect': mapselect,
 }
 return render(request, 'EVapp/mapSearch.html', context)

def purchase(request):
  return render(request, 'EVapp/purchase.html', None)

##############################################################


#################### ADD 서영 ################################

def question_list(request):
 page = request.GET.get('page', '1')
 kw = request.GET.get('kw', '')
 so = request.GET.get('so', 'recent')
 if so == 'recommend':
     question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_at')
 elif so == 'popular':
     question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_at')
 else:  # recent
     question_list = Question.objects.order_by('-create_at')
 if kw:
     question_list = question_list.filter(
         Q(subject__icontains=kw) |  # 제목검색
         Q(content__icontains=kw) |  # 내용검색
         Q(author__username__icontains=kw) |  # 질문 글쓴이검색
         Q(answer__author__username__icontains=kw)  # 답변 글쓴이검색
     ).distinct()
 paginator = Paginator(question_list, 10)
 page_obj = paginator.get_page(page)
 context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so' : so}
 return render(request, 'EVapp/question_list.html', context)

def question_detail(request, question_id):
 question = Question.objects.get(id=question_id)
 return render(request, 'EVapp/question_detail.html', {'question':question})

@login_required(login_url='login')
def question_create(request):
 if request.method == 'POST':
  form = NewQuestionForm(request.POST)
  if form.is_valid():
   question = form.save(commit=False)
   question.author = request.user
   question.create_at = timezone.now()
   question.save()
   return redirect('question_list')
 else:
  form = NewQuestionForm()
  return render(request, 'EVapp/question_create.html', {'form': form})

@login_required(login_url='login')
def answer_create(request, question_id):
 question = get_object_or_404(Question, pk=question_id)
 if request.method == 'POST':
  form = AnswerForm(request.POST)
  if form.is_valid():
   answer = form.save(commit=False)
   answer.author = request.user
   answer.question = question
   answer.create_at = timezone.now()
   answer.save()
   return redirect('{}#answer_{}'.format(
       resolve_url('question_detail', question_id=question.id), answer.id))
 else:
  form = AnswerForm()
 context = {'question': question, 'form': form}
 return render(request, 'EVapp/question_detail.html', context)


def signup(request):
 if request.method == "POST":
  form = UserForm(request.POST)
  if form.is_valid():
   form.save()
   username = form.cleaned_data.get('username')
   raw_password = form.cleaned_data.get('password1')
   user = authenticate(username=username, password=raw_password)
   login(request, user)
   return redirect('index')
 else:
  form = UserForm()
 return render(request, 'EVapp/signup.html', {'form': form})

@login_required(login_url='login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('question_detail', question_id=question.id)

    if request.method == "POST":
        form = NewQuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('question_detail', question_id=question.id)
    else:
        form = NewQuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'EVapp/question_create.html', context)

@login_required(login_url='login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('question_detail', question_id=question.id)
    question.delete()
    return redirect('index')

@login_required(login_url='login')
def answer_modify(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('question_detail', question_id=answer.question.id)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('{}#answer_{}'.format(
                resolve_url('question_detail', question_id=answer.question.id), answer.id))
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'EVapp/answer_modify.html', context)

@login_required(login_url='login')
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('question_detail', question_id=answer.question.id)
    answer.delete()
    return redirect('question_detail', question_id=answer.question.id)

@login_required(login_url='login')
def comment_create_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_at = timezone.now()
            comment.question = question
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('question_detail', question_id=comment.question.id), comment.id))
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'EVapp/comment_form.html', context)

@login_required(login_url='login')
def comment_modify_question(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('question_detail', question_id=comment.question.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('question_detail', question_id=comment.question.id), comment.id))
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'EVapp/comment_form.html', context)

@login_required(login_url='login')
def comment_delete_question(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('question_detail', question_id=comment.question.id)
    else:
        comment.delete()
    return redirect('question_detail', question_id=comment.question.id)

@login_required(login_url='login')
def vote_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        question.voter.add(request.user)
    return redirect('question_detail', question_id=question.id)

@login_required(login_url='login')
def vote_answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user == answer.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        answer.voter.add(request.user)
    return redirect('question_detail', question_id=answer.question.id)
