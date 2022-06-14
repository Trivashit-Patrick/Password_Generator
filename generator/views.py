from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html' )

def about(request):
        return render(request,'generator/about.html')

def password(request):

    Characters = list('abcdefghijklmmnopqrstuvwxyz')
    passw=''
    if request.GET.get('uppercase'):
        Characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('specialcharacters'):
        Characters.extend(list('!@@#$%^&*()'))
    if request.GET.get('numbers'):
        Characters.extend(list('1234567890'))

    length = int(request.GET.get('length',12))
    for i in range(length):
        passw += random.choice(Characters)

    return render(request,'generator/password.html',{'password':passw})# {'password':thepassword} )
