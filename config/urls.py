# config\urls.pu


from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("comp/", include("comp.urls")),
    path("workplace/", include("workplace.urls")),
]
