from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characters =  list('abcdefghijklmnopqrstuvwxyz')
    lenght = int(request.GET.get('lenght',10))


    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!”#$%&’()*+,-./:;<>=?@[]{}\^`_|~') )
    if request.GET.get('numbers'):
        characters.extend(list('0123456789') )


    thePassword = ''
    for x in range(lenght):
        thePassword += random.choice(characters)



    return render(request, 'generator/password.html', {'password':thePassword})

def about(request):
    return render(request, 'generator/about.html')
