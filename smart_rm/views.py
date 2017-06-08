from django.shortcuts import render
from .forms import *
from django.http import JsonResponse
from .file_system import get_info
from django.http import HttpResponseRedirect

name_list = ['5', '7', '13']
some_name = 'dimas'
def delete(request):
    name_list = ['5', '7', '13']
    return render(request, 'smart_rm/delete.html', locals())

def show(request):
    name_list = ['5', '7', '13']
    return render(request, 'smart_rm/show.html', locals())

def add(request):
    name_list = ['5', '7', '13']
    add_form = AddingForm(request.POST or None)
    if request.method == 'POST' and add_form.is_valid():
        add_form.save()
    return render(request, 'smart_rm/add.html', locals())

def tasks(request):
    name_list = ['5', '7', '13']
    return render(request, 'smart_rm/tasks.html', locals())

def settings(request):
    name_list = ['5', '7', '13']
    return render(request, 'smart_rm/settings.html', locals())

def history(request):
    name_list = ['5', '7', '13']
    return render(request, 'smart_rm/history.html', locals())

def logs(request):
    name_list = ['5', '7', '13']
    return render(request, 'smart_rm/logs.html', locals())

def get_info_for_file_system(request):
    json_answer = get_info('/Users/Dima/dima1')
    print json_answer
    return JsonResponse(json_answer, safe=False)