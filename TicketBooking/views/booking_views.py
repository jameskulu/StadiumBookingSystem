from django.shortcuts import render,redirect
from TicketBooking.models import Booking,Match
from TicketBooking.forms import UserForm_Booking
from django.http import HttpResponse,JsonResponse
from TicketBooking.authenticate import Authenticate

# @Authenticate.valid_user
# def booking(request):
#     bookings=Booking.objects.all()
#     return render(request,"dashboard/booking.html",{'bookings':bookings})

@Authenticate.valid_user
def booking(request):
    limit=3
    page=1
    if request.method=="POST":
        if "next" in request.POST:
            page=(int(request.POST['page'])+1)
        elif "prev" in request.POST:
            page=(int(request.POST['page'])-1)
        tempoffset=page-1
        offset=tempoffset*limit
        bookings=Booking.objects.raw("select * from ticketbooking_booking limit 3 offset %s",[offset])
    else:
        bookings=Booking.objects.raw("select * from ticketbooking_booking limit 3 offset 0")
    return render (request,"dashboard/booking.html",{'bookings':bookings, 'page': page})

@Authenticate.valid_user_include_id
def edit(request,id):
    seats=Booking.objects.all()
    matches=Match.objects.all()
    booking=Booking.objects.get(Booking_Id=id)
    return render(request,"dashboard/booking_edit.html",{'booking':booking,'matches':matches,'seats':seats})

@Authenticate.valid_user_include_id
def update(request,id):
    booking=Booking.objects.get(Booking_Id=id)
    form=UserForm_Booking(request.POST,instance=booking)
    form.save()
    return redirect("/dashboard/booking")

@Authenticate.valid_user_include_id
def delete(request,id):
    Booking.objects.get(Booking_Id=id)
    booking=Booking.objects.get(Booking_Id=id)
    booking.delete()
    return redirect("/dashboard/booking")

@Authenticate.valid_user
def search(request):
	booking=Booking.objects.filter(Customer_id=request.GET['search']).values()
	return JsonResponse(list(booking),safe=False)
