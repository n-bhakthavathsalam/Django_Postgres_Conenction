from django.shortcuts import render
from.models import Employee1


def index(request):
    obj = Employee1.objects.all()
    context = {'obj':obj}
    return render(request, 'index.html', context)

