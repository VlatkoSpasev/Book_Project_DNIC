# Users
## Add new user and check permissions
```python
from django.contrib.auth.models import User
u = User.objects.create_user(username='student')
u.has_perm('auth.change_user')
```
## Add new superuser and check permissions

```python
from django.contrib.auth.models import User
superuser = User.objects.create_superuser(
    username='super_student',
    email='super@finki.com',
    password='secret',
)
superuser.has_perm('does.not.exist')
```

## List all users ad superusers
```python
from django.contrib.auth.models import User
User.objects.all()
User.objects.filter(is_superuser=True)
```

## List other objects
```python
from Books.models import Book
Book.objects.values_list()
```

## Authenticating user
```python
from django.contrib.auth import authenticate
user = authenticate(username="super_student", password="secret")
```

## Create permissions
```python
from Books.models import Book
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

content_type = ContentType.objects.get_for_model(Book)
permission = Permission.objects.create(
    codename="can_publish",
    name="Can Publish Book",
    content_type=content_type,
)

# user.user_permissions.add(permission)
```

## Change permissions
```python
from Books.admin import AuthorAdmin
from Books.models import Book

def has_change_permission(self, request, obj: Book = None):
    if obj:
        if obj.author == request.user:
             return request.user.has_perm()
        else:
            return False
    return super(AuthorAdmin, self).has_change_permission(self, request, obj)
```

## Filter queryset by logged user
```python
def get_queryset(self, request):
    qs = super().get_queryset(request)
    if request.user.is_superuser:
        return qs
    return qs.filter(author=request.user)
```

