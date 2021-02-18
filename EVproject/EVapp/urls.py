from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
 path('', views.index, name='index'),
 path('about/', views.about, name='about'),
 path('blog/', views.blog, name='blog'),
 path('blog_details/', views.blog_details, name='blog_details'),
 path('car/', views.car, name='car'),
 #path('car_details/', views.car_details, name='car_details'),
 #path('contact/', views.contact, name='contact'),
 path('map/', views.map, name='map'),
 path('loadMapData/<int:id>', views.loadMapData),
 path('purchase/',views.purchase, name='purchase'),
 path('mapSearch',views.mapSearch, name= 'mapSearch'),
 path('question_list/', views.question_list, name='question_list'),
 path('board/<int:question_id>/', views.question_detail, name='question_detail'),
 path('board/question_create/', views.question_create, name='question_create'),
 path('board/answer_create/<int:question_id>/', views.answer_create, name='answer_create'),
#  또 수정
 path('login/', auth_views.LoginView.as_view(template_name='EVapp/login.html'), name='login'),
 path('logout/', auth_views.LogoutView.as_view(), name='logout'),
 path('signup/', views.signup, name='signup'),
 path('board/question_modify/<int:question_id>/', views.question_modify, name='question_modify'),
 path('board/question_delete/<int:question_id>/', views.question_delete, name='question_delete'),
 path('board/answer_modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
 path('board/answer_delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
 path('comment/create_question/<int:question_id>/', views.comment_create_question, name='comment_create_question'),
 path('comment/modify_question/<int:comment_id>/', views.comment_modify_question, name='comment_modify_question'),
 path('comment/delete_question/<int:comment_id>/', views.comment_delete_question, name='comment_delete_question'),
 path('vote_question/<int:question_id>/', views.vote_question, name='vote_question'),
 path('vote_answer/<int:answer_id>/', views.vote_answer, name='vote_answer'),
]



