from rest_framework.routers import SimpleRouter

from django.urls import path
from comp.apps import CompConfig
from comp.views import CompViewSet
urlpatterns = []
app_name = CompConfig.name
router = SimpleRouter()
router.register("", CompViewSet)

urlpatterns += router.urls
