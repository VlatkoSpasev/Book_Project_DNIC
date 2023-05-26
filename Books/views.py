from django.shortcuts import render, redirect
from .models import Book, Author
from datetime import datetime
from .forms import BookForm, AuthorForm
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

# @login_required
def index(request):
	# return HttpResponse("Hello, world. This is the index page.")

	queryset = Book.objects.all()
	context = {"books": queryset, "Date": datetime.now().date(), "form":BookForm}
	return render(request, "index.html", context=context)


def detail(request, isbn):
	book = Book.objects.get(isbn=isbn)
	return HttpResponse(f"You're looking at book with id = {isbn} and title {book.title}")

def list(request):
	books = Book.objects.all()
	return HttpResponse(f"<i>You're looking at books list.</i><br/>" + ", ".join([str(b) for b in books]))

def add(request):
	if request.method == "POST":
		form_data = BookForm(data=request.POST, files=request.FILES)
		if form_data.is_valid():
			book = form_data.save(commit=False)
			book.user = request.user
			book.cover_image = form_data.cleaned_data['cover_image']
			book.save()
			return redirect("list")

	return render(request, "add.html", context={"form":BookForm})

def add_author(request):
	if request.method == "POST":
		form = AuthorForm(request.POST)
		if form.is_valid():
			author = Author(
				first_name=form.data['first_name'],
				last_name=form.data['last_name'],
				year_of_birth=form.data['year_of_birth'],
				country=form.data['country'],
			)
			author.save()
			return HttpResponseRedirect("/")
	else:
		form = AuthorForm()

	return render(request, "add_author.html", {"form": form})
