$(document).ready(function() {
    console.log("document ready!");
      $('.animcard').on('click', function(){
    console.log(`whelp made it here!`);
        if ( $(this).hasClass('front') ) {
          $(this).removeClass('front');
          $(this).addClass('back');
        } else {
          $(this).removeClass('back');
          $(this).addClass('front');
        }
      });
    });

function cardDisplay() {
    console.log(`whelp made it here!`);
    // when clicked, 1- do animation to flip tile and 2- display centered as modal
} 
