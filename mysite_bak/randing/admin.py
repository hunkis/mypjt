from django.contrib import admin
from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)

# Register your models here.
# #아래 두줄이 무엇을 의미하는지는 모델 배울실 때 나옵니다.
# python manage.py makemigrations
# python manage.py migrate

# #서버를 실행하는 커맨드 입니다
# python manage.py runserver