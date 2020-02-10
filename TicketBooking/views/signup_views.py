from django.shortcuts import render,redirect
from TicketBooking.models import Customer
from TicketBooking.forms import UserForm_Customer

def signup(request):
    if request.method=="POST":
        request.session['session_Customer_First_Name']=request.POST['Customer_First_Name']
        request.session['session_Customer_Last_Name']=request.POST['Customer_Last_Name']
        request.session['session_Customer_email']=request.POST['Customer_Email']

        form=UserForm_Customer(request.POST) #Customer
        form.save()
        request.session['allow_signup']=True
        return redirect("/")
    else:
        form = UserForm_Customer()
    return render(request,"signup.html",{'form':form})

def logout(request):
    request.session['session_Customer_Last_Name']=""
    request.session['session_Customer_First_Name']=""
    request.session['session_Customer_email']=""
    return redirect("/")
