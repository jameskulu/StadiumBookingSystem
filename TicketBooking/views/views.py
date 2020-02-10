from django.shortcuts import render
from TicketBooking.authenticate import Authenticate

@Authenticate.valid_user
def dashboard(request):
    return render (request,"dashboard/dashboard.html")
