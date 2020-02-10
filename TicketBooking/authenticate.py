from django.shortcuts import render,redirect
from TicketBooking.models import User
from django.db.models import Q
from django.contrib import messages


class Authenticate:
    def valid_user(function):
        def wrap(request):
            try:
                users = User.objects.get(Q(User_Email=request.session['User_Email']) & Q(User_Password=request.session['User_Password'])) #Matching email and password from users table
                return function(request)
            except:
                # messages.warning(request,"please login...")
                messages.warning(request,"**Please enter valid Email/Password",extra_tags='alert') #message warming
                return redirect("/")
        return wrap

    def valid_user_include_id(function):
        def wrap(request,id):
            try:
                users = User.objects.get(Q(User_Email=request.session['User_Email']) & Q(User_Password=request.session['User_Password']))
                return function(request,id)
            except:
                    # messages.warning(request,"please login...")

                return redirect ("/")
        return wrap
