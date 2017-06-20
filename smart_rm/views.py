from django.shortcuts import render
from .forms import *
import json
from django.http import JsonResponse
from .file_system import get_info
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
import make_config


name_list = Trash_bin.objects.all()
some_name = 'dimas'


def get_context_data(self, **kwargs):
    data = super(CreateView, self).get_context_data(**kwargs)
    data['name_list'] = Trash_bin.objects.all()
    return data

@csrf_exempt
def add_task(request):
    data = dict(request.POST)
    current_trash = Trash_bin.objects.get(name=data['trash'][0])
    task_instance = Task(current_trash_bin=current_trash, files_to_delete=data['files[]'])
    task_instance.save()
    return render(request, 'smart_rm/success.html')

@csrf_exempt
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
    regular_tasks = RegularTask.objects.all()
    tasks_list = Task.objects.all()
    return render(request, 'smart_rm/tasks.html', locals())

def settings_without_bin(request):
    current_page = 'settings'
    name_list = Trash_bin.objects.all()
    return render(request, 'smart_rm/settings.html', locals())

def regex(request):
    current_page = 'history'
    name_list = Trash_bin.objects.all()
    return render(request, 'smart_rm/regex.html', locals())

def logs(request):
    current_page = 'logs'
    name_list = Trash_bin.objects.all()
    return render(request, 'smart_rm/logs.html', locals())

def get_info_for_file_system(request):
    json_answer = get_info('/Users/Dima/dima1')
    #print json_answer
    return JsonResponse(json_answer, safe=False)

def get_trash_bin(request, trashBin):
    cur_trash = Trash_bin.objects.get(name=trashBin)
    return cur_trash

def success(request):
    name_list = Trash_bin.objects.all()
    return render(request, 'smart_rm/success.html', locals())



class TrashBinCreate(CreateView):
    model = Trash_bin
    template_name = 'smart_rm/add.html'
    fields = '__all__'
    success_url = "/success/"

    def get_context_data(self, **kwargs):
        data = super(CreateView, self).get_context_data(**kwargs)
        data['name_list'] = Trash_bin.objects.all()
        return data

    def get_form_kwargs(self):
        kwargs = super(TrashBinUpdate, self).get_form_kwargs()
        try:
            kwargs['data']['dried']
            dried = True
        except KeyError:
            dried = False

        try:
            kwargs['data']['silent']
            silent = True
        except KeyError:
            silent = False

        try:
            make_config.make_config(name_of_trash_bin=kwargs['data']['name'],
                                    path_of_trash_bin=kwargs['data']['path_of_trash'],
                                    max_size=int(kwargs['data']['size']), max_time=int(kwargs['data']['time']),
                                    max_num=int(kwargs['data']['number']), policies=kwargs['data']['policies'],
                                    dried=dried, silent=silent)
        except KeyError:
            print 'KeyError'
        return kwargs


class TrashBinUpdate(UpdateView):
    name_list = Trash_bin.objects.all()
    model = Trash_bin
    template_name = 'smart_rm/settings_with_trash_bin.html'
    fields = '__all__'
    success_url = "/success/"

    def get_context_data(self, **kwargs):
        data = super(UpdateView, self).get_context_data(**kwargs)
        data['name_list'] = Trash_bin.objects.all()
        return data

    def get_form_kwargs(self):
        kwargs = super(TrashBinUpdate, self).get_form_kwargs()
        try:
            kwargs['data']['dried']
            dried = True
        except KeyError:
            dried = False

        try:
            kwargs['data']['silent']
            silent = True
        except KeyError:
            silent = False

        try:
            make_config.make_config(name_of_trash_bin=kwargs['data']['name'],
                                    path_of_trash_bin=kwargs['data']['path_of_trash'],
                                    max_size=int(kwargs['data']['size']), max_time=int(kwargs['data']['time']),
                                    max_num=int(kwargs['data']['number']), policies=kwargs['data']['policies'],
                                    dried=dried, silent=silent)
        except KeyError:
            print 'KeyError'
        return kwargs


class TrashBinDelete(DeleteView):
   model = Trash_bin
   success_url = '/success/'

class RegularCreate(CreateView):
    model = RegularTask
    template_name = 'smart_rm/regex.html'
    fields = '__all__'
    success_url = "/success/"