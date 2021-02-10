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
# path('signup/', views.signup, name='signup'),
# path('signin/',views.signin, name='signin'),

]