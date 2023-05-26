from django.contrib import admin
from .models import Author, Book, Publication, PublicationAuthor

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
	pass
	list_display = ("first_name", "last_name", "year_of_birth", "count_books")
	list_filter = ("first_name", "last_name", "year_of_birth")
	search_fields = ("last_name__startswith", "first_name__startswith",)

	def count_books(self, author):
		from django.utils.html import format_html

		result = Book.objects.filter(author=author).count()
		return format_html(f"<b>{result}</b>")

	count_books.short_description = "Number of books by author"


	def has_add_permission(self, request, obj=None):
		if request.user.is_superuser:
			return True
		return False

	def has_change_permission(self, request, obj=None):
		return True

	def has_delete_permission(self, request, obj=None):
		return True

admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
	list_display = ("title", "isbn", "author")
	def get_queryset(self, request):
		qs = super().get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(author=request.user)

admin.site.register(Book, BookAdmin)


class PublicationAuthorAdmin(admin.StackedInline):
	model = PublicationAuthor
	extra = 1


class PublicationBookAdmin(admin.TabularInline):
	model = Book
	readonly_fields = ('title', 'isbn', )
	extra = 2


class PublicationAdmin(admin.ModelAdmin):
	inlines=[PublicationAuthorAdmin, PublicationBookAdmin, ]

admin.site.register(Publication, PublicationAdmin)