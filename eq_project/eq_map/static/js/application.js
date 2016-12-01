$(document).ready(function() {
  console.log("Loaded!");
  tabActivator();
  initMap();
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

var map;

// function initMap() {
var initMap = function() {
  centerCoords = new google.maps.LatLng(38.01324,-98.64066)

  map = new google.maps.Map(document.getElementById('map'), {
    center: centerCoords,
    zoom: 4,
    mapTypeId: 'terrain'
  });
}
