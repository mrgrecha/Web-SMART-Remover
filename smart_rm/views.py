from django.shortcuts import render
# from .forms import *
from .models import *
import os
from django.http import JsonResponse
from .file_system import get_info
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.decorators.csrf import csrf_exempt
import config_changing
import source.src.trash
import source.high_level_operations
import source.src.serialization


def clean_list(some_list, key):
    if key:
        x = [file.encode('ascii', 'ignore')[1:] for file in
         some_list[key][0].replace('&#39;', '').replace('[', '').replace(']', '').split(
            ', ')]
        print 'XXX', x
        return x
    else:
        y =  [file.encode('ascii', 'ignore') for file in
        some_list[0].replace('&#39;', '').replace('[', '').replace(']', '').split(
             ', ')]
        print 'YYY', y
        return y

@csrf_exempt
def add_task(request):
    data = dict(request.POST)
    current_trash = Trash_bin.objects.get(name=data['trash'][0])
    task_instance = Task(current_trash_bin=current_trash,
                         files=[file.encode('ascii', 'ignore') for file in data['files[]']],
                         name_of_operation='Remove to trash')
    task_instance.save()
    return render(request, 'smart_rm/success.html')


@csrf_exempt
def execute_task(request):
    data = dict(request.POST)
    name_of_operation = data['operation'][0]
    files = data['files']
    current_trash_bin = data['trash']
    config_name = 'config_of_' + current_trash_bin[0] + '.cfg'
    my_trash = source.src.trash.Trash(os.path.join(os.path.expanduser('~'), '.Configs_for_web_rm', config_name))
    print 'Name of operation', name_of_operation
    status = 'Done'
    if name_of_operation == 'Remove from trash':
        try:
            source.high_level_operations.high_deleting_files_from_trash(the_trash=my_trash,
                                                                        list_of_files=clean_list(data, 'hashes'))
            #TODO: for each case add except with status/ make code better/ fix bug with remove file
        except:
            pass
        finally:
            history_instance = History(files=clean_list(data, 'hashes'), trash_bin=current_trash_bin,
                                       name_of_operation=name_of_operation,
                                       state=status)
            history_instance.save()
    elif name_of_operation == 'Remove to trash':
        source.high_level_operations.high_remove(clean_list(files, False), my_trash)
        history_instance = History(files=files, trash_bin=current_trash_bin, name_of_operation=name_of_operation,
                                   state='Done')
        history_instance.save()

    elif name_of_operation == 'Recover':
        source.high_level_operations.high_recover(the_trash=my_trash,
                                                                    list_of_files=clean_list(data, 'hashes'))
        history_instance = History(files=files, trash_bin=current_trash_bin, name_of_operation=name_of_operation,
                                   state='Done')
        history_instance.save()

    print 'History was saved'
    Task.objects.get(id=data['task_id'][0]).delete()
    return render(request, 'smart_rm/success.html')


@csrf_exempt
def execute_regular_task(request):
    data = dict(request.POST)
    start_folder = data['start_folder'][0]
    pattern = data['pattern'][0]
    current_trash_bin = data['trash']
    config_name = 'config_of_' + current_trash_bin[0] + '.cfg'
    my_trash = source.src.trash.Trash(os.path.join(os.path.expanduser('~'), '.Configs_for_web_rm', config_name))
    source.high_level_operations.high_regular_removing(start_folder=start_folder, pattern=pattern, the_trash=my_trash)
    history_instance = History(pattern=pattern, start_folder=start_folder, trash_bin=current_trash_bin, name_of_operation='Regular removing',
                               state='Done')
    history_instance.save()
    RegularTask.objects.get(id=data['task_id'][0]).delete()
    return render(request, 'smart_rm/success.html')


@csrf_exempt
def delete_regular_task(request):
    data = dict(request.POST)
    RegularTask.objects.get(id=data['task_id'][0]).delete()
    return render(request, 'smart_rm/success.html')


@csrf_exempt
def delete_task(request):
    data = dict(request.POST)
    Task.objects.get(id=data['task_id'][0]).delete()
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


def show_trash(request, pk):
    name_of_database = str(pk) + '.json'
    path_to_database = os.path.join(os.path.expanduser('~'), '.Configs_for_web_rm', name_of_database)
    with open(path_to_database, 'r'):
        arr_json_files = source.src.serialization.load_json(path_to_database)
    return render(request, 'smart_rm/show_trash.html', locals())

def tasks(request):
    current_page = 'tasks'
    name_list = Trash_bin.objects.all()
    regular_tasks = RegularTask.objects.all()
    tasks_list = Task.objects.all()
    return render(request, 'smart_rm/tasks.html', locals())


@csrf_exempt
def recover(request, pk):
    data = dict(request.POST)
    task_instance = Task(files=data['names[]'], current_trash_bin=Trash_bin.objects.get(name=pk), hashes=data['hashes[]'], name_of_operation='Recover')
    task_instance.save()
    return render(request, 'smart_rm/success.html')


@csrf_exempt
def remove_from_trash(request, pk):
    data = dict(request.POST)
    print data
    task_instance = Task(files=data['names[]'], current_trash_bin=Trash_bin.objects.get(name=pk),
                         hashes=data['hashes[]'], name_of_operation='Remove from trash')
    task_instance.save()
    return render(request, 'smart_rm/success.html')

def history(request):
    current_page = 'history'
    history_list = History.objects.all()
    return render(request, 'smart_rm/history.html', locals())

def settings_without_bin(request):
    current_page = 'settings'
    name_list = Trash_bin.objects.all()
    return render(request, 'smart_rm/settings.html', locals())


def regex(request):
    current_page = 'history'
    name_list = Trash_bin.objects.all()
    return render(request, 'smart_rm/regex.html', locals())




def get_info_for_file_system(request):
    print 'Get info:', request.GET
    id = request.GET['id']
    if id == '#':
        home = os.path.expanduser('~')
        return JsonResponse(get_info(home), safe=False)
    else:
        return JsonResponse(get_info(id), safe=False)


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
        kwargs = super(TrashBinCreate, self).get_form_kwargs()
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
            config_changing.make_config(name_of_trash_bin=kwargs['data']['name'],
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
            config_changing.make_config(name_of_trash_bin=kwargs['data']['name'],
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


   def get_object(self, queryset=None):
       trash_bin = super(TrashBinDelete, self).get_object()
       config_changing.remove_trash_bin(name_of_trash_bin=trash_bin)
       return trash_bin


class RegularCreate(CreateView):
    model = RegularTask
    template_name = 'smart_rm/regex.html'
    fields = '__all__'
    success_url = "/success/"