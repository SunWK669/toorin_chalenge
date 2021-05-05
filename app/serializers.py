from rest_framework import serializers
from app.models import Book, Author, PublishingCompany

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"