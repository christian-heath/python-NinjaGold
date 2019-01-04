from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime
import random

def activitylog(request, location, gold, time):
    message = "<p>You leave the "+str(location)+" with "+str(gold)+" gold at "+str(time)+"</p>"
    request.session['activity'] += message

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activity' not in request.session:
        request.session['activity'] = "Hello! Welcome to Ninja Gold!"
    return render(request, "ninja_gold/index.html")

def process(request):
    if request.method == "POST":
        buildingName = request.POST['building']
        time = strftime("%a, %d %b %Y %H:%M:%S", localtime())
        if request.POST['building'] == 'farm':
            gold = random.randrange(10,21)
            request.session['gold'] += gold
            activitylog(request, buildingName, gold, time)
        if request.POST['building'] == 'cave':
            gold = random.randrange(5,11)
            request.session['gold'] += gold
            activitylog(request, buildingName, gold, time)
        if request.POST['building'] == 'house':
            gold = random.randrange(2,6)
            request.session['gold'] += gold
            activitylog(request, buildingName, gold, time)
        if request.POST['building'] == 'casino':
            gold = random.randrange(-50,51)
            request.session['gold'] += gold
            activitylog(request, buildingName, gold, time)
        return redirect('/')
    else:
        return redirect('/')

def reset(request):
    del request.session['gold']
    del request.session['activity']
    return redirect('/')
