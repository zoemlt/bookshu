from inspect import Attribute
from django.shortcuts import render
from .models import Space

# Create your views here.
def home(request):
    spaces = Space.objects.all()
    context = {"spaces": spaces}
    return render(request, "base/home.html", context)


def space(request, pk):
    space = Space.objects.get(id=pk)
    context = {"space": space}
    return render(request, "base/space.html", context)
