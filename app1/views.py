from django.http import HttpResponse
from django.shortcuts import redirect, render

from app1.models import TodoList

# Create your views here.
def home(request):
    people = [
        {
            "name" : "Bikram Shrestha",
            "age" : 23,
            "address" : "Bhaktapur"
        },
        {
            "name" : "Suprem Giri",
            "age" : 20,
            "address" : "Kathmandu"
        },
        {
            "name" : "Kabigya Adhikari",
            "age" : 21,
            "address" : "Chitwan"
        }
    ]
    context ={
        "title" : "Home Page",
        "heading" : "Welcome to Home Page.",
        "content" : "This is the content of the home page.",
        "people" : people       
    }
    return render(request, 'home.html', context)

def aboutus(request):
    return HttpResponse("This is a aboutus page.")

def contactus(request):
    return HttpResponse("Contact Us at: 9841234567")

def todolist(request):
    queryset = TodoList.objects.all()
    completed = TodoList.objects.filter(is_completed = True).count()
    incomplete = TodoList.objects.filter(is_completed = False).count()
    context = {
        'tasks': queryset,
        'completed': completed,
        'incomplete': incomplete
    }
    return render(request, 'todolist.html', context)

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        TodoList.objects.create(title = title, description = description)
        return redirect('/todolist/')
    return render(request, 'create.html')

def mark_complete(request, id):
    task = TodoList.objects.get(id = id)
    if task.is_completed == False:
        task.is_completed = True
        task.save()
    else:
        task.is_completed = False
        task.save()
    return redirect('/todolist/')

def edit(request, id):
    task = TodoList.objects.get(id = id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        task.title = title
        task.description = description
        task.save()
        return redirect('/todolist/')
        
    context = {
        'task': task
    }
    return render(request, 'edit.html', context)

def delete(request, id):
    task = TodoList.objects.get(id = id)
    task.delete()
    
    return redirect('/todolist/')