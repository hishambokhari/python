// $('h1').dblclick(function(){
//   $(this).text("I was changed")
// })

// Key press

// $('input').eq(0).keypress(function(){
//   $('h3').toggleClass('turnBlue');
// })

// $('input').eq(0).keypress(function(event){
//   if (event.which === 13) {
//     $('h3').toggleClass('turnBlue');
//   }
// }) // 13 is the numerical codes for enter button -- .which gives you the numerical codes.


// on()

// $('h1').on('dblclick', function(){
//   $(this).toggleClass('turnBlue');
// })

// $('h1').on('mouseenter', function(){
//   $(this).toggleClass('turnBlue');
// })



// Animations and Effects


// Fade out
// $('input').eq(1).on('click', function(){
//   $('.container').fadeOut(3000)
// })

//Slide up
$('input').eq(1).on('click', function(){
  $('.container').slideUp(3000)
})

