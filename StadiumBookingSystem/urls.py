from django.contrib import admin
from django.urls import path
from TicketBooking.views import views,customer_views,match_views,booking_views,signup_views,login_views,index_views,matches_views,contact_views,users_views,create_views,match_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Client
    path('',index_views.index), # For CREATING customer, match and booking
    path('matches',matches_views.match),
    path('contact',contact_views.contact),
    path('login',login_views.login),
    path('signup',signup_views.signup),

    # Dashboard
    path('dashboard',views.dashboard),
    path('dashboard/customer',customer_views.customer),
    path('dashboard/booking', booking_views.booking),
    path('dashboard/match',match_views.match),
    path('dashboard/users',users_views.user),


    #Create
    path('dashboard/users/create',users_views.create),
    path('dashboard/matches/create',match_views.create),


    #Edit
    path('dashboard/users/edit/<int:id>',users_views.edit),
    path('dashboard/users/update/<int:id>',users_views.update),

    path('dashboard/matches/edit/<int:id>',match_views.edit),
    path('dashboard/matches/update/<int:id>',match_views.update),

    path('dashboard/customer/edit/<int:id>',customer_views.edit),
    path('dashboard/customer/update/<int:id>',customer_views.update),

    path('dashboard/booking/edit/<int:id>',booking_views.edit),
    path('dashboard/booking/update/<int:id>',booking_views.update),


    #Delete
    path('dashboard/users/delete/<int:id>',users_views.delete),
    path('dashboard/matches/delete/<int:id>',match_views.delete),
    path('dashboard/customer/delete/<int:id>',customer_views.delete),
    path('dashboard/booking/delete/<int:id>',booking_views.delete),


    #Search
    path('dashboard/users/search',users_views.search),
    path('dashboard/customers/search',customer_views.search),
    path('dashboard/matches/search',match_views.search),
    path('dashboard/bookings/search',booking_views.search),

    # path('entry',login_views.entry),
    path('entry',index_views.entry),

    #logout
    path('dashboard/logout',index_views.logout),
    path('logout',signup_views.logout),


]
