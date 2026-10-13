# comp\views.py


from django.shortcuts import render, get_object_or_404
from .models import Comp

def comp_list(request):
    comps = Comp.objects.all()
    return render(request, 'comp/comp_list.html', {'comps': comps})

def comp_detail(request, pk):
    comp = get_object_or_404(Comp, pk=pk)
    return render(request, 'comp/comp_detail.html', {'comp': comp})