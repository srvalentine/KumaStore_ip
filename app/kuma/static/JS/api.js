var myHeaders = new Headers();
myHeaders.append("apikey", "vbix3Le0zOibhcasnMxDgk90BoyPU46R");


document.getElementsByClassName('signo').innerHTML = 'CLP'; 

var requestOptions = {
  method: 'GET',
  redirect: 'follow',
  headers: myHeaders
};

const to = 'CLP';
const from = 'USD';


function cambioMoneda(){
  var select = document.getElementById('divisa');
  var option = select.value;
  var pesos = document.getElementsByClassName('precio');
  for(i = 0; i < document.getElementsByClassName('precio').length ; i++){
    const amount = document.getElementsByClassName('precio')[i].innerHTML;
    if(option == 1){
      console.log("Divisa por defecto");
      for(var i = 0; i < pesos.length; i++){
         pesos[i].innerHTML = pesos[i].getAttribute('data-clp');
      }
    }else if(option == 2){
      fetch(`https://api.apilayer.com/exchangerates_data/convert?to=${to}&from=${from}&amount=1`, requestOptions)
      .then(response => response.json())
      .then(data => {
        var resultado = data.result;
        console.log(resultado);
        for(var i = 0; i < pesos.length; i++){
          var clpValue = pesos[i].getAttribute('data-clp');
          var usdValue = clpValue / resultado;
          pesos[i].innerHTML = usdValue.toFixed(2);
        }
      })
      .catch(error => console.log('error', error));
    }
  }
}


var map = L.map('map').setView([-33.4513,-70.6385], 12);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
  }).addTo(map);

  L.marker([-33.50384612119525, -70.60743010793385]).addTo(map)
    .bindPopup('La sucursal atendida está aquí.')
    .openPopup();
















  
  





