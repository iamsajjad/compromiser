from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime
from signalData.models import Coordinate
from .models import User

from hashlib import sha3_512

# Create your views here.


def Base(request):

    return render(request, 'base/base.html')

def Create(request):

    username = request.POST['username']
    password = request.POST['password']

    code = sha3_512(str(datetime.now()).encode()).hexdigest()
    user = User.objects.create(
        username = username,
        password = password,
        code = code
    )
    defaultLoaction = Coordinate.objects.create(
        latitude = 0,
        longitude = 0,
        altitude = 10
    )
    user.coordinates.add(defaultLoaction)
    user.save()

    return render(request, 'base/informations.html', {'code' : code})

def Show(request):

    username = request.POST['username']
    password = request.POST['password']

    try:
        user = User.objects.filter(username=username)[0]
    except Exception as e:
        return render(request, 'base/base.html')

    if password == user.password:
        code = user.code
    else:
        return render(request, 'base/base.html')


    return HttpResponseRedirect('/dataOut/{0}'.format(code))
