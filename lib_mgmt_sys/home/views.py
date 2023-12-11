from django.http import HttpResponse
from django.shortcuts import  redirect, render
from .forms import AuthorAddForm, BookModelForm
from .models import Author, Book

# Create your views here.
def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html' )


def feature(request):
    return render(request, 'feature.html' )


def add_author(request):
    if request.method=="GET":
        add_author_form = AuthorAddForm()
        return render(request, 'add_author.html', context={'form':add_author_form})
    elif request.method =="POST":
        add_author_form = AuthorAddForm(request.POST)
        name = request.POST['name']
        age = request.POST['age']
        author = Author.objects.create(name=name, age=age)
        return HttpResponse('Author is added successfully.')


def list_book(request):
    book = Book.objects.all()
    return render(request, 'list_book.html', {'books':book})



def add_book(request):
    if request.method =="GET":
        add_book_form = BookModelForm
        return render(request, 'add_book.html', context={'form':add_book_form})
    else:
        add_book_form = BookModelForm(request.POST)
        if add_book_form.is_valid():
            add_book_form.save()
            return redirect(list_book)

    return render(request, 'add_book.html', context={'form':add_book_form})



def edit_book(request,id):
    book = Book.objects.get(id=id)
    if request.method =="GET":
        form = BookModelForm(instance = book)
        return render(request, 'edit_book.html', {'form':form})

    elif request.method =="POST":
        form = BookModelForm(request.POST, instance = book)
        if form.is_valid():
            form.save()
            return redirect('list_book')
    return render(request, 'edit_book.html', {'form':form})



def delete_book(request,id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('list_book')
   
