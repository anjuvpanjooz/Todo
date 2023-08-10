from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from todoapp.forms import TodoForm
from todoapp.models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
# Create your views
class TaskListview(ListView):
    model=Task
    template_name='home.html'
    context_object_name='task1'
class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'
class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields=('task_name','priority','date')
    def get_success_url(self):
        return reverse_lazy('todoapp:cvdetail',kwargs={'pk':self.object.id})
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('todoapp:cvhome')

def add(request):
    task1=Task.objects.all()
    if request.method=='POST':
        task_name=request.POST.get('task_name','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(task_name=task_name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'task1':task1})
def update(request,id):
        task=Task.objects.get(id=id)
        f=TodoForm(request.POST or None,instance=task)
        if f.is_valid():
            f.save()
            return redirect('/')
        return render(request,'edit.html',{'f':f,'task':task})
def delete(request,id):
    task=Task.objects.get(id=id)
    if request.method =='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')
