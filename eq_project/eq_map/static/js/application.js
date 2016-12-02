$(document).ready(function() {
  console.log("Loaded!");
  tabActivator();
  plotEarthquakes();
  initMap();
});

var map;
var markers = [];

var tabActivator = function() {
  // Get tab id that is clicked on and make that <li> active
  $( ".tabs" ).click(function( event ) {
    // event.preventDefault();
    $(event.target).parent().addClass("active").siblings().removeClass("active");
  })
}

var getCircle = function(magnitude) {
  return {
    path: google.maps.SymbolPath.CIRCLE,
    fillColor: 'red',
    fillOpacity: 0.4,
    scale: Math.pow(2, magnitude) / 2,
    strokeColor: 'white',
    strokeWeight: 0.5
  };
}

// Loop through the results array and place a marker for each
// set of coordinates.
eqfeed_callback = function(eqs) {
  for (var idx = 0; idx < eqs.length; idx++) {
    var an_event = eqs[idx];
    var latLng = new google.maps.LatLng(an_event.eq_lat, an_event.eq_long);
    // console.log(getCircle(an_event.magnitude));
    var marker = new google.maps.Marker({
      position: latLng,
      icon: (getCircle(an_event.mag)),
      title: ("MAG: "+an_event.mag),
      // title: ("DATE: "+an_event.eq_date +"  MAG: "+an_event.mag),
      map: map
    });
    markers.push(marker);
  }
}


var plotEarthquakes = function() {
  // console.log("Listener loaded.")
  $('#plot-all-form').submit(function(event) {
    event.preventDefault();
    console.log("Clicked!")

    $.ajax({
            // action: "/locations",
            url: "/locations/",
            method: "GET",
            dataType: "json",
            context: document.body
          }).done(function(response) {
            console.log("AJAX Response!")
            earthquakes = response;
            eqfeed_callback(earthquakes);
          });
  })
};

// Sets the map on all markers in the array.
var setMapOnAll = function(map) {
  for (var i = 0; i < markers.length; i++) {
    markers[i].setMap(map);
  }
}

// Removes the markers from the map, but keeps them in the array.
var clearMarkers = function() {
  setMapOnAll(null);
}

// Deletes all markers in the array by removing references to them.
var deleteMarkers = function() {
  clearMarkers();
  markers = [];
}

var clearListener = function() {
  $('#clear-all-form').submit(function(event){
    event.preventDefault();
    deleteMarkers();
  })
}

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




// var getEarthquakes =   $.ajax({
//         url: "/events",
//         method: "GET",
//         dataType: "json",
//         context: document.body
//       }).done(function(response) {
//         earthquakes = response;
//         eqfeed_callback(earthquakes);
//       });
