from django.urls import include, path
from rest_framework.routers import DefaultRouter

from app.views import BookViewSet

routers = DefaultRouter()
routers.register("books", BookViewSet)

urlpatterns = [path("", include(routers.urls))]
