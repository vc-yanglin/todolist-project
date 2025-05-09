from django.shortcuts import render
from .models import Todo


# Create your views here.
def todolist(request):
    todos = Todo.objects.all()
    print(todos)
    result = {"todos": todos}
    return render(request, "todo/todolist.html", result)


def viewtodo(request, id):
    todo = None
    try:
        todo = Todo.objects.get(id=id)
    except Exception as e:
        print(e)

    return render(request, "todo/viewtodo.html", {"todo": todo})
