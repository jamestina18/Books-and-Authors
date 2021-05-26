from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def index(request):
     authors = Author.objects.all()
     context = {
          "authors": authors
     }
     return render(request,'index.html', context)

def add_user(request):
     if request.method == "POST":
          first_name = request.POST['first_name']
          last_name = request.POST['last_name']

          Author.objects.create(first_name= first_name, last_name= last_name)
     return redirect("/")