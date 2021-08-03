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
  var coveredM2 = document.getElementById("uiCoveredM2");
  var balconyM2 = document.getElementById("uiBalconyM2");
  var comuna = document.getElementById("uiComunas");
  var neighborhood = document.getElementById("uiNeighborhoods");
  var PredPrice = document.getElementById("uiPredictedPrice");

  var url = SERVICE_URL + "/predict_price";

  $.post(url, {
      bedrooms: beds,
      bathrooms: baths,
      covered_area_m2: parseFloat(coveredM2.value),
      balcony_area_m2: parseFloat(balconyM2.value),
      comuna: comuna.value,
      neighborhood: neighborhood.value
  }, function(data, status) {
      console.log(data.predicted_price);
      PredPrice.innerHTML = "<h2>CLP " + data.predicted_price.toString() + "</h2>";
      console.log(status);
  });
}

var comunasObject = {
  "Santiago": [
      "Centro Histórico De Santiago", 
      "Santa Isabel", 
      "Bulnes", 
      "San Diego",
      "Parque Almagro",
      "Bogotá - Sierra Bella",
      "Parque O'Higgins",
      "Ejército - Toesca",
      "Barrio Diez De Julio",
      "Barrio Yungay",
      "Barrio Brasil",
      "Barrio República",
      "Barrio Lastarria",
      "Franklin - Biobío",
      "Parque Los Reyes",
      "Barrio San Borja"
  ],
  "Las Condes": [
      "Barrio El Golf", 
      "Metro Escuela Militar", 
      "Metro Manquehue - Apumanque", 
      "Parque Arauco",
      "Centro Financiero",
      "Nueva Las Condes",
      "Metro Hernando De Magallanes",
      "Sebastián Elcano",
      "Alto Las Condes",
      "Vaticano",
      "Rotonda Atenas",
      "Mall Sport",
      "San Carlos De Apoquindo",
      "Los Dominicos",
      "Estoril",
      //"San Damián",
      "Parque Padre Alberto Hurtado",
      "Colón Oriente - Vital Apoquindo"
  ],
  "Providencia": [
      "Los Leones", 
      "Las Lilas", 
      "Pedro De Valdivia", 
      "Manuel Montt",
      "Metro Tobalaba - Mall Costanera",
      "Salvador",
      "Inés De Suárez",
      "Barrio Italia",
      "Campus Oriente",
      "Plaza Italia",
      "Metro Bilbao",
      "Pedro De Valdivia Norte",
      "Bellavista"
  ],
  "Ñuñoa": [
      "Metro Irarrázaval",
      "Plaza Ñuñoa",
      "Metro Monseñor Eyzaguirre",
      "Metro Ñuñoa",
      "Estadio Nacional",
      "Plaza Egaña",
      "Parque Juan Xxiii",
      "Parque San Eugenio - Metro Ñuble",
      "Diagonal Oriente",
      "Metro Simón Bolivar",
      "Juan Gómez Millas",
      "Villa Frei",
      "Diego De Almagro",
      "Parque Botánico",
      "Amapolas"
  ],
  "Vitacura": [
      "Parque Bicentenario",
      "Pío Xi",
      "Tabancura",
      "Jardín Del Este",
      "La Llavería",
      "Juan Xxiii",
      //"Santa María De Manquehue",
      "Estadio Manquehue",
      "Borde Río - Casa Piedra",
      //"Lo Curro",
      "Estadio Croata",
      "Nuestra Señora Del Rosario",
      "Villa El Dorado"
  ],
  "Estación Central": [
      "San Alberto Hurtado",
      "Metro Ecuador",
      "Metro Las Rejas",
      "Universidad De Santiago"
  ],
  "San Miguel": [
      "Lo Vial",
      "Ciudad Del Niño",
      "El Llano"
  ],
  "Independencia": [
      "Hospitales",
      "Plaza Chacabuco",
      "Independencia",
      "Juan Antonio Ríos",
      "Metro Cal Y Canto"
  ],
  "Lo Barnechea": [
      "La Dehesa",
      "Lo Barnechea",
      "Puente Nuevo",
      "Los Trapenses",
      "El Huinganal",
      "Plaza San Enrique",
      "Valle Escondido"
  ],
  "Macul": [
      "Macul",
      "Metro Camino Agrícola",
      "Metro Las Torres",
      "Villa Macul",
      "Las Dalias",
      "Santa Julia De Macul",
      "Escuela Agrícola",
      "Metro Carlos Valdovinos",
      "Metro Macul",
      "Metro Quilín",
      "Metro Los Presidentes"
  ],
  "La Florida": [
      "Plaza Vespucio",
      "La Florida",
      "Vicente Valdés",
      "Metro Mirador",
      "La Florida Alto",
      "Rojas Magallanes"
  ],
  "Recoleta": [
      "Cerro Blanco",
      "Bellavista",
      "Recoleta",
      "Patronato",
      "Cementerios"
  ],
  "Quinta Normal": [
      "Gruta De Lourdes",
      "Quinta Normal",
      "Parque Padre Renato Poblete",
      "Blanqueado",
      "Salvador Gutiérrez"
  ],
  "La Cisterna": [
      "Lo Ovalle",
      "Metro La Cisterna",
      "La Cisterna",
      "El Parrón"
  ],
  "San Joaquín": [
      "Rodrigo De Araya",
      "San Joaquín",
      "Carlos Valdovinos",
      "Metro San Joaquín"
  ],
  "La Reina": [
      "Blest Gana",
      "La Reina",
      "Metro Príncipe De Gales - Country Club",
      "Metro Simón Bolivar",
      "Carlos Ossandón"
  ],
  "Huechuraba": [
      "Pedro Fontova",
      "Bosques De La Pirámide",
      "Ciudad Empresarial",
      "Huechuraba"
  ]
}

window.onload = function() {
  var comunaSel = document.getElementById("uiComunas");
  var neighborhoodSel = document.getElementById("uiNeighborhoods");
  for (var x in comunasObject) {
    comunaSel.options[comunaSel.options.length] = new Option(x, x);
  }
  comunaSel.onchange = function() {
    //empty Neighborhoods dropdown
    neighborhoodSel.length = 1;
    //display correct values
    var y = comunasObject[this.value];
    for (var i = 0; i < y.length; i++) {
      neighborhoodSel.options[neighborhoodSel.options.length] = new Option(y[i], y[i]);
    }
  }

};
