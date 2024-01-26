from django.shortcuts import render

def home(request):
    return render(request,'recipes/pages/home.html',context={
        'name': 'Thiago Morais'
    })

# Create your views here.
