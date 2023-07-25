from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm


def todo_list(request):
    #    전체 목록 가져오기
    #    todos = Todo.objects.all()
    # 미완료된 목록 가져오기
    # where complete = 0
    todos = Todo.objects.filter(complete=False)
    return render(request, "todo/todo_list.html", {"todos": todos})


def todo_detail(request, id):
    # id와 일치하는 todo 조회 후 보내기
    todo = get_object_or_404(Todo, id=id)
    return render(request, "todo/todo_detail.html", {"todo": todo})


def todo_create(request):
    """
    get / post 둘다 동작

    """
    if request.method == "POST":
        form = TodoForm(request.POST)  # DTO 개념
        if form.is_valid():  # 유효성 검증(테이블 작성 기준)
            todo = form.save()  # db 반영
            return redirect("todo_detail", id=todo.id)
    else:
        # 화면단에서 사용 가능함
        form = TodoForm()

    return render(request, "todo/todo_create.html", {"form": form})


def todo_edit(request, id):
    """
    set complete=1
    """
    # 수정할 todo찾기
    todo = get_object_or_404(Todo, id=id)
    # todo = get_object_or_404(Todo,id=id)
    if request.method == "POST":
        form = TodoForm(request.POST, instnace=todo)
        if form.is_valid():
            todo = form.save()
            return redirect("todo_detail", id=todo.id)
    else:
        form = TodoForm(instance=todo)
    # 수정할 todo 값 변경
    return render(request, "todo/todo_edit.html", {"form": form})


def todo_done(request, id):
    # id와 일치하는 doto 찾기
    todo = Todo.objects.get(id=id)
    # post - 바인딩된 폼에 post 요청으로 넘어오는 값 담기
    todo.complete = True
    todo.save()
    # get - 찾은 todo를 폼에 바인딩 한 후 보내기
    return redirect("todo_list")


def done_list(request):
    dones = Todo.objects.filter(complete=True)
    return render(request, "todo/done_list.html", {"dones": dones})
