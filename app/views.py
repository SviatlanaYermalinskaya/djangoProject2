from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    return render(request, 'index.html')


names = {'Egor', 'Olya', 'Alex', 'Alena', 'Oleg'}
@csrf_exempt
def some_url(request, s: str):
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



