from django import forms
from .models import Book

class BookForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(BookForm, self).__init__(*args, **kwargs)
		for field in self.visible_fields():
			print(field)
			field.field.widget.attrs["class"] = "form-control"

			
	class Meta:
		model = Book
		exclude = ("user",)