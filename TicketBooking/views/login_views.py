from django.shortcuts import render,redirect
from TicketBooking.models import User
from TicketBooking.authenticate import Authenticate
from TicketBooking.forms import UserForm_User

def login(request):
    users=User.objects.all()
    return render (request,"login.html",{'users':users})

# def entry(request):
#     request.session['User_Email']=request.POST['User_Email']
#     request.session['User_Password']=request.POST['User_Password']
#     return redirect('/dashboard')

def logout(request):
    request.session['User_Password']=""
    return redirect("/login")
