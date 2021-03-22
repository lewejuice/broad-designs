// Google maps API JS function, obtained from the google documentation
var mapsApiKey = $('#id_maps_api_key').text().slice(1, -1);

function initMap() {
  const map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 51.3666518, lng: 1.3858356},
    zoom: 9,
    mapId: 'f1e2fa33d3b68b37'
  });
  // Broad designs logo file for the map marker
  const image =
    "https://broad-designs.s3.eu-west-2.amazonaws.com/media/bdesignlogo.png";
  var icon = {
    url: image, 
    scaledSize: new google.maps.Size(40, 40),
    origin: new google.maps.Point(0,0),
    anchor: new google.maps.Point(0, 0)
  };
  const beachMarker = new google.maps.Marker({
    position: { lat: 51.364276, lng: 1.429022 },
    map,
    icon: icon,
  });
}