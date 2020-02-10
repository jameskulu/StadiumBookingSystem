from django.shortcuts import render,redirect
from TicketBooking.models import Match
from TicketBooking.forms import UserForm_Match
from django.http import HttpResponse,JsonResponse
from TicketBooking.authenticate import Authenticate

# @Authenticate.valid_user
# def match(request):
#     matches=Match.objects.all()
#     return render(request,"dashboard/match.html",{'matches':matches})

@Authenticate.valid_user
def match(request):
    limit=3
    page=1
    if request.method=="POST":
        if "next" in request.POST:
            page=(int(request.POST['page'])+1)
        elif "prev" in request.POST:
            page=(int(request.POST['page'])-1)
        tempoffset=page-1
        offset=tempoffset*limit
        matches=Match.objects.raw("select * from ticketbooking_match limit 3 offset %s",[offset])
    else:
        matches=Match.objects.raw("select * from ticketbooking_match limit 3 offset 0")
    return render (request,"dashboard/match.html",{'matches':matches, 'page': page})


@Authenticate.valid_user
def create(request):
    if request.method=="POST":
        form=UserForm_Match(request.POST)
        form.save()
        return redirect("/dashboard/match")
    else:
        form=UserForm_Match()
    return render(request,"dashboard/match_create.html",{'form':form})

@Authenticate.valid_user_include_id
def edit(request,id):
    match=Match.objects.get(Match_Id=id)
    return render(request,"dashboard/match_edit.html",{'match':match})

@Authenticate.valid_user_include_id
def update(request,id):
    match=Match.objects.get(Match_Id=id)
    form=UserForm_Match(request.POST,instance=match)
    form.save()
    return redirect("/dashboard/match")

@Authenticate.valid_user_include_id
def delete(request,id):
    Match.objects.get(Match_Id=id)
    match=Match.objects.get(Match_Id=id)
    match.delete()
    return redirect("/dashboard/match")

@Authenticate.valid_user
def search(request):
	matches=Match.objects.filter(Match_Name__contains=request.GET['search']).values()
	return JsonResponse(list(matches),safe=False)
