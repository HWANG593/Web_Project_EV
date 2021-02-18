from django.contrib import admin

# 수정
from .models import Question

admin.site.register(Question)