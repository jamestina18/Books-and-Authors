from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def index(request):
     books = Book.objects.all()
     context = {
          "books": books
     }
     return render(request,'index.html', context)

def add_book(request):
     if request.method == "POST":
          title = request.POST['title']
          desc = request.POST['desc']

          Book.objects.create(title= title, desc= desc)
     return redirect("/")

def assign_book(request, book_id):
     books = Book.objects.get(id=book_id)
     authors = Author.objects.get(id=request.POST['author_id'])
     books.authors.add(authors)
     return redirect(f'/assign-author/{book_id}')

def display_book(request, book_id):
     books = Book.objects.get(id=book_id)
     context = {
          "books": books,
          "authors": Author.objects.exclude(books__id= book_id)
     }
     return render(request, 'book_list.html', context)

def display_author(request, author_id):
     author = Author.object.get(id = author_id)
     context = {
          "author": author,
          "book": Book.objects.exclude(authors__id= author_id)
     }
     return render(request, author.html, context)
