function validateUser(){
  var email = document.getElementById('id_User_Email').value;
  var password=document.getElementById('id_User_Password').value;

  if(email.indexOf('@')<=0){
    document.getElementById('spanusercreate').innerHTML="**invalid '@' position";
    return false;
  }

  if(password.length < 8){
      document.getElementById('spanuserpassword').innerHTML="**Please enter more than 8 characters";
      return false;
  }
  alert("User has been added successfully !")
}

function validateMatch(){

  var match = document.getElementById('id_Match_Name').value;
  if(match.includes(" vs ")) {}
  else{
    document.getElementById('spanmatchcreate').innerHTML="**Match name should be in 'Friends Club vs Brigade Boys Club - ANFA Stadium (15/2/2020 13:45)' format";
    return false;
  }
  alert("Match has been added successfully !")
}


function validateCustomer(){
  var firstname=document.getElementById('id_Customer_First_Name').value;
  var lastname=document.getElementById('id_Customer_Last_Name').value;
  var email = document.getElementById('id_Customer_Email').value;

  if (!isNaN(firstname)){
    document.getElementById('spancustomerfirstname').innerHTML="**Only characters are allowed";
    return false;
  }
    if (!isNaN(lastname)){
      document.getElementById('spancustomerlastname').innerHTML="**Only characters are allowed";
      return false;
    }

    if(email.indexOf('@')<=0){
      document.getElementById('spancustomeremail').innerHTML="**invalid '@' position";
      return false;
    }

    alert("Registered successfully !")
}

function validateBooking(){
  alert("Ticket has been booked successfully !")
}

function validateBookingEdit(){
  var email=document.getElementById('bookingemailedit').value;
  if(email.indexOf('@')<=0){
    document.getElementById('spanbookingemailedit').innerHTML="**invalid '@' position";
    return false;
  }
  if((email.charAt(a.length-4)!='.') && (email.charAt(a.length-3)!='.')) {
    document.getElementById('spanusercreate').innerHTML="**invalid '.' position";
    return false;
  }
  alert("Edited successfully !")
}

function validateUserEdit(){
  var email = document.getElementById('useremailedit').value;
  var password=document.getElementById('userpasswordedit').value;

  if(email.indexOf('@')<=0){
    document.getElementById('spanuseremailedit').innerHTML="**invalid '@' position";
    return false;
  }

  if(password.length < 8){
      document.getElementById('spanuserpasswordedit').innerHTML="**Please enter more than 8 characters";
      return false;
  }
  alert("Edited successfully !")
}

function validateCustomerEdit(){

  var firstname=document.getElementById('customerfirstnameedit').value;
  var lastname=document.getElementById('customerlastnameedit').value;
  var email = document.getElementById('customeremailedit').value;

  if (!isNaN(firstname)){
    document.getElementById('spancustomerfirstnameedit').innerHTML="**Only characters are allowed";
    return false;
  }
    if (!isNaN(lastname)){
      document.getElementById('spancustomerlastnameedit').innerHTML="**Only characters are allowed";
      return false;
    }

    if(email.indexOf('@')<=0){
      document.getElementById('spancustomeremailedit').innerHTML="**invalid '@' position";
      return false;
    }
    alert("Edited successfully !")
}


function validateMatchEdit(){

  var match = document.getElementById('matchedit').value;
  if(match.includes(" vs ")) {}
  else{
    document.getElementById('spanmatchedit').innerHTML="**Match name should be in 'Friends Club vs Brigade Boys Club - ANFA Stadium (15/2/2020 13:45)' format";
    return false;
  }
  alert("Edited successfully !")
}
