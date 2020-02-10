from django.db import models

class Customer(models.Model):
    Customer_Id = models.AutoField(auto_created=True,primary_key=True)
    Customer_First_Name = models.CharField(max_length=100,default="Harry")
    Customer_Last_Name = models.CharField(max_length=100,default="Harry")
    Customer_Email = models.CharField(max_length=100,default="Harry")

class Match(models.Model):
    Match_Id = models.AutoField(auto_created=True,primary_key=True)
    Match_Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Match_Name

class Booking(models.Model):
    Booking_Id = models.AutoField(auto_created=True,primary_key=True)
    No_Of_Tickets = models.CharField(max_length=100)
    Type_Of_Seats = models.CharField(max_length=100,default="seat")
    Customer_id = models.CharField(max_length=100,default="1")
    Match = models.ForeignKey(Match, on_delete = models.CASCADE,default=1)


class User(models.Model):
    User_Id = models.AutoField(auto_created=True,primary_key=True)
    User_Email = models.CharField(max_length=100)
    User_Password = models.CharField(max_length=100)

class Meta:
    db_table="Customer"
    db_table="Booking"
    db_table="Match"
    db_table="User"
