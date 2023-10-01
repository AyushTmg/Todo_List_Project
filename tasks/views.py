from django.shortcuts import render,redirect
from .models import *
from .forms import *

def index(request):
    task=Tasks.objects.all()
    context={'tasks':task,}
    return render(request,'tasks/index.html',context)

def addTask(request):
    form=TaskForm()
    if request.method =='POST':
        form = TaskForm (request.POST)
        if form.is_valid():
            form.save()
         
        else:
            print(form.errors)
        return redirect("/")
        
    context={'form':form,}
    return render(request,'tasks/add_task.html',context)

def viewTask(request,pk):
    task=Tasks.objects.get(id=pk)
    if request.method=='POST':
        return redirect("/")
    context={'tasks':task} 
    return render(request,'tasks/view_task.html',context)
    

def updateTask(request,pk):
    task=Tasks.objects.get(id=pk)
    form=TaskForm(instance=task)
    if request.method=='POST':
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')


    context={'form':form}
    return render(request,'tasks/update_task.html',context)

def deleteTask(request,pk):
    item=Tasks.objects.get(id=pk)

    if request.method=='POST':
        item.delete()
        return redirect('/')

    context={'items':item}
    return render(request,'tasks/delete_task.html',context)