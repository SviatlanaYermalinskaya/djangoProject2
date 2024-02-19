from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import pandas as pd

from app.form import ImageForm
from app.models import ModelPerson, Img


# Create your views here.
def index(request):
    return render(request, 'index.html')

def color(request):
    return render(request, 'testo2.html', {'color': 'blue'})


names = {'Egor', 'Olya', 'Alex', 'Alena', 'Oleg'}
@csrf_exempt
def some_url(request, s: str):
    if s == 'some_url':
        return HttpResponse(f"Ваш {request.method} запрос обработан!")
    if s == 'add':
        if request.method == 'POST':
            name = request.POST['input_name'].capitalize()
            if name != '':
                names.add(name)
        return render(request, 'add.html')

    if s.capitalize() in names:
        return render(request, 'hello.html', {'name': s.capitalize()})

    if s == 'name':
        return render(request, 'name.html',{'url': s, 'name': list(names)})

    url = f"http://{request.get_host()}/{s}/"
    return render(request, 'error.html', {'url': url})

@csrf_exempt
def img_form(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            fname = request.FILES['img'].name
            form.save()
            added_image = Img.objects.last()

            return render(request, 'form.html', {'form': form, 'image': added_image, 'fname': fname})
    else:
        form = ImageForm()
    return render(request, 'form.html', {'form': form})

def testo(request):
    person = ModelPerson()
    person.name = 'Name'
    person.surname = 'Surname'
    person.age = 18
    person.profession = 'Profession'
    person.save()
    return render(request, 'testo.html')