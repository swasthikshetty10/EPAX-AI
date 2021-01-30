from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.http import HttpResponseRedirect
from to_do import database
# Create your views here.
def home(request):
    todo_items = database.list_tasks(request.user.id)
    return render(request, 'to_do/index.html', {
        "todo_items": todo_items,
    })


@csrf_exempt
def add_todo(request):  # post method is used to get data  from index.html
    usrid = request.user.id
    content = request.POST['content']
    # created_obj = Todo.objects.create(added_date=current_date, text=content)  # creating object
    # length_of_todos = Todo.objects.all().count()  # returns no of element in database
    database.add_task(id_=usrid , task = content)
    return HttpResponseRedirect('/todo')


@csrf_exempt
def delete_todo(request, todo_id):
    database.del_task(request.user.id , todo_id)
    return HttpResponseRedirect('/todo')
