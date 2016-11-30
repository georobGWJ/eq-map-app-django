$(document).ready(function() {
  console.log("Loaded!");
  tabActivator();
  // dataTabListener();
  // mapTabListener();
  // vizTabListener();
  // userTabListener();
});

var tabActivator = function() {
  // Get tab id that is clicked on and make that <li> active
  $( ".tabs" ).click(function( event ) {
    // event.preventDefault();
    $(event.target).parent().addClass("active").siblings().removeClass("active");
  })
}

var dataTabListener = function(){
  $("#data-tab").click(function(event) {
    event.preventDefault();
    $("#main-container").html()
  })
};
