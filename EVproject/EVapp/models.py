from django.db import models
from django.contrib.auth.models import User

# class User(models.Model):
#     email = models.CharField(max_length=50)
#     pwd = models.CharField(max_length=100)
#     name = models.CharField(max_length=10)
#     Car_Model = models.CharField(max_length=30)



##### ADD 재웅 ############

class ElectricCarList(models.Model) :
    number = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=30, null=True)
    subname = models.CharField(max_length=30, null=True)
    chargetype = models.CharField(max_length=30, null=True)
    onedistance = models.IntegerField(null=True)
    battery = models.IntegerField(null=True)
    fastcharge = models.CharField(max_length=30, null=True)
    slowcharge = models.CharField(max_length=30, null=True)
    rank = models.IntegerField(null=True)
    price = models.CharField(max_length=30, null=True)

######################################


############ ADD 서영 #################

class Question(models.Model):
    # 또 수정
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=100)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')

    def __str__(self):
        return self.subject

class Answer(models.Model):
    # 또 수정
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')


    # def __str__(self):
    #     return self.content


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_at = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
###############################################