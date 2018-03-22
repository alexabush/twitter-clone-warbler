$(function() {
  // var $ajaxButton = $('.ajax_button');
  // console.log('page has loaded');
  // $ajaxButton.on('click', function() {
  // console.log('clicked');
  // $.getJSON('http://localhost:5000/json', function(message) {
  // console.log(message.text);
  // });
  // });

  $('#messages').on('click', function(event) {
    console.log(
      $(event.target)
        .closest('li')
        .attr('id')
    );
  });

  // $('#messages').on('click', function(event) {
  //   console.log(
  //     $(event.target)
  //       .closest('li')
  //       .attr('id')
  //   );
  // });
});
