from django.shortcuts import render
from .models import Book

# Create your views here.

def index(request):
	queryset = Book.objects.all()
	return render(request, "index.html")