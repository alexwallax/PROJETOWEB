from django.shortcuts import render

# listar as tarefas cadastradas
def todo_list(request):
    nome = "Alex"
    return render(request, "todos/todo_list.html", {"nome": nome})
