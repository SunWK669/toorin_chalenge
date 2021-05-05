from django.contrib import admin

from app.models import Author, Book, PublishingCompany

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(PublishingCompany)