from django.shortcuts import render,redirect
from TicketBooking.forms import UserForm_Booking,UserForm_Customer
from TicketBooking.models import Match,Booking,Customer,User
from django.http import HttpResponse

def index(request):
    if request.method=="POST":
        form2=UserForm_Booking(request.POST)
        form2.save()
        del request.session['allow_signup']
        del request.session['session_Customer_email']
        del request.session['session_Customer_First_Name']
        del request.session['session_Customer_Last_Name']
        return redirect("/")
    else:
        form2=UserForm_Booking()
        users=User.objects.all()
        matches=Match.objects.all()
    return render(request,"index.html",{'matches':matches,'form2':form2,'users':users})

def entry(request):
    request.session['User_Email']=request.POST['User_Email']
    request.session['User_Password']=request.POST['User_Password']
    return redirect('/dashboard')

def logout(request):
    request.session['User_Password']=""
    return redirect("/")
