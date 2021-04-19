from django.http import HttpResponseRedirect
from Mainapp.models import Todo
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

# Create your views here.


def home(request):
    todo_items = Todo.objects.filter(user=request.user).order_by("-date")
    # it will order by added date
    return render(request, 'to_do/index.html', {
        "todo_items": todo_items,
    })


@csrf_exempt
def add_todo(request):  # post method is used to get data  from index.html
    current_date = timezone.now()
    print(current_date)
    print(type(current_date))
    content = request.POST['content']
    created_obj = Todo.objects.create(user=request.user,
                                      title=content, details=content)  # creating object
    # returns no of element in database
    length_of_todos = Todo.objects.filter(user=request.user)
    return HttpResponseRedirect('/todo')


@csrf_exempt
def delete_todo(request, todo_id):
    Todo.objects.filter(user=request.user).get(title=todo_id).delete()
    return HttpResponseRedirect('/todo')
