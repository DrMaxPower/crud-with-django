(function($){
    $(function(){
  
      $('.sidenav').sidenav();
      $('.parallax').parallax();
  
    }); 
  })(jQuery); 

  $(document).ready(function(){
    $('.datepicker').datepicker();
    $('.timepicker').timepicker();
  });

  // Change color of p set on todays date in index
  // simple setup.. 
  // let today = new Date()
  // let dayInt = today.getDate()
  // let monthInt = today.getMonth() + 1
  // get mote specific then p
  // let pDateFromDjango = $('p').text()
  // => 08 17
  // join numbers
  //  check if numberstring is equal
  // if equal add light green color to paragraphs
  // make shore it will only color "todays" paragraph