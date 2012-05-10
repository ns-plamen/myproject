$(document).ready(function(){
  $(".day_style").click(function(){
      $(".selected_day").toggleClass("selected_day");
      $(this).addClass("selected_day");
      //$(this).toggleClass("old_selection");
      var select_date = $(this).attr("id");
      var week_day = new Date(now_year, now_month, select_date);
      var weekdays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
      var months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
      var weekday = weekdays[week_day.getDay()];
      var month = months[week_day.getMonth()];
      $("#display").val(weekday+" "+month+" "+select_date+" "+now_year);
    }
  );
  //select weekdays
  $(".weekdays").click(function(){
      $(".selected_day").toggleClass("selected_day");
      $(this).addClass("selected_day");
      var selected_weekday = $(this).attr("id");

      if (selected_weekday == "mon")   {
          $("#display").val("all Monday");
          var calculated_weekdays = $("#month_monday").attr("value");
          calculated_weekdays = calculated_weekdays.substring(1, calculated_weekdays.length-1).split(", ");
          for(var i=0; i<calculated_weekdays.length; i++){ 
            $("#"+calculated_weekdays[i]).toggleClass("selected_day"); 
          }
      }
      if (selected_weekday == "tue")   {
          $("#display").val("all Tuesday");
          var calculated_weekdays = $("#month_tuesday").attr("value");
          calculated_weekdays = calculated_weekdays.substring(1, calculated_weekdays.length-1).split(", ");
          for(var i=0; i<calculated_weekdays.length; i++){ 
            $("#"+calculated_weekdays[i]).toggleClass("selected_day"); 
          }  
      }
      if (selected_weekday == "wed")   {
          $("#display").val("all Wednesday");
          var calculated_weekdays = $("#month_wednesday").attr("value");
          calculated_weekdays = calculated_weekdays.substring(1, calculated_weekdays.length-1).split(", ");
          for(var i=0; i<calculated_weekdays.length; i++){ 
            $("#"+calculated_weekdays[i]).toggleClass("selected_day"); 
          } 
      }
      if (selected_weekday == "thu")   {
          $("#display").val("all Thursday");
          var calculated_weekdays = $("#month_thursday").attr("value");
          calculated_weekdays = calculated_weekdays.substring(1, calculated_weekdays.length-1).split(", ");
          for(var i=0; i<calculated_weekdays.length; i++){ 
            $("#"+calculated_weekdays[i]).toggleClass("selected_day"); 
          } 
      }
      if (selected_weekday == "fri")   {
          $("#display").val("all Friday");
          var calculated_weekdays = $("#month_friday").attr("value");
          calculated_weekdays = calculated_weekdays.substring(1, calculated_weekdays.length-1).split(", ");
          for(var i=0; i<calculated_weekdays.length; i++){ 
            $("#"+calculated_weekdays[i]).toggleClass("selected_day"); 
          }
      }
      if (selected_weekday == "sat")   {
          $("#display").val("all Satarday");
          var calculated_weekdays = $("#month_saturday").attr("value");
          calculated_weekdays = calculated_weekdays.substring(1, calculated_weekdays.length-1).split(", ");
          for(var i=0; i<calculated_weekdays.length; i++){ 
            $("#"+calculated_weekdays[i]).toggleClass("selected_day"); 
          }
      }
      if (selected_weekday == "sun")   {
          $("#display").val("all Sunday");
          var calculated_weekdays = $("#month_sunday").attr("value");
          calculated_weekdays = calculated_weekdays.substring(1, calculated_weekdays.length-1).split(", ");
          for(var i=0; i<calculated_weekdays.length; i++){ 
            $("#"+calculated_weekdays[i]).toggleClass("selected_day"); 
          }
      }

         
    }
  );

//alert("debug");
});


      












