from django import forms
from .models import Book, Author

class BookForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(BookForm, self).__init__(*args, **kwargs)
		for field in self.visible_fields():
			field.field.widget.attrs["class"] = "form-control"
	#
	class Meta:
		model = Book
		exclude = ("user",)


class AuthorForm(forms.Form):
	first_name = forms.CharField(max_length=5)
	last_name = forms.CharField(max_length=20)
	year_of_birth = forms.IntegerField()
	country = forms.CharField(max_length=20)
	biography = forms.CharField(widget=forms.Textarea)

	def __init__(self, *args, **kwargs):
		super(AuthorForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'