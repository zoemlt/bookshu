from django.shortcuts import render

# Create your views here.
spaces = [
    {"id": 1, "name": "Harry Potter"},
    {"id": 2, "name": "FOG"},
    {"id": 3, "name": "Bible"},
]


def home(request):
    context = {"spaces": spaces}
    return render(request, "base/home.html", context)


def space(request, pk):
    space = None
    for i in spaces:
        if i["id"] == int(pk):
            space = i
    context = {"space": space}
    return render(request, "base/space.html", context)
