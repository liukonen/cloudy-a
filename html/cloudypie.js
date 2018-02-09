//if the document is ready
$(document).ready(function()
{
 //placeholder
 var outText = "";
 
 //Load the output Json object for looping
 $.getJSON("output.json", function(result)
 {
  //for each forcast, generate a div tag for it
  result.forecast.txt_forecast.forecastday.forEach((product, index) => 
  {
	  outText += "<div class=\"col-md-4\"><div class=\"card mb-4 bg-secondary\"><h3 class=\"card-header\"><img src=\"" + product.icon_url +  "\" />" +  product.title +  "</h3><div class=\"card-body\"><p class=\"card-text\">" + product.fcttext + "</p></div></div></div>";
  });
  //Add the div tags to the screen
  $("#WeatherForcasts").append(outText);
 
  //if we have errors in the error log, display them, else display the last updated value
  $.get("error.log", function(response) 
  {
     var logfile = response;
	 if (logfile === "")
	 {
		 $("#LastUpdated").load("Lastupdated.log"); 
		 document.getElementById("LastUpdated").className += " alert-success";
	 }
     else
	 {
		 document.getElementById("LastUpdated").className += " alert-danger";
		 $("#LastUpdated").load("error.log")
     }
  });
 });
});
