from authors.models import Author
from django.contrib import admin

from users.models import User

admin.site.register(Author)
admin.site.register(User)
