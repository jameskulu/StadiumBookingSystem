$(document).ready(()=>{

// Book now button function
    $("#book").on('click',()=>{
           $(".form .container").show();
       });

// images

    $(".slidershow").mousedown(function(){
    return false;
    });

// admin login modal

    var message= document.getElementById('spanmsg');
    if (message){
    $(function(){
      $('#adminbtn').click();
      })
    }
})
