# Create your views here.
from rest_framework.viewsets import ModelViewSet
from comp.models import Comp
from comp.serializers import CompSerializer


class CompViewSet(ModelViewSet):
    queryset = Comp.objects.all()
    serializer_class = CompSerializer
