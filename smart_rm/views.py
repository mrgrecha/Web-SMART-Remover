from django.shortcuts import render

def delete(request):
    return render(request, 'smart_rm/delete.html')

def show(request):
    return render(request, 'smart_rm/show.html')

def add(request):
    return render(request, 'smart_rm/add.html')

def tasks(request):
    return render(request, 'smart_rm/tasks.html')

def settings(request):
    return render(request, 'smart_rm/settings.html')

def history(request):
    return render(request, 'smart_rm/history.html')

def logs(request):
    return render(request, 'smart_rm/logs.html')