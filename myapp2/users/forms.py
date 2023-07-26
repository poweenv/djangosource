from django import forms

# 장고에서 제공하는 User 생성폼과 모델 가져오기
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    """
    UserCreationForm 클래스를 상속받는 Form 정의
        |
    BaseUserCreationForm : username, password1, password2
    """

    # 부모가 넘겨주는 email은 필수 입력 요소가 아님
    # 필수 입력 요소로 만들기 위해 재정의
    email = forms.EmailField(label="email")

    class Meta:
        model = User
        #fields = "__all__" + 상속()
        fields = ["username","email"] # + 상속(password1,password2)