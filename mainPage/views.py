from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

def mainPageView(request) :
    return render(request, 'mainPage/index.html')

def contactMeView(request) :
    if request.method == "POST":
        cName = request.POST['cName']
        cEmail = request.POST['cEmail']
        cMessage = request.POST['cMessage']

        # send an email
        send_mail(
            cName, #subject
            cMessage, #message
            cEmail, #from email
            ['jacobawelling@gmail.com'], #to email
        )


        return render(request, 'mainPage/index.html', { 'cName': cName })
    else:
        return render(request, 'mainPage/index.html', {'cName': ''})

