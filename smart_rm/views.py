from django.shortcuts import render
from .forms import *
from django.http import JsonResponse
from .file_system import get_info
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy

name_list = Trash_bin.objects.all()
some_name = 'dimas'

def delete(request):
    name_list = Trash_bin.objects.all()
    current_page = 'delete'
    return render(request, 'smart_rm/delete.html', locals())

def show(request):
    name_list = Trash_bin.objects.all()
    current_page = 'show'
    return render(request, 'smart_rm/show.html', locals())

def add(request):
    name_list = Trash_bin.objects.all()
    add_form = AddingForm(request.POST or None)
    if request.method == 'POST' and add_form.is_valid():
        add_form.save()
    return render(request, 'smart_rm/add.html', locals())

def tasks(request):
    current_page = 'tasks'
    name_list = Trash_bin.objects.all()
    return render(request, 'smart_rm/tasks.html', locals())

def settings_without_bin(request):
    current_page = 'settings'
    name_list = Trash_bin.objects.all()
    return render(request, 'smart_rm/settings.html', locals())

def history(request):
    current_page = 'history'
    name_list = Trash_bin.objects.all()
    return render(request, 'smart_rm/history.html', locals())

def logs(request):
    current_page = 'logs'
    name_list = Trash_bin.objects.all()
    return render(request, 'smart_rm/logs.html', locals())

def get_info_for_file_system(request):
    json_answer = get_info('/Users/Dima/dima1')
    print json_answer
    return JsonResponse(json_answer, safe=False)

def get_trash_bin(request, trashBin):
    cur_trash = Trash_bin.objects.get(name=trashBin)
    return cur_trash

def success(request):
    return render(request, 'smart_rm/success.html')


class TrashBinCreate(CreateView):
    name_list = Trash_bin.objects.all()
    model = Trash_bin
    template_name = 'smart_rm/add.html'
    fields = '__all__'
    success_url = "/success/"

class TrashBinUpdate(UpdateView):
    name_list = Trash_bin.objects.all()
    model = Trash_bin
    template_name = 'smart_rm/settings_with_trash_bin.html'
    fields = '__all__'
    success_url = "/success/"

class TrashBinDelete(DeleteView):
   model = Trash_bin
   success_url = '/success/'