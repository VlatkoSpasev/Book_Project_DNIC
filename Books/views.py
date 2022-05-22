from django.shortcuts import render
from .models import Book
from datetime import datetime
from .forms import BookForm
# Create your views here.

def index(request):
	queryset = Book.objects.filter(user=request.user).all()
	context = {"books": queryset, "Date": datetime.now().date(), "form":BookForm}
	return render(request, "index.html", context=context)