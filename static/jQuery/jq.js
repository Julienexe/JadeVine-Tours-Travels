//Mobile Navigation bar
$(document).ready(function(){

  $("#menubars").click(function(){
    $("#navbar").slideToggle("slow");
  });


//Hide Navigation bar onclick out of navbar
document.onclick = function(event) {
  if (!(event.target.matches(' #menubars') || event.target.matches(' #navbar'))) {
    $("#navbar").slideUp("slow");
  }
};

//Animate website logo
$('#logo').animate({opacity:'1'},1500);

//Return to top button
$("footer button").click(function(){
  $("html,body").animate({ scrollTop:0 }, 900);
});


//Image slideshow
$(".slideshow > div:gt(0)").hide();
$('.slideshow > div span').animate({opacity:'1'},1000);
$('.slideshow > div span .head1').animate({opacity:'1'},2000);
$('.slideshow > div span .p1').animate({opacity:'1'},2200);
var inter = setInterval(startAnimating, 10000);

function  startAnimating() {
  $('.slideshow > div span').animate({opacity:'0'},700);
  $('.slideshow > div span .head1').animate({opacity:'0'},600);
  $('.slideshow > div span .p1').animate({opacity:'0'},500);

  $('.slideshow > div:first').slideDown(1000);

  $('.slideshow > div span').animate({opacity:'1'},1000);
  $('.slideshow > div span .head1').animate({opacity:'1'},2000);
  $('.slideshow > div span .p1').animate({opacity:'1'},2200);
  $('.slideshow > div:first').next().slideUp(1000).end().appendTo('.slideshow');
}

$("#right").click(function(){
  clearInterval(inter);
  $('.slideshow > div span').animate({opacity:'0'},500);
  $('.slideshow > div span .head1').animate({opacity:'0'},400);
  $('.slideshow > div span .p1').animate({opacity:'0'},300);
  $('.slideshow > div:first').slideDown(500).next().slideUp(500).end().appendTo('.slideshow');
  $('.slideshow > div span').animate({opacity:'1'},300);
  $('.slideshow > div span .head1').animate({opacity:'1'},400);
  $('.slideshow > div span .p1').animate({opacity:'1'},500);
});
$("#left").click(function(){
  clearInterval(inter);
  /*$('.slideshow > div span').animate({opacity:'0'},700);
  $('.slideshow > div span .head1').animate({opacity:'0'},600);
  $('.slideshow > div span .p1').animate({opacity:'0'},500);
  $('.slideshow > div:first').slideUp(1000).prev().slideDown(1000).end().appendTo('.slideshow');
  $('.slideshow > div span').animate({opacity:'1'},1000);
  $('.slideshow > div span .head1').animate({opacity:'1'},2000);
  $('.slideshow > div span .p1').animate({opacity:'1'},2200);*/
});
//---------------------------****************---------------------------------

$("#contactUsForm").submit(function(e){
  e.preventDefault();
  if (($("#phoneNum").val().length < 10) || ($("#phoneNum").val().length > 11)) {
    $("#contactUsForm .smsMob")
    .text("Phone number must be 10 or 11 digits.")
    .css("display","block")
    .css("color","#F44336")
    .fadeIn('fast')
    .delay(3000)
    .fadeOut('slow');
  } else {
    $.ajax({
        type: 'POST',
        url: 'save_contact.php',
        data: new FormData(this),
        dataType: 'json',
        contentType: false,
        cache: false,
        processData:false,
        beforeSend: function() {
          $("#contactUsForm .subBtn").css("display","none");
          $("#contactUsForm .loading").fadeIn('fast');
          $('#contactUsForm .sms').text("").css("display","none");
        },
        success: function(response) {
            if (response.status == 1) {
              $('#contactUsForm')[0].reset();
              $('#contactUsForm .sms')
              .text(response.message)
              .css("display","block")
              .css("color","green")
              .css("border-bottom","1px solid green")
              .delay(3000)
              .fadeOut('slow');
              $("#contactUsForm").animate({ scrollTop:0 }, "slow");
            } else {
              $('#contactUsForm .sms')
              .text(response.message)
              .css("display","block")
              .css("color","#F44336")
              .css("border-bottom","1px solid #F44336")
              .delay(3000)
              .fadeOut('slow');
              $("contactUsForm").animate({ scrollTop:0 }, "slow");
            }
            $("#contactUsForm .loading").css("display","none");
            $("#contactUsForm .subBtn").fadeIn('fast');
        }
    });
  }
});

});
