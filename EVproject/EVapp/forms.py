from django import forms
from .models import Question, Answer, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewQuestionForm(forms.ModelForm):
    subject = forms.CharField(
        max_length=200,
        label='제목')
    content = forms.CharField(
        widget=forms.Textarea(),
        label='내용'
    )

    class Meta:
        model = Question
        fields = ['subject', 'content']


class AnswerForm(forms.ModelForm):
    content = forms.Textarea()

    class Meta:
        model = Answer
        fields = ['content',]

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "email")

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }