from django.contrib import admin
from .models import Question,Answer,Comment

class QuestionAdmin(admin.ModelAdmin):
    # admin페이지에서 선택한 걸 보여줌
    list_display = ("subject","created_at")
    # 검색 할때 어떤걸 기준으로 할지 결정
    search_fields =["subject"]

admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Comment)
