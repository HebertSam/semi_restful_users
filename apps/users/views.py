from django.shortcuts import render, redirect
from django.contrib import messages

from .models import users

# Create your views here.
def index(request):

    context = {
        'data': users.objects.all(),
    }
    return render(request, 'users/index.html', context)
def show(request, id):
    data = users.objects.get(id=id)
    print data.first_name

    context = {
        'user_data': data
    } 
    return render(request, 'users/user.html', context)

def edit(request, id):
    data = users.objects.get(id=id)
    
    context = {
        'user_data': data
    }
    return render(request, 'users/edit.html', context)
def new_user(request):
    
    return render(request, 'users/create.html' )

def create(request):

    errors = users.objects.basic_validator(request.POST)

    if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/make')
    # print errors
    # if errors != None:
    #     for error in errors:
    #         messages.error(request, error)
    #     return redirect('/create')
    else:
        users.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
    return redirect('/')

def update(request, id):
    errors = users.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error)
        return redirect('/edit/'+ id)
    else:
        user = users.objects.get(id=id)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        return redirect('/')

def delete(request, id):
    user = users.objects.get(id=id)
    user.delete()
    return redirect('/')

