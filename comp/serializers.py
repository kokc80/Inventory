from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from comp.models import Comp


class CompSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comp
        fields = "__all__"


class CompDetailSerializer(serializers.ModelSerializer):
    comp_count = SerializerMethodField()

    def get_comp_count(self, comp):
        return Comp.objects.filter(comp=comp).count()

    class Meta:
        model = Comp
        fields = "__all__"
