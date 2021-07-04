from django.db.models.aggregates import Avg
from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from django.db.models import Avg
from .models import *
# Create your views here.
def index(request):
    books = Book.objects.all().order_by("-rating")
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    context={
        "books":books,
        "total_number_of_book":num_books,
        "average_rating":avg_rating
    }
    return render(request,'book_outlet/index.html',context)

def book_detail(request,slug):
    #try:
    #    book = Book.objects.get(pk=id)
    #except:
    #    raise Http404()
    book = get_object_or_404(Book,slug=slug)
    context={
        "title":book.title,
        "author":book.author,
        "rating":book.rating,
        "is_bestseller":book.is_bestselling,
    }
    return render(request,'book_outlet/book_detail.html',context)