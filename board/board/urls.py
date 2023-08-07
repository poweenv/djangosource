from django.urls import path
from .views.answer_views import (
    answer_delete,
    answer_edit,
    answer_create,
    vote_answer,
)
from .views.base_views import (
    index,
    question_detail,
   
)
from .views.comment_views import(
    comment_create_answer,
    comment_create_question,
    comment_edit_answer,
    comment_edit_question,
    comment_delete_answer,
    comment_delete_question,
)
from .views.question_views import(
    question_create,
    question_edit,
    question_delete,
    vote_question,
)

app_name = "board"

urlpatterns = [
    # http://127.0.0.1:8000/board
    path("", index, name="index"),
    # http://127.0.0.1:8000/board/1/ 상세조회
    path("<int:qid>/", question_detail, name="detail"),
    # http://127.0.0.1:8000/board/question/create/ 질문등록
    path("question/create/", question_create, name="question_create"),
    # http://127.0.0.1:8000/board/question/modify/1/ 질문등록
    path("question/modify/<int:qid>/", question_edit, name="question_modify"),
    path("question/create/", question_create, name="question_create"),
    # http://127.0.0.1:8000/board/question/delete
    path("question/delete/<int:qid>/", question_delete, name="question_delete"),
    # 답변
    # http://127.0.0.1:8000/board/answer/create/질문번호/
    path("answer/create/<int:qid>/", answer_create, name="answer_create"),
    path("answer/modify/<int:aid>/", answer_edit, name="answer_modify"),
    path("answer/delete/<int:aid>/", answer_delete, name="answer_delete"),
    # name에 들어가는게 html에 주는 url값이고 그 왼쪽에 있는 값이 views에서 쓰는값
    # 질문 댓글
    path(
        "comment/create/question/<int:qid>/",
        comment_create_question,
        name="comment_create_question",
    ),
    
    path(
        "comment/edit/question/<int:comment_id>/",
        comment_edit_question,
        name="comment_edit_question",
    ),
    
    
    path(
        "comment/delete/question/<int:comment_id>/",
        comment_delete_question,
        name="comment_delete_question",
    ),
    # 답변 댓글
    path(
        "comment/create/answer/<int:aid>/",
        comment_create_answer,
        name="comment_create_answer",
    ),
    
    # 답변 수정
    path(
        "comment/edit/answer/<int:comment_id>/",
        comment_edit_answer,
        name="comment_edit_answer",
    ),
    
    # 답변 삭제 
    path(
        "comment/delete/answer/<int:comment_id>/",
        comment_delete_answer,
        name="comment_delete_answer",
    ),
    # 추천 
    # 질문 추천
    path("vote/question/<int:qid>/",vote_question,name="vote_question"),
    path("vote/answer/<int:aid>/",vote_answer,name="vote_answer"),
]
