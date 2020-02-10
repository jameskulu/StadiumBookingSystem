from django import forms
from TicketBooking.models import Customer,Match,Booking,User

#### USER form

class UserForm_User(forms.ModelForm):

    User_Email = forms.CharField(widget=forms.TextInput(
    attrs={
            'class' : 'form-control',
            'placeholder':'Add Email',
            'autocomplete':'off'

    }
    ))

    User_Password = forms.CharField(widget=forms.PasswordInput(
    attrs={
            'class' : 'form-control',
            'placeholder':'Add Password'
    }
    ))

    class Meta:
        model = User
        fields = "__all__"


#### CUSTOMER FORM

class UserForm_Customer(forms.ModelForm):

    Customer_First_Name = forms.CharField(widget=forms.TextInput(
    attrs={
            'class' : 'form-control',
            'placeholder':'Add First Name',
            'autocomplete':'off'
    }
    ))

    Customer_Last_Name = forms.CharField(widget=forms.TextInput(
    attrs={
            'class' : 'form-control',
            'placeholder':'Add Last Name',
            'autocomplete':'off'
    }
    ))

    Customer_Email = forms.CharField(widget=forms.TextInput(
    attrs={
            'class' : 'form-control',
            'placeholder':'Add Email',
            'autocomplete':'off'
    }
    ))

    class Meta:
        model = Customer
        fields = "__all__"



#### Match Form

class UserForm_Match(forms.ModelForm):
    Match_Name = forms.CharField(widget=forms.TextInput(
    attrs={
            'class' : 'form-control',
            'placeholder':'Add Match',
            # 'onkeyup':'validateMatch()',
            'autocomplete':'off'
    }
    ))

    class Meta:
        model = Match
        fields = "__all__"


#### BOOKING FORM

class UserForm_Booking(forms.ModelForm):

    class Meta:
        model = Booking
        fields = "__all__"
