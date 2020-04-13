from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime
from userView.models import User
from .models import Coordinate

# Create your views here.

def dataIn(request, code, x, y, z):

    date = datetime.now()
    abscissae = Coordinate.objects.create(
        latitude = x,
        longitude = y,
        altitude = z,
        date = date,
    )
    user = User.objects.filter(code=code)[0]
    user.coordinates.add(abscissae)
    abscissae.save()

    return render(request, 'map/dataIn.html')

def dataOut(request, code):

    user = User.objects.filter(code=code)[0]
    abscissae = user.coordinates.last()

    data = {
        'x' : abscissae.latitude,
        'y' : abscissae.longitude,
        'z' : abscissae.altitude,
        'date' : abscissae.date,
        'username' : user.username,
        'code' : user.code,
    }

    return render(request, 'map/dataOut.html', data)
