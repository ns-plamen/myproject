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
         $(".cal_tab td:nth-child(1)").toggleClass("selected_day");
         $(".blank_style").removeClass("selected_day");
         $("#display").val("All Monday");
      }
      if (selected_weekday == "tue")   {
         $(".cal_tab td:nth-child(2)").toggleClass("selected_day");
         $(".blank_style").removeClass("selected_day");
         $("#display").val("All Tuesday");
      }
      if (selected_weekday == "wed")   {
         $(".cal_tab td:nth-child(3)").toggleClass("selected_day");
         $(".blank_style").removeClass("selected_day");
         $("#display").val("All Wednesday");
      }
      if (selected_weekday == "thu")   {
         $(".cal_tab td:nth-child(4)").toggleClass("selected_day");
         $(".blank_style").removeClass("selected_day");
         $("#display").val("All Thursday");
      }
      if (selected_weekday == "fri")   {
         $(".cal_tab td:nth-child(5)").toggleClass("selected_day");
         $(".blank_style").removeClass("selected_day");
         $("#display").val("All Friday");
      }
      if (selected_weekday == "sat")   {
         $(".cal_tab td:nth-child(6)").toggleClass("selected_day");
         $(".blank_style").removeClass("selected_day");
         $("#display").val("All Saturday");
      }
      if (selected_weekday == "sun")   {
         $(".cal_tab td:nth-child(7)").toggleClass("selected_day");
         $(".blank_style").removeClass("selected_day");
         $("#display").val("All Sunday");
      }
    });

//alert("debug");
});


      












