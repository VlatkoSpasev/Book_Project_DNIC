from django.shortcuts import render, redirect
from .models import Book
from datetime import datetime
from .forms import BookForm
# Create your views here.

def index(request):
	if request.method == "POST":
		form_data = BookForm(data=request.POST, files=request.FILES)
		if form_data.is_valid():
			book = form_data.save(commit=False)
			book.user = request.user
			book.cover_image = form_data.cleaned_data['cover_image']
			book.save()
			return redirect("books")
			
	queryset = Book.objects.filter(user=request.user).all()
	context = {"books": queryset, "Date": datetime.now().date(), "form":BookForm}
	return render(request, "index.html", context=context)
