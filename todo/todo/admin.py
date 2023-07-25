from django.contrib import admin
from .models import Todo
# admin에서 관리할 모델 정보 / admin 환경 설정
# admin 사용하기 위해서는 admin 계정 생성 필요
# python manage.py createsuperuser

# admin페이지에서 todo 모델 관리할 수 있는 기능 지정
admin.site.register(Todo)