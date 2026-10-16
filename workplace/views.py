# workplace\views.py

from django.shortcuts import get_object_or_404, render

from .models import Workplace


def wp_list(request):
    w_places = Workplace.objects.all()
    return render(request, 'workplace/wp_list.html', {'workplaces': w_places})


def wp_detail(request, pk):
    w_place = get_object_or_404(Workplace, pk=pk)
    return render(request, 'workplace/wp_detail.html', {'workplace': w_place})
