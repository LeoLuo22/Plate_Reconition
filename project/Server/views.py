from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Profile
from django.utils.timezone import datetime
from .main import get_plate_num
import os
# Create your views here.
def index(request):
    return render(request, "index.html")
def process(request):
    file = request.FILES['UpLoadFile']
    content = file.read()
    with open("Server/" + file.name, 'wb') as fh:
        fh.write(content)

    return HttpResponse(get_plate_num("Server/"  + file.name))
