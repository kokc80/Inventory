# config\urls.pu


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("comp/", include("comp.urls")),
]
