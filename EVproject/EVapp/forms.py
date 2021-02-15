from django import forms
from .models import Question, Answer

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