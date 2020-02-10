from django.shortcuts import render,redirect
from TicketBooking.models import Customer
from TicketBooking.forms import UserForm_Customer
from django.http import HttpResponse,JsonResponse
from TicketBooking.authenticate import Authenticate

@Authenticate.valid_user
def customer(request):
    limit=3
    page=1
    if request.method=="POST":
        if "next" in request.POST:
            page=(int(request.POST['page'])+1)
        elif "prev" in request.POST:
            page=(int(request.POST['page'])-1)
        tempoffset=page-1
        offset=tempoffset*limit
        customers=Customer.objects.raw("select * from ticketbooking_customer limit 3 offset %s",[offset])
    else:
        customers=Customer.objects.raw("select * from ticketbooking_customer limit 3 offset 0")
    return render (request,"dashboard/customer.html",{'customers':customers, 'page': page})



@Authenticate.valid_user_include_id
def edit(request,id):
    customer=Customer.objects.get(Customer_Id=id)
    return render(request,"dashboard/customer_edit.html",{'customer':customer})

@Authenticate.valid_user_include_id
def update(request,id):
    customer=Customer.objects.get(Customer_Id=id)
    form=UserForm_Customer(request.POST,instance=customer)
    form.save()
    return redirect("/dashboard/customer")

@Authenticate.valid_user_include_id
def delete(request,id):
    Customer.objects.get(Customer_Id=id)
    customer=Customer.objects.get(Customer_Id=id)
    customer.delete()
    return redirect("/dashboard/customer")

@Authenticate.valid_user
def search(request):
	customers=Customer.objects.filter(Customer_Email=request.GET['search']).values()
	return JsonResponse(list(customers),safe=False)
