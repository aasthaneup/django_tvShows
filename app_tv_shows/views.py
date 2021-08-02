from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def root(request):
    return redirect('/shows')

def shows(request):
    context = {
        'all_shows' : Show.objects.all()
    }
    return render(request, 'shows.html', context)

# page to create new show:
def create_page(request):
    return render(request, 'create.html')

# page to Display the show's data
def display_page(request, id):
    context = {
        'show' : Show.objects.get(id = id)
    }
    return render(request, 'read.html', context)

# page to update the data
def edit_page(request, id):
    context = {
        'show' : Show.objects.get(id = id)
    }
    return render(request, 'update.html', context)

def create_new(request):
    errors = Show.objects.show_validator(request.POST)

    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect ("/shows/new")
    else:
        newshow = Show.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            releasedate = request.POST['releasedate'],
            desc = request.POST['desc']
        )
        return redirect(f'/shows/{newshow.id}')

def update_show(request, id):
    errors = Show.objects.show_validator(request.POST)

    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect (f"/shows/{id}/edit")

    else:
        show_to_update = Show.objects.get(id = id)
        show_to_update.title = request.POST['title']
        show_to_update.network = request.POST['network']
        show_to_update.releasedate = request.POST['releasedate']
        show_to_update.desc = request.POST['desc']
        show_to_update.save()
        return redirect(f'/shows/{show_to_update.id}')

def delete_show(request, id):
    Show.objects.get(id = id).delete()

    return redirect('/shows')