(function($){
    $(function(){
  
      $('.sidenav').sidenav();
      $('.parallax').parallax();
      $('.scrollspy').scrollSpy();
      $('.collapsible').collapsible();
      $('.tooltipped').tooltip();
      $('#message-box').fadeOut(10000);

    });

    // raw function show and hide booking list
    $(function() {
      let allDates = $('div.bookings').children('h5') 
      let today = new Date()
      let dayInt = today.getDate()

      // green-mark todays divs
      for (let i = 0; i < allDates.length; i++) {
        if (parseInt(allDates[i].textContent) === dayInt){
          let parent = allDates[i].parentNode
          $(parent).addClass('teal lighten-5 z-depth-2')
        }
      }
      // find and hide dates under today
      let allMonths = $('div.bookings').children('h6') 
      let allYears = $('div.bookings').children('h7')

      let monthInt = today.getMonth() + 1
      let yearInt = today.getYear()

      for (let j = 0; j < allDates.length; j++) {
        if
        // today is greater then booking day
        ((parseInt(allDates[j].textContent) < dayInt) &&
        // month is greater then booking month
        (parseInt(allMonths[j].textContent) <= monthInt) &&
        // year is greater then booking year
        (parseInt(allYears[j].textContent) <= yearInt)
        ){
          let parent = allDates[j].parentNode
          $(parent).hide()
        }
      }

    })

  })(jQuery);
