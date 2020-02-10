from django.shortcuts import render,redirect
from TicketBooking.models import User
from TicketBooking.forms import UserForm_User
from django.http import HttpResponse,JsonResponse
from TicketBooking.authenticate import Authenticate

@Authenticate.valid_user  #Authentication for privileged users
def user(request):
    limit=3
    page=1
    if request.method=="POST":  #FOR PAGINATION
        if "next" in request.POST:
            page=(int(request.POST['page'])+1)
        elif "prev" in request.POST:
            page=(int(request.POST['page'])-1)
        tempoffset=page-1
        offset=tempoffset*limit
        users=User.objects.raw("select * from ticketbooking_user limit 3 offset %s",[offset]) #Extracting data from table
    else:
        users=User.objects.raw("select * from ticketbooking_user limit 3 offset 0")  #Extracting data from table
    return render (request,"dashboard/users.html",{'users':users, 'page': page})  #Requesting html file


@Authenticate.valid_user
def create(request): #For adding users
    if request.method=="POST":
        form=UserForm_User(request.POST)
        form.save()
        return redirect("/dashboard/users")
    else:
        form = UserForm_User()
    return render(request,"dashboard/user_create.html",{'form':form})

@Authenticate.valid_user_include_id
def edit(request,id):   #For editing users
    user=User.objects.get(User_Id=id)
    return render(request,"dashboard/user_edit.html",{'user':user})

@Authenticate.valid_user_include_id
def update(request,id):   #For updating users
    user=User.objects.get(User_Id=id)
    form=UserForm_User(request.POST,instance=user)
    form.save()
    return redirect("/dashboard/users")

@Authenticate.valid_user_include_id
def delete(request,id):  #For deleteing users
    User.objects.get(User_Id=id)
    user=User.objects.get(User_Id=id)
    user.delete()
    return redirect("/dashboard/users")

@Authenticate.valid_user
def search(request): #For searching users
	users=User.objects.filter(User_Email=request.GET['search']).values()
	return JsonResponse(list(users),safe=False)
