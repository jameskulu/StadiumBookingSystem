$(document).ready(()=>{



// User Search

 $("#usersearch").keydown(()=>{
		$.ajax({
			data:{search:$("#usersearch").val()},
			url:'/dashboard/users/search',
			method:'GET',
			success:function(data){
			console.log(data)
				$("tr").not("tr:first").remove();
				let html="";
				for(user of data){

					html+="<tr>";
						html+="<td>"+user.User_Id+"</td>";
						html+="<td>"+user.User_Email+"</td>";
						html+="<td>"+user.User_Password+"</td>";
						html+="<td><a href='/dashboard/users/edit/"+user.User_Id+"'> <button class='btn btn-primary'>Edit</button></a> <a href='/dashboard/users/delete/"+user.User_Id+"'> <button class='btn btn-danger'>Delete</button></a></td>";
					html+="</tr>";
					$("table").append(html);
					}

			},error:function(error){
			console.log(error)
			},complete:function(){
			console.log("complete")
			}
		})
	})


 // Match Search

  $("#matchessearch").keydown(()=>{
 		$.ajax({
 			data:{search:$("#matchessearch").val()},
 			url:'/dashboard/matches/search',
 			method:'GET',
 			success:function(data){
 			console.log(data)
 				$("tr").not("tr:first").remove();
 				let html="";
 				for(match of data){

 					html+="<tr>";
 						html+="<td>"+match.Match_Id+"</td>";
 						html+="<td>"+match.Match_Name+"</td>";
 						html+="<td><a href='/dashboard/matches/edit/"+match.Match_Id+"'><button class='btn btn-primary'>Edit</button></a> <a href='/dashboard/matches/delete/"+match.Match_Id+"'><button class='btn btn-danger'>Delete</button></a></td>";
 					html+="</tr>";
 					$("table").append(html);
 					}

 			},error:function(error){
 			console.log(error)
 			},complete:function(){
 			console.log("complete")
 			}
 		})
 	})


  //  Customer Search

  $("#customerssearch").keydown(()=>{
 		$.ajax({
 			data:{search:$("#customerssearch").val()},
 			url:'/dashboard/customers/search',
 			method:'GET',
 			success:function(data){
 			console.log(data)
 				$("tr").not("tr:first").remove();
 				let html="";
 				for(customer of data){

 					html+="<tr>";
 						html+="<td>"+customer.Customer_Id+"</td>";
            html+="<td>"+customer.Customer_First_Name+"</td>";
            html+="<td>"+customer.Customer_Last_Name+"</td>";
 						html+="<td>"+customer.Customer_Email+"</td>";
 						html+="<td>"+customer.Customer_Password+"</td>";
 						html+="<td><a href='/dashboard/customer/edit/"+customer.Customer_Id+"'><button class='btn btn-primary'>Edit</button></a> <a href='/dashboard/customer/delete/"+customer.Customer_Id+"'><button class='btn btn-danger'>Delete</button></a></td>";
 					html+="</tr>";
 					$("table").append(html);
 					}

 			},error:function(error){
 			console.log(error)
 			},complete:function(){
 			console.log("complete")
 			}
 		})
 	})


// Booking Search

  $("#bookingssearch").keydown(()=>{
 		$.ajax({
 			data:{search:$("#bookingssearch").val()},
 			url:'/dashboard/bookings/search',
 			method:'GET',
 			success:function(data){
 			console.log(data)
 				$("tr").not("tr:first").remove();
 				let html="";
 				for(booking of data){

 					html+="<tr>";
 						html+="<td>"+booking.Booking_Id+"</td>";
 						html+="<td>"+booking.No_Of_Tickets+"</td>";
 						html+="<td>"+booking.Type_Of_Seats+"</td>";
            html+="<td>"+booking.Match_id+"</td>";
            html+="<td>"+booking.Customer_id+"</td>";
 						html+="<td><a href='/dashboard/booking/edit/"+booking.Booking_Id+"'><button class='btn btn-primary'>Edit</button></a> <a href='/dashboard/booking/delete/"+booking.Booking_Id+"'><button class='btn btn-danger'>Delete</button></a></td>";
 					  html+="</tr>";
 					$("table").append(html);
 					}

 			},error:function(error){
 			console.log(error)
 			},complete:function(){
 			console.log("complete")
 			}
 		})
 	})

  if ($("#page").val() == 1){
      $("#prev").prop("disabled",true)
  }

  $(document).on('click', '#deletecustomer', function(){
    return confirm('Are you sure you want to delete this?');
})

$(document).on('click', '#deletematch', function(){
  return confirm('Are you sure you want to delete this?');
})

$(document).on('click', '#deleteuser', function(){
  return confirm('Are you sure you want to delete this?');
})

$(document).on('click', '#deletebooking', function(){
  return confirm('Are you sure you want to delete this?');
})

$(document).on('click', '#logoutdash', function(){
  return confirm('Do you sure you want to log out?');
})




})
