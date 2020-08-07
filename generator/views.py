import numpy as np
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'generator/home.html')

def fail(request):
    return render(request, 'generator/fail.html')

def password(request):
    list_letters = []
    list_letters_lower = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
                    'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                    'z', 'x', 'c', 'v', 'b', 'n', 'm']
    list_letters_upper = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
                    'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
                    'Z', 'X', 'C', 'V', 'B', 'N', 'M']
    list_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    list_special = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
    x = '0'
    if request.GET.get('lowercase'):
        list_letters = list_letters + list_letters_lower
        x='1'
    if request.GET.get('uppercase'):
        list_letters = list_letters + list_letters_upper
        x='1'
    if request.GET.get('special_sign'):
        list_letters = list_letters + list_special
        x='1'
    if request.GET.get('numbers'):
        list_letters = list_letters + list_numbers
        x='1'
    lenght = int(request.GET.get('lenght',12))
    thepassword = ''
    if x == '1':
        chosen1 = np.random.choice(list_letters, lenght)
        for n in chosen1:
            thepassword += n
        return render(request, 'generator/password.html', {'password': thepassword})
    elif x == '0':
        return render(request, 'generator/fail.html')



def about(request):
    return render(request, 'generator/about.html')
