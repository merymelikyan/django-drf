from django.urls import path
from .views import custom_upload_function


urlpatterns = [
   path("upload/", custom_upload_function, name="custom_upload_file"),
]
