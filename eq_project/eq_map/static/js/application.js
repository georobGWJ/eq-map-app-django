$(document).ready(function() {
  console.log("Loaded!");
  tabActivator();
  initMap();
  mapListener;
  // dataTabListener();
  // mapTabListener();
  // vizTabListener();
  // userTabListener();
  google.maps.event.addListener(map, 'click', function( event ){
    alert( "Latitude: "+event.latLng.lat()+" "+", longitude: "+event.latLng.lng() );
  });

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

    google.maps.event.addListener(map, 'click', function( event ){
      document.getElementById("lat-field").value = event.latLng.lat();
      document.getElementById("long-field").value = event.latLng.lng();

      // alert( "Latitude: "+event.latLng.lat()+" "+", longitude: "+event.latLng.lng() );
    });
}


google.maps.event.addListener(map, 'click', function( event ){
  alert( "Latitude: "+event.latLng.lat()+" "+", longitude: "+event.latLng.lng() );
});
