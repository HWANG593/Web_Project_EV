from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('about/', views.about, name='about'),
 path('blog/', views.blog, name='blog'),
 path('blog_details/', views.blog_details, name='blog_details'),
 path('car/', views.car, name='car'),
 path('car_details/', views.car_details, name='car_details'),
 path('contact/', views.contact, name='contact'),
 path('map/', views.map, name='map'),
 path('loadMapData/<int:id>', views.loadMapData),
 path('question_list/', views.question_list, name='question_list'),
 path('board/<int:question_id>/', views.question_detail, name='question_detail'),
 path('board/question_create/', views.question_create, name='question_create'),
 path('board/answer_create/<int:question_id>/', views.answer_create, name='answer_create'),
 path('login/', views.login, name='login'),
 path('signup/', views.signup, name='signup'),
 path('logout/', views.logout, name='logout'),
]



