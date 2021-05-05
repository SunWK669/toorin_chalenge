from rest_framework import viewsets
from rest_framework.views import Response
from rest_framework import permissions
from rest_framework import status

from app.models import Book, Author, PublishingCompany
from app.serializers import BookSerializer

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
        

schema_view = get_schema_view(
    openapi.Info(
        title="Books Toorin",
        default_version='v1',
        description="Api to consult books",
        terms_of_service="",
        contact=openapi.Contact(email=""),
        license=openapi.License(name=""),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)