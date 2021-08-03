function getBedroomsValue() {
  var uiBedrooms = document.getElementsByName("uiBedrooms");
  for(var i in uiBedrooms) {
    if(uiBedrooms[i].checked) {
      return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}
  
function getBathroomsValue() {
  var uiBathrooms = document.getElementsByName("uiBathrooms");
  for(var i in uiBathrooms) {
    if(uiBathrooms[i].checked) {
      return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function onClickedPredictPrice() {
  console.log("Predict price button clicked");
  var beds = getBedroomsValue();
  var baths = getBathroomsValue();
  var totalM2 = document.getElementById("uiTotalM2");
  var balconyM2 = document.getElementById("uiBalconyM2");
  var comuna = document.getElementById("uiComunas");
  var PredPrice = document.getElementById("uiPredictedPrice");

  var url = SERVICE_URL + "/predict_price";

  $.post(url, {
      bedrooms: beds,
      bathrooms: baths,
      total_area_m2: parseFloat(totalM2.value),
      balcony_area_m2: parseFloat(balconyM2.value),
      comuna: comuna.value
  }, function(data, status) {
      console.log(data.predicted_price);
      PredPrice.innerHTML = "<h2>CLP " + data.predicted_price.toString() + "</h2>";
      console.log(status);
  });
}

function onPageLoad() {
  console.log( "document loaded" );
  var url = SERVICE_URL + "/get_location_names";
  $.get(url, function(data, status) {
      console.log("got response for get_comunas request");
      if(data) {
          var comunas = data.comunas;
          var uiComunas = document.getElementById("uiComunas");
          $('#uiComunas').empty();
          for(var i in comunas) {
              var opt = new Option(comunas[i]);
              $('#uiComunas').append(opt);
          }
      }
  });
}

window.onload = onPageLoad;
