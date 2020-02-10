from django.shortcuts import render,redirect
from TicketBooking.forms import UserForm_User,UserForm_Customer
#
# def create(request):
#     return render (request,"dashboard/create.html")


# def create_customer(request):
#     if request.method=="POST":
#         form=UserForm_Customer(request.POST)
#         form.save()
#         return redirect("/dashboard")
#     else:
#         form = UserForm_Customer()
#     return render(request,"dashboard/create.html",{'form':form})



# def create_user(request):
#     if request.method=="POST":
#         form=UserForm_User(request.POST)
#         form.save()
#         return redirect("/dashboard/users")
#     else:
#         form = UserForm_User()
#     return render(request,"dashboard/user_create.html",{'form':form})



# def create_customer(request):
#     if request.method=="POST":
#         form=UserForm_Customer(request.POST)
#         form.save()
#         # return redirect("/")
#     else:
#         form = UserForm_Customer()
#     return render(request,"index.html",{'form':form})


# def create_customer(request):
#     if request.method=="POST":
#         form=UserForm_Customer(request.POST)
#         form.save()
#         return redirect("/")
#     else:
#         form = UserForm_Customer()
#     return render(request,"index.html",{'form':form})


# def create_match(request):
#     if request.method=="POST":
#         form=UserForm_Match(request.POST)
#         form.save()
#         return redirect("/dashboard/match")
#     else:
#         form = UserForm_Match()
#     return render(request,"dashboard/create.html",{'form':form})
