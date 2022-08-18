(function($){
    $(function(){
  
      $('.sidenav').sidenav();
      $('.parallax').parallax();
      
    });
    
    $(function() {
      let allDates = $('div.bookings').children('h5') 
      let today = new Date()
      let dayInt = today.getDate()
      for (let i = 0; i < allDates.length; i++) {
        if (parseInt(allDates[i].textContent) === dayInt){
          let parent = allDates[i].parentNode
          $(parent).addClass('teal lighten-5 z-depth-2')
        }
      }
    })

  })(jQuery); 
